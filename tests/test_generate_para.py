import ising2D

initial_lattice = ising2D.generate_random_lattice(16, 16)

figtext = 'Nikhil Kumar'
para = ising2D.plot_lattice_evolution(initial_lattice, 10, J=1, step_increment=100, title=f'Above critical temperature (paramagnetic)\nlattice.shape={initial_lattice.shape}, kT=1\nstep_increment=100', figtext=figtext)

print('Saving animation to para.mp4...')
para.save('para.mp4')
