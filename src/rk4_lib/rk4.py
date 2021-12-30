#! /usr/bin/env python3
#

def rk4 ( t0, u0, dt, f ):

    #*****************************************************************************80
    #
    ## RK4 takes one Runge-Kutta step.
    #
    #  Discussion:
    #
    #    It is assumed that an initial value problem, of the form
    #
    #      du/dt = f ( t, u )
    #      u(t0) = u0
    #
    #    is being solved.
    #
    #    If the user can supply current values of t, u, a stepsize dt, and a
    #    function to evaluate the derivative, this function can compute the
    #    fourth-order Runge Kutta estimate to the solution at time t+dt.
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
    #    Input, real T0, the current time.
    #
    #    Input, real U0, the solution estimate at the current time.
    #
    #    Input, real DT, the time step.
    #
    #    Input, function value = F ( T, U ), a function which evaluates
    #    the derivative, or right hand side of the problem.
    #
    #    Output, real U1, the fourth-order Runge-Kutta solution estimate
    #    at time T0+DT.
    #

  #
    #  Get four sample values of the derivative.
    #
    f1 = f ( t0,            u0 )
    f2 = f ( t0 + dt / 2.0, u0 + dt * f1 / 2.0 )
    f3 = f ( t0 + dt / 2.0, u0 + dt * f2 / 2.0 )
    f4 = f ( t0 + dt,       u0 + dt * f3 )
    #
    #  Combine them to estimate the solution U1 at time T1 = T0 + DT.
    #
    u1 = u0 + dt * ( f1 + 2.0 * f2 + 2.0 * f3 + f4 ) / 6.0

    return u1


def rk4vec ( t0, m, u0, dt, f ):

    #*****************************************************************************80
    #
    ## RK4VEC takes one Runge-Kutta step for a vector ODE.
    #
    #  Discussion:
    #
    #    Thanks  to Dante Bolatti for correcting the final function call to:
    #      call f ( t1, m, u3, f3 )
    #    18 August 2016.
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
    #    Input, real T0, the current time.
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, real U0(M), the solution estimate at the current time.
    #
    #    Input, real DT, the time step.
    #
    #    Input, function uprime = F ( t, m, u  )
    #    which evaluates the derivative UPRIME(1:M) given the time T and
    #    solution vector U(1:M).
    #
    #    Output, real U(M), the fourth-order Runge-Kutta solution
    #    estimate at time T0+DT.
    #
    import numpy as np
    #
    #  Get four sample values of the derivative.
    #
    f0 = f ( t0, m, u0 )

    t1 = t0 + dt / 2.0
    u1 = np.zeros ( m )
    u1[0:m] = u0[0:m] + dt * f0[0:m] / 2.0
    f1 = f ( t1, m, u1 )

    t2 = t0 + dt / 2.0
    u2 = np.zeros ( m )
    u2[0:m] = u0[0:m] + dt * f1[0:m] / 2.0
    f2 = f ( t2, m, u2 )

    t3 = t0 + dt
    u3 = np.zeros ( m )
    u3[0:m] = u0[0:m] + dt * f2[0:m]
    f3 = f ( t3, m, u3 )
    #
    #  Combine them to estimate the solution U at time T1.
    #
    u = np.zeros ( m )
    u[0:m] = u0[0:m] + ( dt / 6.0 ) * ( \
                                        f0[0:m] \
                                        + 2.0 * f1[0:m] \
                                        + 2.0 * f2[0:m] \
                                        +       f3[0:m] )

    return u


def timestamp ( ):

    #*****************************************************************************80
    #
    ## TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import time

    t = time.time ( )
    print ( time.ctime ( t ) )

    return None
