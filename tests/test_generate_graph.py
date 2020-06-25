import ising2D

initial_lattice = ising2D.generate_random_lattice(16, 16)
ising2D.plot_magnetization_vs_T(initial_lattice, 0, 5, 100, length=16, width=16, num_steps=1000000, marker='s', color='blue')
