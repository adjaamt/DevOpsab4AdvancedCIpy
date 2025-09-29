"""
setup script for the Python CI project.
"""

from setuptools import setup, find_packages

setup(
    name="simple-calculator",
    version="0.1.0",
    description="A simple calculator for CI demo",
    packages=find_packages(),
    python_requires=">=3.8",
)
