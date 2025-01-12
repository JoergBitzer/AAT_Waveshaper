import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import soundfile as sf

# sinussweep
def gen_sweep(f_start, f_end, duration, fs):
    t = np.linspace(0, duration, int(duration*fs), False)
    sweep = signal.chirp(t, f_start, duration, f_end, method='linear')
    return sweep

fs = 44100  
f_start = 200
f_end = 20000
duration = 5
sweep = gen_sweep(f_start, f_end, duration, fs)

# upsampling
upsamplefactor = 4
sweep_up = signal.resample_poly(sweep, upsamplefactor, 1)
# non linearity
y = 1.5*sweep_up - 0.5*sweep_up*sweep_up*sweep_up

# downsampling
y_down = signal.resample_poly(y, 1, upsamplefactor)

# spectrogram
f, t, Sxx = signal.spectrogram(y_down, fs, nperseg=1024)
fig, ax = plt.subplots()
ax.pcolormesh(t, f, 10*np.log10(Sxx))
ax.set_ylabel('Frequency [Hz]')
ax.set_xlabel('Time [sec]')
plt.show()
