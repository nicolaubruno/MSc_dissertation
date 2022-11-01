# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Set plot
plt.clf()
plt.rcParams.update({"font.size":16})
plt.style.use('seaborn-whitegrid')
lines = ["solid", "dashed", "dotted", "dashdot", (0, (1, 5))]

# Domain
t = np.linspace(0, 8, 1000) * np.pi # 1 / Omega

# Looping in detuning (delta [Omega])
for i, gamma in enumerate([1/10, 1/2, 1, 2]):
	p_s = (gamma/2)**2 / (1/2 + (gamma/2)**2)
	omega_gamma = np.sqrt(1 - (gamma/4)**2)
	p = np.exp(-3 * gamma * t / 4) * (1 - p_s) * (np.cos(omega_gamma * t) + ((3*gamma)/(4*omega_gamma))*np.sin(omega_gamma * t)) + p_s
	p_2 = (1 - p) / 2

	if gamma == 0: label = r"$\Gamma = 0$"
	elif gamma == 1: label = r"$\Gamma = \Omega$"
	elif abs((int(gamma) - gamma)) > 0: label = (r"$\Gamma = %.1f \Omega$" % gamma)
	else: label = (r"$\Gamma = %d \Omega$" % gamma)

	plt.plot(t, p_2, linewidth = 2, linestyle = lines[i], color="black", label=label, marker="")

plt.xlabel(r"$ \Omega t $")
plt.ylabel(r"$\rho_{2,2}$")

# x-ticks
arr_xticks = []

for i in range(int(max(t)/np.pi) + 1):
	if i == 0:
		arr_xticks.append("0")

	elif i == 1:
		arr_xticks.append(r"$\pi$")

	else:
		arr_xticks.append(r"$%d\pi$" % i)

plt.xticks(np.linspace(min(t), max(t), len(arr_xticks)), arr_xticks)

plt.legend(frameon=True)
plt.grid(linestyle="--")
plt.tight_layout()
plt.show()
