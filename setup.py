from setuptools import setup, find_packages

setup(
    name="causal_env",
    version="0.1.0",
    description="A Python package for causal environment simulations.",
    author="Tyler",
    author_email="tyler.bonnell@gmail.com",
    url="https://github.com/tbonne/causal_env",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "networkx"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
