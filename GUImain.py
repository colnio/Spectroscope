from GUI import Ui_Spectroscope
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time
import Fourier
import pandas as pd 
import numpy as np
import Averaging

length_of_pass = 113.6 # mm
filename = 'data'
speed = 1000000
port = 'COM5'
power = 128
passes = 1
mirror_speed = length_of_pass / 120 # 1 mm/s TO CHANGE!!!!!!

def measurements():
    miss_count = 0
    print("Started to measure")
    global filename, port, passes, power, ui, speed
    with serial.Serial(port, speed) as ser:
        # ser.write(b"S" + str(power).encode('ASCII') + b'-')
        reverses_times = []
        Coord = []
        Voltage = []
        c_passes = 0
        ser.write(("M" + str(passes) + '-').encode('ASCII'))
        t = time.time()
        coord = 0
        direction = 1
        while c_passes < passes:
            try:
                line = ser.readline()   # read a '\n' terminated line
                if b'*' in line:
                    reverses_times.append([Coord[-1], len(Coord)])
                    c_passes += 1
                    direction *= -1
                else:
                    coord = coord + mirror_speed * direction * (time.time() - t)
                    Coord.append(coord)
                    Voltage.append((int(line) / 1024) * 5)
            except ValueError:
                Coord.pop(-1)
                miss_count += 1
                continue

    ui.Graph.plot(Coord[:reverses_times[0][-1]:], Voltage[:reverses_times[0][-1]:])

    for i in range(passes):
        l = (0 if i == 0 else reverses_times[i-1][-1])
        r = (len(Coord) if i == passes - 1 else reverses_times[i+1][-1]) 
        tmp = [[Coord[i], Voltage[i]] for i in range(l, r)]
        if i % 2 == 1:
            tmp.reverse()
        frame = pd.DataFrame(tmp, columns=['Coord', 'Voltage'])
        frame.to_csv(filename + str(i+1) + ".csv", index=False)
    
    
    print("Measured, miss:\t", miss_count)

def set_port():
    global port
    global ui
    port = ui.portLine.text()
    print("Port set: ", port)

def set_passes():
    global passes
    global ui 
    passes = int(ui.passesLine.text())
    print("The number of passes set: ", speed)

def set_power():
    global power 
    global ui 
    power = int(ui.accelLine.text())
    print("Power set: ", power)

def set_file():
    global filename
    global ui 
    filename = ui.fileLine.text()
    print("File set: ", filename)

def transform():
    global filename, passes
    global ui
    Averaging.Averaging(filename, passes)
    Fourier.Fourier(filename)
    freq = []
    power = []
    with open(filename + '_fourier.csv', 'r') as data: 
        _ = data.readline()
        _ = data.readline()
        for i in data.readlines():
            line = i.split(',')
            freq.append(float(line[0]))
            power.append(abs(complex(line[-1])))
    ui.fourierGraph.plot(freq, power)
    print("Transform finished")
            


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Spectroscope()
ui.setupUi(MainWindow)

ui.portButton.clicked.connect(set_port)
ui.passesButton.clicked.connect(set_passes)
ui.accelButton.clicked.connect(set_power)
ui.fileButton.clicked.connect(set_file)
ui.startButton.clicked.connect(measurements)
ui.fourierButton.clicked.connect(transform)

MainWindow.show()
sys.exit(app.exec_())