import ising2D

figtext = 'Nikhil Kumar'
ferro = ising2D.plot_lattice_evolution(initial_lattice, 1, J=1, step_increment=100, title=f'Below critical temperature, J=1 (ferromagnetic)\nlattice.shape={initial_lattice.shape}, kT=1\nstep_increment=100', figtext=figtext)

print('Saving animation to ferro.mp4...')
ferro.save('ferro.mp4')
