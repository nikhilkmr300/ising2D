# ising2D
A package to simulate the behaviour of an Ising model system. 
The Ising model is a model in statistical mechanics used to describe the behaviour of a magnetic system.
The system is modelled as a matrix/lattice of +1 and -1 spins.

The energy of the system is given by 
<img src="/tex/2952095dffb5082a65347403fb15d457.svg?invert_in_darkmode&sanitize=true" align=middle width=159.61948859999998pt height=24.657735299999988pt/>
where J represents the interaction strength between spins,
<img src="/tex/f29c574505eea1cddce4335737b3cad0.svg?invert_in_darkmode&sanitize=true" align=middle width=100.71062924999998pt height=24.65753399999998pt/> is the spin of the <img src="/tex/3def24cf259215eefdd43e76525fb473.svg?invert_in_darkmode&sanitize=true" align=middle width=18.32504519999999pt height=27.91243950000002pt/> lattice point.
<img src="/tex/7409d8ab6a0b37fe9d5c8ce22df9aba8.svg?invert_in_darkmode&sanitize=true" align=middle width=55.38259154999999pt height=21.68300969999999pt/> indicates that the summation is performed over the 4 nearest neighbours (i.e., the von Neumann neighbourhood).

On each iteration, a lattice site is randomly chosen.
The spin of this lattice site is then changed with a probability of <img src="/tex/2756e01d0c990457ca6dacc33d8ce90b.svg?invert_in_darkmode&sanitize=true" align=middle width=73.2011082pt height=28.670654099999997pt/>, 
where <img src="/tex/8b315c12c08fd5b9b3d2a80e5db71bb5.svg?invert_in_darkmode&sanitize=true" align=middle width=26.780867849999986pt height=22.465723500000017pt/> is the change in energy of the system on flipping the spin.
This is then repeated for several iterations.

Depending on J and whether the temperature is below or above the critical temperature,
the system exhibits:
* Ferromagnetic: For J > 0 and temperature below critical temperature
* Antiferromagnetic: For J < 0 and temperature below critical temperature
* Paramagnetic: For temperature above critical temperature

# Installation
Install `pip` if you do not have it already. Refer https://pip.pypa.io/en/stable/installing/.
Use the command `pip install ising2D` to install the package.

# Description of functions
Here is a description of the functions that you might want to use in your code:
* plot_magnetization_vs_T: Generates a plot of final magnetization vs temperature for a lattice initalized as initial_lattice. Final magnetization is the magnetization of the lattice after num_steps steps of the MCM algorithm.
* run_metropolis: Runs num_steps number of steps of the Monte Carlo Metropolis (MCM) algorithm.
* generate_lattice_evolution: Takes num_steps number of steps of the Monte-Carlo metropolis (MCM) algorithm.
* plot_lattice_evolution: Generates an animation of the evolution of the lattice through the MCM algorithm.

The tests directory in this repository contains some code you might find useful in understanding how to use this package.
