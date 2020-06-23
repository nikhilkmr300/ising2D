import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm

def generate_random_lattice(length, width):
    """
    Generates a random lattice.

    Parameters:
    length (int): Number of rows in lattice
    width (int): Number of columns in lattice

    Returns:
    NumPy ndarray: Lattice of randomly generated spins (+1 or -1) of shape
        (length, width)
    """

    return np.random.choice([-1, 1], size=(length, width))

def plot_lattice(lattice, title='', xlabel='x', ylabel='y', figtext=''):
    """
    Plots lattice at a particular configuration. Spin +1 is displayed in white,
    spin -1 is displayed in black.

    Parameters:
    lattice (array_like): Lattice to be plotted
    title (string): Title for plot, optional
    xlabel (string): Label for x-axis, optional
    ylabel (string): Label for y-axis, optional
    figtext (string): Figure text, optional

    Returns:
    None

    Notes:
    Use plt.figure() before calling this function if you would like to plot on a new figure.
    """

    lattice = np.array(lattice)
    # +1 spin is displayed in white, -1 spin is displayed in black
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.figtext(0.5, 0.02, figtext, ha='center')
    plt.imshow(lattice, cmap='gray')
    plt.show()

def generate_lattice_evolution(initial_lattice, T, J=1, k=1, num_steps=100000):
    """
    Takes num_steps number of steps of the Monte-Carlo metropolis (MCM)
    algorithm.

    Parameters:
    inital_lattice (array_like): Inital lattice before running the MCM algorithm
    T (float): Temperature
    J (float): Strength of interaction, optional
    k (float): Boltzmann constant, taken as 1 by default for simplicity,
        optional
    num_steps (int): Number of steps to take of the MCM algorithm, optional

    Returns:
    list: List of arrays at all steps of the MCM algorithm, length num_steps
    """

    initial_lattice = np.array(initial_lattice)
    print(f'Generating lattice evolution of initial_lattice [lattice.shape={initial_lattice.shape}, T={round(T, 2)}, J={round(J, 2)}, k={round(k, 2)}, num_steps={num_steps}]...')
    lattice = initial_lattice.copy()    # Initializing the lattice using inital_lattice
    lattice_evolution = [initial_lattice]   # List to store the lattice at each step of the MCM algorithm

    for i in tqdm(range(num_steps)):
        # Taking a step of the MCM algorithm
        lattice = take_step(lattice, T, J=J, k=k)
        # Appending the current lattice to the list lattice_evolution
        lattice_evolution.append(lattice.copy())

    return lattice_evolution

def plot_lattice_evolution(initial_lattice, T, J=1, k=1, num_steps=100000, repeat_delay=3000, step_increment=1, title='', figtext=''):
    """
    Generates an animation of the evolution of the lattice through the MCM
    algorithm.

    Parameters:
    lattice (array_like): Lattice for which step of MCM algorithm is to be taken
    T (float): Temperature
    J (float): Strength of interaction, optional
    k (float): Boltzmann constant, taken as 1 by default for simplicity,
        optional
    num_steps (int): Number of steps to take of the MCM algorithm, optional
    repeat_delay (int): Time in milliseconds before repeating the animation
        playback, optional
    step_increment (int): Number of steps incremented between each frame of the
        animation, optional
    title (string): Title for plot, optional

    Returns:
    matplotlib.ArtistAnimation object

    Notes:
    Keeping step_increment=1 will plot all of the lattices generated during the
    evolution until convergence/num_steps (whichever is less), and may take some
    time to run, especially if num_steps is large. It makes sense to skip
    animating some of the steps of the MCM algorithm.
    """

    print(f'Plotting lattice evolution of inital_lattice [lattice.shape={initial_lattice.shape}, T={round(T, 2)}, J={round(J, 2)}, k={round(k, 2)}, num_steps={num_steps}]...')
    lattice_evolution = generate_lattice_evolution(initial_lattice, T, J=J, k=k, num_steps=num_steps)
    images = []
    for i in range(0, len(lattice_evolution), step_increment):
        image = plt.imshow(lattice_evolution[i], cmap='gray')
        images.append([image])
        # If all spins are aligned for J > 0 (ferromagnetic), break out of loop
        if(J > 0 and (np.sum(lattice_evolution[i]) == initial_lattice.shape[0]**2 or np.sum(lattice_evolution[i]) == -initial_lattice.shape[0]**2)):
            break
        # If all spins are opposite aligned for J < 0 (antiferromagnetic), break out of loop
        if(J < 0 and np.sum(lattice_evolution[i]) == 0):
            break

    fig = plt.figure(1)
    plt.title(title)
    plt.figtext(0.5, 0.02, figtext, ha='center')
    evolution_animation = animation.ArtistAnimation(fig, images, blit=True, repeat_delay=3000)
    plt.show()

    return evolution_animation

def take_step(lattice, T, J=1, k=1):
    """
    Takes a step of the Monte Carlo Metropolis algorithm.
    Spin at random index flips with probability exp(-delta_E / (k * T)) if
    delta_E > 0.
    If delta_E < 0, spin always flips.

    Parameters:
    lattice (array_like): Lattice for which step of MCM algorithm is to be taken
    T (float): Temperature
    J (float): Strength of interaction, optional
    k (float): Boltzmann constant, taken as 1 by default for simplicity,
        optional

    Returns:
    NumPy ndarray: Lattice after running the MCM algorithm for 1 step
    """

    lattice = np.array(lattice)
    (length, width) = lattice.shape
    i, j = np.random.randint(0, length), np.random.randint(0, width)

    delta_E = 2 * J * lattice[i, j] * (lattice[(i-1)%length,j] + lattice[(i+1)%length,j] + lattice[i,(j-1)%width] + lattice[i,(j+1)%width])

    if(np.random.rand() < 1 / (1 + np.exp(delta_E / (k * T)))):
        lattice[i, j] = -lattice[i, j]

    return lattice

def run_metropolis(lattice, T, num_steps=100000, J=1, k=1):
    """
    Runs num_steps number of steps of the Monte Carlo Metropolis (MCM)
        algorithm.

    Parameters:
    lattice (array_like): Lattice for which step of MCM algorithm is to be taken
    T (float): Temperature
    J (float): Strength of interaction, optional
    k (float): Boltzmann constant, taken as 1 by default for simplicity,
        optional
    num_steps (int): Number of steps to take of the MCM algorithm, optional

    Returns:
    NumPy ndarray: Lattice after running the MCM algorithm for num_steps number
        of steps
    """

    print(f'Running metropolis algorithm on lattice [lattice.shape={lattice.shape}, T={round(T, 2)}, J={round(J, 2)}, k={round(k, 2)}, num_steps={num_steps}]...')
    for i in tqdm(range(num_steps)):
        lattice = take_step(lattice, T, J=J, k=k)
    return lattice

def calculate_magnetization(lattice):
    """
    Calculates magnetization of lattice.

    Parameters:
    lattice (array_like): Lattice for which magnetization is to be calculated

    Returns:
    float: Magnetization of the lattice

    Notes:
    Magnetization is calculated as sum of spins divided by the number of lattice points.
    """
    return np.abs(np.sum(lattice) / (lattice.shape[0] * lattice.shape[1]))

def plot_magnetization_vs_T(initial_lattice, low, high, num, length=16, width=16, num_steps=100000, J=1, k=1, marker='s', color='blue', xlabel='Temperature', ylabel='Magnetization', title='', figtext=''):
    """
    Generates a plot of final magnetization vs temperature for a lattice
    initalized as initial_lattice.
    Final magnetization is the magnetization of the lattice after num_steps
    steps of the MCM algorithm.

    Parameters:
    inital_lattice (array_like): Inital lattice before running the MCM algorithm
    low (float): Lower bound on temperature)
    high (float): Upper bound on temperature
    num (int): Number of temperature points to consider for plotting
    length (int): Number of rows in lattice, optional
    width (int): Number of columns in lattice, optional
    num_steps (int): Number of steps to be taken by the MCM algorithm for each
        value of temperature, optional
    J (float): Strength of interaction, optional
    k (float): Boltzmann constant, taken as 1 by default for simplicity,
        optional
    marker (string): Marker to use by matplotlib.pyplot.plot
    color (string): Colour of plotted points to use by matplotlib.pyplot.plot
    xlabel (string): Label for x-axis, optional
    ylabel (string): Label for y-axis, optional
    title (string): Title for plot, optional
    figtext (string): Figure text, optional

    Returns:
    tuple: Tuple containing the array temperatures and the magnetizations at
        those temperatures

    Notes:
    Use plt.figure() before calling this function if you would like to plot on a
    new figure.
    """

    print(f'Plotting final magnetization of inital_lattice after {num_steps} steps, for {num} temperature values in the range {low} to {high}...\n')

    temperatures = np.linspace(low, high, num)
    magnetizations = np.empty(len(temperatures))

    # Running MCM on initial_lattice, and calculating magnetization after num_steps steps, for each temperature
    for i, T in enumerate(temperatures):
        lattice = initial_lattice
        lattice = run_metropolis(lattice, T, num_steps)
        magnetizations[i] = calculate_magnetization(lattice)

    plt.figure()
    plt.scatter(temperatures, magnetizations, marker=marker, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.figtext(0.5, 0.02, figtext, ha='center')
    plt.show()

    return (temperatures, magnetizations)

if __name__ == '__main__':
    initial_lattice = generate_random_lattice(16, 16)
    plot_magnetization_vs_T(initial_lattice, 0, 5, 100, length=16, width=16, num_steps=1000000, marker='s', color='blue')

    """
    figtext = 'Nikhil Kumar'
    ferro = plot_lattice_evolution(initial_lattice, 1, J=1, step_increment=100, title=f'Below critical temperature, J=1 (ferromagnetic)\nlattice.shape={initial_lattice.shape}, kT=1\nstep_increment=100', figtext=figtext)
    antiferro = plot_lattice_evolution(initial_lattice, 1, J=-1, num_steps=100000, step_increment=10, title=f'Below critical temperature, J=-1 (antiferromagnetic)\nlattice.shape={initial_lattice.shape}, kT=10\nstep_increment=10', figtext=figtext)
    para = plot_lattice_evolution(initial_lattice, 10, J=1, step_increment=100, title=f'Above critical temperature (paramagnetic)\nlattice.shape={initial_lattice.shape}, kT=1\nstep_increment=100', figtext=figtext)

    print('Saving animations...')
    ferro.save('ferro_animation.mp4')
    antiferro.save('antiferro_animation.mp4')
    para.save('para_animation.mp4')
    """
