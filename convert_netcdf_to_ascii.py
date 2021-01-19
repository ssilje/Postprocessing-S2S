import numpy as np
import xray as xr
from pylab import *
import csv

data = xr.open_dataset("/nird/projects/NS9001K/sso102/S2S/DATA/S2S_SST/sst_CY46R1_2019-07-01_pf_forecast_BERGEN.nc")
d = xr.DataArray(data.variables['sst'])
#print(d[:,21,68])
print(d.shape)

#data = xr.open_dataset("/home/python/PBLH_Exp_08_jul_2006.nc")
#d = xr.DataArray(data.variables['PBLH'])
#print(d[:,21,68])

#df = d[:,21,68]
#with open ('/home/python/output.txt','w') as fout:
#    writer = csv.writer(fout)
#    writer.writerows(df)  
