# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Set plot
plt.clf()
plt.rcParams.update({"font.size":16})
plt.style.use('seaborn-whitegrid')
lines = ["solid", "dashed", "dotted", "dashdot", (0, (1, 5))]
graph = 1

# Net absorption cross section
if graph == 1:
	# Domain
	delta = np.linspace(-2, 2, 1000) # 1 / Gamma

	for i, s0 in enumerate([0, 1, 5, 10]):
		# Population of the excited state
		sigma = 1 / (1 + s0 + (2*delta)**2)

		if (int(s0) - s0) == 0: label = r"$s_0 = %d$" % int(s0)
		else: label = r"$s_0 = %.1f$" % s0

		plt.plot(delta, sigma, label=label, color="black", marker="", linewidth=2, linestyle=lines[i])

	plt.xlabel(r"$\Delta [\Gamma]$")
	plt.ylabel(r"$\sigma_{abs} / \sigma_0 $")

# Absorption line shape
elif graph == 2:
	# Domain
	delta = np.linspace(-10, 10, 1000) # 1 / Gamma

	for i, s0 in enumerate([5, 10, 20, 40]):
		gamma_prime = np.sqrt(1 + s0)
		L_Gamma = (1 / (1 + (2*delta/gamma_prime)**2)) * 2 / (np.pi * gamma_prime**2)

		if (int(s0) - s0) == 0: label = r"$s_0 = %d$" % int(s0)
		else: label = r"$s_0 = %.1f$" % s0

		plt.plot(delta, L_Gamma, label=label, color="black", marker="", linewidth=2, linestyle=lines[i])

	plt.xlabel(r"$\Delta [\Gamma]$")
	plt.ylabel(r"$L(\Delta) \Gamma $")

plt.legend(frameon=True)
plt.grid(linestyle="--")
plt.tight_layout()
plt.show()
