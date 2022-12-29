#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import glob

# with open('README.rst') as readme_file:
#     readme = readme_file.read()

# with open('HISTORY.rst') as history_file:
#     history = history_file.read()

scripts = glob.glob('bin/*')

requirements = ['numpy', 'scipy','astropy', 'fitsio', 'numba', 'mpi4py', 'setuptools']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Andrei Cuceu",
    author_email='andreicuceu@gmail.com',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    description=("Package for computing 2-point statistics "
                 "of the Lyman-alpha forest and related tracers."),
    install_requires=requirements,
    license="GNU General Public License v3.0",
    # long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='lya2pt',
    name='lya2pt',
    packages=find_packages(include=['lya2pt', 'lya2pt.*']),
    setup_requires=setup_requirements,
    scripts=scripts,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/andreicuceu/lya2pt',
    version='0.1.0',
    zip_safe=False,
)
