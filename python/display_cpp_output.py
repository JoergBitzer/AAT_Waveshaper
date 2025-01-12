import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import scipy.signal as signal

# Load the data
data,fs = sf.read('C:/AudioDev/build/AAT_Waveshaper/tester/ConsoleAppExample_artefacts/Debug/SweepIn.wav')
data2,fs = sf.read('C:/AudioDev/build/AAT_Waveshaper/tester/ConsoleAppExample_artefacts/Debug/SweepOut.wav')

# Plot the data as spectrogram
f, t, Sxx = signal.spectrogram(data2, fs, nperseg=1024)
fig, ax = plt.subplots()
ax.pcolormesh(t, f, 10*np.log10(Sxx))
ax.set_ylabel('Frequency [Hz]')
ax.set_xlabel('Time [sec]')

plt.show()

