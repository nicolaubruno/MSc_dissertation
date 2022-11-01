# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Set plot
plt.clf()
plt.rcParams.update({"font.size":16})
plt.style.use('seaborn-whitegrid')
lines = ["solid", "dashed", "dotted"]

# Domain
t = np.linspace(0, 4, 1000) * np.pi # 1 / Omega

# Looping in detuning (delta [Omega])
for i, delta in enumerate([0, 1, 2]):
	G = np.sqrt(1 + delta**2) # Omega
	P = 1 / (2*G**2) * (1 - np.cos(G*t))

	if delta == 0: label = r"$\Delta = 0$"
	elif delta == 1: label = r"$\Delta = \Omega$"
	else: label = (r"$\Delta = %d \Omega$" % delta)

	plt.plot(t, P, linewidth = 2, linestyle = lines[i], color="black", label=label, marker="")

plt.xlabel(r"$ \Omega t $")
plt.ylabel(r"$\rho_{2,2}$")

# x-ticks
arr_xticks = []

for i in range(int(2*max(t)/np.pi) + 1):
	if i == 0:
		arr_xticks.append("0")

	elif i == 1:
		arr_xticks.append(r"$\pi/2$")

	elif i == 2:
		arr_xticks.append(r"$\pi$")

	elif i % 2 == 0:
		arr_xticks.append(r"$%d\pi$" % (i / 2))

	else:
		arr_xticks.append(r"$%d\pi/2$" % i)

plt.xticks(np.linspace(min(t), max(t), len(arr_xticks)), arr_xticks)

plt.legend(frameon=True)
plt.grid(linestyle="--")
plt.tight_layout()
plt.show()
