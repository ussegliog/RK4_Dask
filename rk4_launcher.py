#! /usr/bin/env python3
#

import rk4_lib.rk4_API as rk4API
import rk4_lib.rk4 as rk4
import numpy as np

if ( __name__ == '__main__' ):
  rk4.timestamp ( )
  # Define main parameters
  dt = 0.1
  tmax = 12.0 * np.pi
  t0 = 0.0
  x0 = 0.0
  v0 = 1.0
  ind = 0

  u0 = np.zeros ( 2 )
  
  u0 = rk4API.rk4_API(ind, t0, x0, v0, tmax, dt)

  print(u0)
  
  rk4.timestamp ( )

