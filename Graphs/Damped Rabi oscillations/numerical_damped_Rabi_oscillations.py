# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Setting parameters
Delta = 0 # Gamma
Omega = 1 # Gamma

# Operator matrix
# ---
M = np.zeros((3,3))

# Diagonal terms
M[0][0] = -1/2
M[1][1] = -1/2
M[2][2] = -1
# ---

# Generate data for different detunings
num_Deltas = 100
all_Deltas = np.linspace(-50, 50, num_Deltas)
all_Omegas = [1, 2, 5, 10]
num_Omegas = len(all_Omegas)

m = [[] for i in range(num_Omegas)]
for j in range(num_Omegas):
	for i in range(3):
		m[j].append(np.zeros(num_Deltas, dtype=complex))
	
	m[j] = np.array(m[j], dtype=complex)
m = np.array(m)

for i, Delta in enumerate(all_Deltas):
	for j, Omega in enumerate(all_Omegas):
		# Set off-diagonal terms
		M[0][1] = - Delta
		M[1][0] = Delta
		M[1][2] = - Omega
		M[2][1] = Omega

		# Eigenvalues
		# ---
		mi = np.linalg.eig(M)[0]

		# Real value
		if abs(mi[0].imag) <= abs(mi[1].imag) and abs(mi[0].imag) <= abs(mi[2].imag):
			m[j][0][i] = abs(mi[0].real)
			m[j][1][i] = abs(mi[1].real)
			m[j][2][i] = abs(mi[1].imag)

		elif abs(mi[1].imag) <= abs(mi[0].imag) and abs(mi[1].imag) <= abs(mi[2].imag):
			m[j][0][i] = abs(mi[1].real)
			m[j][1][i] = abs(mi[0].real)
			m[j][2][i] = abs(mi[0].imag)

		elif abs(mi[2].imag) <= abs(mi[0].imag) and abs(mi[2].imag) <= abs(mi[1].imag):
			m[j][0][i] = abs(mi[2].real)
			m[j][1][i] = abs(mi[0].real)
			m[j][2][i] = abs(mi[0].imag)
		# ---

# Plot graph
plt.clf()
plt.style.use('seaborn-whitegrid')
plt.rcParams.update({"font.size":16})
plt.style.use('seaborn-whitegrid')

markers = ["o", "^", "square"]
titles = ["Damping coefficient a", "Damping coefficient b", "Frequency c"]
x_labels = ["a", "b", "c"]
lines = ["solid", "dashed", "dotted", "dashdot", (0, (1, 5))]
i = 2 # Set plot

for j, Omega in enumerate(all_Omegas):
	if Omega == 0:
		label = r"$|\Omega| = 0$"

	elif Omega == 1:
		label = r"$|\Omega| = \Gamma$"

	else:
		label = (r"$|\Omega| = %d\Gamma$" % Omega)

	plt.plot(all_Deltas, m[j][i], label=label, color="black", linestyle=lines[j], linewidth=2, marker="")

plt.xlabel(r"$\Delta [\Gamma]$")
plt.ylabel(x_labels[i] + r" $[\Gamma]$")
plt.legend(frameon=True)
plt.grid(linestyle="--")

plt.tight_layout()
plt.show()