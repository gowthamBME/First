import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
fs = 500
t = np.linspace(0, 1, fs, endpoint=False)
x = np.sin(2 * np.pi * 7 * t) + np.sin(2 * np.pi * 13 * t)
x += 0.5 * np.random.randn(t.size)
b, a = signal.butter(4, 10, fs=fs, btype='low')
y = signal.filtfilt(b, a, x)
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Noisy Signal')
plt.plot(t, y, label='Filtered Signal', linewidth=2)
plt.legend()
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Signal Filtering Example')
plt.show()