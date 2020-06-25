import setuptools

setuptools.setup(
    name="ising2D",
    version="0.0.6",
    author="Nikhil Kumar",
    author_email="nikhilkmr300@gmail.com",
    description="A package to simulate the behaviour of an Ising model system.",
    long_description="Refer https://github.com/nikhilkmr300/ising2D/blob/master/README.md for description.",
    url="https://github.com/nikhilkmr300/ising2D",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
      'numpy>=1.18',
      'matplotlib>=3.2',
      'tqdm>=4.46'
    ],
    python_requires='>=3.6',
)
