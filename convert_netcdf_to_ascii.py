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
print(time.shape)
print(sst.shape)
time2= np.squeeze(time)
print(time2)

#sst2 = sst.strip( ) 
print(sst)
#print(sst2)

for x in sst:
    for y in time:
        sst_new = str(x)[1:-1]
        sst_new=str(sst_new)[1:-1]
        #print(sst_new)
        column_test=x,y
        column_test=sst_new,y
       # print(sst_new,y)
        
print(column_test)   
#data = xr.open_dataset("/home/python/PBLH_Exp_08_jul_2006.nc")
#d = xr.DataArray(data.variables['PBLH'])
#print(d[:,21,68])

#df = d[:,21,68]
with open ('output.txt','w') as fout:
    writer = csv.writer(fout)
    writer.writerow(sst)  
    writer.writerow(time2)  

                  
with open('example1.csv', 'w') as result:
    writer = csv.writer(result, delimiter=",")
    writer.writerow(('SST', 'time'))
    columns = sst,time2
    writer.writerow(column_test)
