# ising2D
A package to simulate the behaviour of an Ising model system. 
The Ising model is a model in statistical mechanics used to describe the behaviour of a magnetic system.
The system is modelled as a matrix/lattice of +1 and -1 spins.

The energy of the system is given by 
$H = - J \sum{<i, j>}^{} J_{ij} \sigma_{{i} \sigma_{j}$
On each iteration, a lattice site is randomly chosen.
The spin of this lattice site is then changed with a probability of $\exp(\frac{-\Delta E}{kT})$, 
where $\Delta E$ is the change in energy of the system on flipping the spin.
This is then repeated for several iterations.

Depending on J and whether the temperature is below or above the critical temperature,
the system exhibits:
* Ferromagnetic: For J > 0 and temperature below critical temperature
* Antiferromagnetic: For J < 0 and temperature below critical temperature
* Paramagnetic: For temperature above critical temperature
