import pandas as pd 
import numpy as np 

def Averaging(name, number):
    data = []
    for i in range(number):
        data.append(pd.read_csv(name + str(i + 1) + '.csv')) 
    averaged = []
    for i in range(len(data[0]["Coord"])):
        if i % 2:
            data[i].iloc[::-1]
    for j in range(min([len(data[i]) for i in range(len(data))])):
        coord_sum_i = 0
        voltage_sum_i = 0
        for i in range(len(data)):
            coord_sum_i += data[i]["Coord"][j]
            voltage_sum_i += data[i]["Voltage"][j]
        averaged.append([coord_sum_i / len(data), voltage_sum_i / len(data)])
    frame = pd.DataFrame(averaged, columns=['Coord', 'Voltage'])
    frame.to_csv(name + '.csv', index=False)
    print("Averaging complete")