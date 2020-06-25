# ising2D
A package to simulate the behaviour of an Ising model system. 
The Ising model is a model in statistical mechanics used to describe the behaviour of a magnetic system.
The system is modelled as a matrix/lattice of +1 and -1 spins.

The energy of the system is given by 
<img src="/tex/9e46b9fae7622a77b0e8a0c6c7957d5b.svg?invert_in_darkmode&sanitize=true" align=middle width=187.10811734999996pt height=24.657735299999988pt/>
On each iteration, a lattice site is randomly chosen.
The spin of this lattice site is then changed with a probability of <img src="/tex/2756e01d0c990457ca6dacc33d8ce90b.svg?invert_in_darkmode&sanitize=true" align=middle width=73.2011082pt height=28.670654099999997pt/>, 
where <img src="/tex/8b315c12c08fd5b9b3d2a80e5db71bb5.svg?invert_in_darkmode&sanitize=true" align=middle width=26.780867849999986pt height=22.465723500000017pt/> is the change in energy of the system on flipping the spin.
This is then repeated for several iterations.

Depending on J and whether the temperature is below or above the critical temperature,
the system exhibits:
* Ferromagnetic: For J > 0 and temperature below critical temperature
* Antiferromagnetic: For J < 0 and temperature below critical temperature
* Paramagnetic: For temperature above critical temperature
