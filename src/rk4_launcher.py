#! /usr/bin/env python3
#

# Global imports 
import pandas as pd
import numpy as np
import argparse

# rk4 imports
import rk4_lib.rk4_API as rk4API
import rk4_lib.rk4 as rk4

# Dask imports
import dask.dataframe as dd
import dask.array as da
from dask_jobqueue import PBSCluster
from dask.distributed import Client, LocalCluster


# Dummy function
def my_costly_simulation(line):
    import time
    import random
    print(line.compute()[0])
    return sum(line)

# Launch rk4_API for each object (aka line or Rk4Data)
def launch_rk4_API(line):
  # Get The array inside the Dask array line
  npArray = line.compute()
  # Launch with each elt of the array, rk4_API
  u0 = rk4API.rk4_API(npArray[0], npArray[1], npArray[2], npArray[3], npArray[4], npArray[5])
  # Copy elts into res
  res = npArray.copy() 
  # Update x1 and v1 into res
  res[2] = u0[0]
  res[3] = u0[1]
  # Return a dask array
  return da.from_array(res)



# Main
if ( __name__ == '__main__' ):
  
  # Check arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("input_file", help="input file for the RK4 processings")
  parser.add_argument("output_file", help="output file for the RK4 processings")
  parser.add_argument("-mode", "--mode", dest="cluster_mode", nargs="+", action="store",
                      help=""""Define cluster mode, ex: -mode cluster""", default="local")
  args = parser.parse_args()
  print(args.input_file)
  print(args.output_file)

  ########################### Dask Cluster ###############################
  cluster = None
  if args.cluster_mode == "cluster" :
    cluster = PBSCluster(processes=1, cores=4, memory="20GB", local_directory='$TMPDIR',
                         project='DaskTest', walltime='01:00:00', interface='ib0')

    
    cluster.scale(8)
  else :
    print("Local mode")
    cluster = LocalCluster()

    cluster.scale(2)
    
  client = Client(cluster)
  print(client)
  
  ########################### Read Input File ###########################
  # Create a Dask DataFrame from input_file
  # 6 colunms defined : Id t0 x0 v0 tmax and dt
  df_in = dd.read_csv(args.input_file, sep=" ", names=['Id', 't0', 'x0', 'v0' ,'tmax', 'dt'])
  
  # df.to_dask_array(lengths=True)) to compute chunk sizes. Otherwise df.values has a
  # shape = (nan,6) 
  print(df_in.to_dask_array(lengths=True))
  # shape_in = (nbLine_into_File, nbColunm=6)
  shape_in = df_in.to_dask_array(lengths=True).shape
  
  ############################ Processing ###############################
  # Distribution of each line to launch_rk4_API function on Dask client
  futures = client.map(launch_rk4_API, df_in.to_dask_array(lengths=True))

  # Block until result, and add the column to initial input tables
  results = client.gather(futures) # result is a list of dask array

  ########################### Write Output File ###########################
  # Create a dask array from results
  data = [results[i] for i in range(len(results))]
  da_output = da.concatenate(data, axis=0)
  da_output = da_output.reshape(shape_in)

  # Convert to dataFrame
  df_out = dd.from_dask_array(da_output)
  # Write into output_file
  dd.to_csv(df_out, args.output_file, single_file = True, sep = " ", index=False, header=False)
