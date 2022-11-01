# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Constant
mu_B = 927.4009994e-26 # J / T
hbar = 1.054571800e-34 # J s

# Atomic transition and Laser beam
s0 = 1
delta = -1 # Gamma 
Gamma = 2*np.pi * 30.5e6 # Hz
del_B = 10 * 1e-4 / (1e-2) # T / m
beta = ((del_B * mu_B) / (hbar * Gamma * 1e2)) # Gamma / cm
k = 2*np.pi / (461e-9) # 1 / m
g = 1
m = 88 * 1.660539040e-27 #kg

# MOT force
# ---
# Maximum force
F_max = hbar * k * Gamma / 2 # N

# Zeeman shift
z_prime = np.linspace(-3, 3, 1000) # Gamma
z_prime_2 = np.linspace(-1.5, 1.5, 1000) # Gamma
delta_Z = {i: -i * g * z_prime for i in [-1, 1]} # Gamma
omega_MOT_square = -(8 * g * hbar * k * s0 * delta * Gamma) / (F_max * (1 + s0 + 4*delta**2)**2)

# Doppler shift
v_prime = np.linspace(-3, 3, 1000) # Gamma
v_prime_2 = np.linspace(-1.5, 1.5, 1000) # Gamma
delta_D = {i: -i * v_prime for i in [-1, 1]} # Gamma
damping = -(8 * hbar * k * s0 * delta * Gamma) / (F_max * (1 + s0 + 4*delta**2)**2)

#
F_MOT_position = s0 * (1 / (1 + s0 + 4*(delta + delta_Z[+1])**2) - 1 / (1 + s0 + 4*(delta + delta_Z[-1])**2)) # F_max
F_MOT_velocity = s0 * (1 / (1 + s0 + 4*(delta + delta_D[+1])**2) - 1 / (1 + s0 + 4*(delta + delta_D[-1])**2)) # F_max
# ---

# Plot F_MOT
# ---
plt.clf()
plt.rcParams.update({"font.size":14, "figure.figsize":(7,6)})
plt.style.use('seaborn-whitegrid')

# Position
#
plt.plot(z_prime, F_MOT_position, linewidth=2, color="#888", label=r"$ F_{MOT}(z, 0)\ |\ F_{MOT}(0, v) $")
plt.plot(z_prime_2, - omega_MOT_square * z_prime_2, linewidth=2, linestyle="--", color="black", label=r"$ - m \omega_{MOT}^2 z\ |\ - m 2 \zeta \omega_{MOT} v $")

plt.xlabel(r"$ \beta z / \Gamma\ |\ k v / \Gamma $")
plt.ylabel(r"$ F_{MOT} / F_{max} $")

plt.legend(frameon=True)
plt.grid(linestyle="--")

plt.tight_layout()
plt.show()
# ---
