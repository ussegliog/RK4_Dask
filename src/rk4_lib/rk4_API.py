#! /usr/bin/env python3
#

import rk4_lib.rk4 as rk4
import numpy as np
import platform

def rk4_API (ind, t0, x0, v0, tmax, dt):

    #*****************************************************************************80
    #
    # RK4_API launchs the RK4 routine for a vector ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #


    #print ( '' )
    #print ( 'RK4_API' )
    #print ( '  Python version: %s' % ( platform.python_version ( ) ) )
    #print ( '  RK4API takes one Runge-Kutta step for a vector ODE.' )

    n = 2


    #print ( '' )
    #print ( '          T          U1(T)            U2(T)' )
    #print ( '' )


    i = 0

    u0 = np.zeros ( 2 )
    u0[0] = x0
    u0[1] = v0

    while ( True ):
      #
      #  Print (T0,U0).
      #
      #print ( '  %4d  %14.6g  %14.6g  %14.6g' % ( i, t0, u0[0], u0[1] ) )
      #
      #  Stop if we've exceeded TMAX.
      #
      if ( tmax <= t0 ):
        break

      i = i + 1
      #
      #  Otherwise, advance to time T1, and have RK4 estimate
      #  the solution U1 there.
      #
      t1 = t0 + dt
      u1 = rk4.rk4vec ( t0, n, u0, dt, rk4_f )
      #
      #  Shift the data to prepare for another step.
      #
      t0 = t1
      u0 = u1.copy ( )
      #
      #  Terminate.
      #
      #print ( '' )
      #print ( 'RK4VEC_TEST:' )
      #print ( '  Normal end of execution.' )
    return u0

def rk4_f ( t, n, u ):

    #*****************************************************************************80
    #
    ## RK4VEC_TEST_F evaluates the right hand side of a particular ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T, the current time.
    #
    #    Input, real U(N), the current solution value.
    #
    #    Output, real VALUE, the value of the derivative, dU/dT.
    #
    import numpy as np

    value = np.array ( [ u[1], - u[0] ] )

    return value
