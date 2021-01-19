import numpy as np
import xarray as xr
from netCDF4 import Dataset
from matplotlib import pylab
from pylab import *
import csv

nc_file = ("/nird/projects/NS9001K/sso102/S2S/DATA/S2S_SST/sst_CY46R1_2019-07-01_cf_forecast_BERGEN.nc")
#d = xr.DataArray(data.variables['sst'])
f = Dataset(nc_file, mode='r')
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
sst = f.variables['sst'][:]
time = f.variables['time'][:]


#print(d[:,21,68])
#print(f.shape)
print(lon.shape)

#data = xr.open_dataset("/home/python/PBLH_Exp_08_jul_2006.nc")
#d = xr.DataArray(data.variables['PBLH'])
#print(d[:,21,68])

#df = d[:,21,68]
with open ('output.txt','w') as fout:
    writer = csv.writer(fout)
    writer.writerows(sst)  
    writer.writerows(sst)  
