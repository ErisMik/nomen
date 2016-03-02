"""
This is the Setup file for the Cython stuff
Run with: python setup.py build_ext --inplace
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["library/*.pyx", "plugins/*.pyx"]))
