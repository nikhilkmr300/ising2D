import ising2D

initial_lattice = ising2D.generate_random_lattice(16, 16)

figtext = 'Nikhil Kumar'
antiferro = ising2D.plot_lattice_evolution(initial_lattice, 1, J=-1, num_steps=100000, step_increment=10, title=f'Below critical temperature, J=-1 (antiferromagnetic)\nlattice.shape={initial_lattice.shape}, kT=1\nstep_increment=10', figtext=figtext)

print('Saving animation to antiferro.mp4...')
antiferro.save('antiferro.mp4')
