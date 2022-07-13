from setuptools import setup, find_packages

setup(
    name='Monte-Carlo-Simulator',
    version='1.0.0',
    url='https://github.com/dvnmc/Monte-Carlo-Simulator.git',
    author='Devin McDonald',
    author_email='djm6cz@virginia.edu',
    description='Monte Carlo Simulator Package (Final Project)',
    packages=find_packages(),    
    install_requires=['numpy', 'pandas'],
)

