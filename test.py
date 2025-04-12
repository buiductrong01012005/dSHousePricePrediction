import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(-10, 10, 1000)
H_mag = np.abs(1j * w / ((1 - w**2) + 2j * w))
H_phase = np.angle(1j * w / ((1 - w**2) + 2j * w))

plt.figure(figsize=(12,5))

# Biên độ
plt.subplot(1, 2, 1)
plt.plot(w, H_mag)
plt.title('Biên độ |H(ω)|')
plt.xlabel('ω')
plt.ylabel('|H(ω)|')
plt.grid(True)

# Pha
plt.subplot(1, 2, 2)
plt.plot(w, H_phase)
plt.title('Pha ∠H(ω)')
plt.xlabel('ω')
plt.ylabel('Pha (rad)')
plt.grid(True)

plt.tight_layout()
plt.show()
