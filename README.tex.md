# ising2D
A package to simulate the behaviour of an Ising model system. 
The Ising model is a model in statistical mechanics used to describe the behaviour of a magnetic system.
The system is modelled as a matrix/lattice of +1 and -1 spins.

The energy of the system is given by 
$$H = - \sum_{<i, j>}^{} J_{ij} \sigma_{i} \sigma_{j}$$
where J represents the interaction strength between spins,
$\sigma_{i} \in {-1, +1}$ is the spin of the $i^{th}$ lattice point.
$<i, j>$ indicates that the summation is performed over the 4 nearest neighbours (i.e., the von Neumann neighbourhood).

On each iteration, a lattice site is randomly chosen.
The spin of this lattice site is then changed with a probability of $\exp(\frac{-\Delta E}{kT})$, 
where $\Delta E$ is the change in energy of the system on flipping the spin.
This is then repeated for several iterations.

Depending on J and whether the temperature is below or above the critical temperature,
the system exhibits:
* Ferromagnetic: For J > 0 and temperature below critical temperature
* Antiferromagnetic: For J < 0 and temperature below critical temperature
* Paramagnetic: For temperature above critical temperature

# Installation
Install `code`pip`code` if you do not have it already. Refer https://pip.pypa.io/en/stable/installing/.
Use the command `code`pip install ising2D`code` to install the package.

# Description of functions
Here is a description of the functions that you might want to use in your code:
* plot_magnetization_vs_T: Generates a plot of final magnetization vs temperature for a lattice initalized as initial_lattice. Final magnetization is the magnetization of the lattice after num_steps steps of the MCM algorithm.
* run_metropolis: Runs num_steps number of steps of the Monte Carlo Metropolis (MCM) algorithm.
* generate_lattice_evolution: Takes num_steps number of steps of the Monte-Carlo metropolis (MCM) algorithm.
* plot_lattice_evolution: Generates an animation of the evolution of the lattice through the MCM algorithm.

The tests directory in this repository contains some code you might find useful in understanding how to use this package.
