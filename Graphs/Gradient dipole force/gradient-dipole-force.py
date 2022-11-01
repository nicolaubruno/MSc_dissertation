# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Set plot
plt.clf()
plt.rcParams.update({"font.size":16})
plt.style.use('seaborn-whitegrid')
lines = ["solid", "dashed", "dotted", "dashdot", (0, (1, 5))]

# Domain
delta = np.linspace(-10, 10, 1000) # Gamma

# Looping in the saturation parameter
for i, s0 in enumerate([1, 5, 10, 20]):
	s = s0 / (1 + (2*delta)**2)
	U = (delta / 2) * np.log(1 + s)

	if s0 == 0: label = r"$s_0 = 0$"
	else: label = (r"$s_0 = %d$" % s0)

	plt.plot(delta, U, linewidth = 2, linestyle = lines[i], color="black", label=label, marker="")

plt.xlabel(r"$ \Delta[\Gamma] $")
plt.ylabel(r"$U_{dp} / (\hbar \Gamma)$")

plt.legend(frameon=True)
plt.grid(linestyle="--")
plt.tight_layout()
plt.show()
