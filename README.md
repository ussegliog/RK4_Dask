# RK4_Dask

Example of Dask application for a runge kutta estimation 

This code uses a RK4 implementation (from https://people.sc.fsu.edu/~jburkardt/py_src/rk4/rk4.html) to approximate a ODE calculation.

## Requirements

This code needs an installation of Python with Dask module (at least 2.0.x).

## Input/Output

Two files are used as input and output. Each files are in txt format and contains for each line data/objet named RK4Data. A RK4Data is composed of :
* An id
* An array with 5 values : intial_time, x0 (position), v0 (velocity), last_time, time_step

At the end of the execution, an output file is created with the same shape and updates the values for position and velocity estimated at the last_time.


## Execution

To launch this application, do :

python src/rk4_launcher.py <input.txt> <output.txt>

Another argument is available : mode. Two modes are possible with local or cluster (PBScluster).
