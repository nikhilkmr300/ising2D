# ising2D
A package to simulate the behaviour of an Ising model system. 
The Ising model is a model in statistical mechanics used to describe the behaviour of a magnetic system.
The system is modelled as a matrix/lattice of +1 and -1 spins.

The energy of the system is given by 
<img src="/tex/f3153da5e6e864e5a02757996f31be6f.svg?invert_in_darkmode&sanitize=true" align=middle width=817.6453593pt height=24.657735299999988pt/>\exp(\frac{-\Delta E}{kT})<img src="/tex/11ce50964722b0e6b2431b841856db2f.svg?invert_in_darkmode&sanitize=true" align=middle width=52.169074649999985pt height=22.831056599999986pt/>\Delta E$ is the change in energy of the system on flipping the spin.
This is then repeated for several iterations.

Depending on J and whether the temperature is below or above the critical temperature,
the system exhibits:
* Ferromagnetic: For J > 0 and temperature below critical temperature
* Antiferromagnetic: For J < 0 and temperature below critical temperature
* Paramagnetic: For temperature above critical temperature
