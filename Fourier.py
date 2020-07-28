from math import sin, pi
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

accuracy = 1000

def Fourier(name):
    data = pd.read_csv(name + '.csv')
    Coord = data["Coord"]
    Voltage = data["Voltage"]
    plt.plot(Coord, Voltage)
    plt.grid(True)
    plt.savefig(name + '_graph.jpg', dpi=300)

    spectrum = np.fft.rfft(Voltage)
    freq = np.fft.rfftfreq(len(Voltage), (Coord[len(Coord) - 1] - Coord[0]) / len(Coord))
    # Additional processing to get correct xlim
    # plt.xlim(0,120)
    

    plt.plot(freq, spectrum)
    plt.grid(True)
    plt.savefig(name + '_spectrum.jpg', dpi=300)
    tmp = [[freq[i], spectrum[i]] for i in range(len(freq))]
    frame = pd.DataFrame(tmp, columns=['frequency', 'power'])
    frame.to_csv(name + "_fourier.csv", index=False)
    print("Fourier transformation complete")


if __name__ == "__main__":
    Fourier("data")