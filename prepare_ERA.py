import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.dates as mdates
import os,sys

DATABASE = '/nird/projects/NS9853K/DATA'
workdir = '/nird/projects/NS9001K/sso102/DATA/test'
var_long='sea_surface_temperature' 

# 10m_u_component_of_wind 2m_temperature sea_surface_temperature total_precipitation 10m_v_component_of_wind mean_sea_level_pressure snowfall

DATE = pd.date_range(start='1999-07-01', end='2020-07-01')

DATAERA = '%s/%s/'%(DATABASE,'SFE/ERA_daily_nc')


## Regrid ERA
for idate in DATE
d = idate.strftime('%Y%m%d')
filein = '%s/%s_%s%s'%(DATAERA,var_long,d,'.nc')
fileout_tmp = '%s/%s_%s%s'%(workdir,var_long,d,'_remapcon.nc')
fileout_EUR = '%s/%s_%s%s'%(workdir,var_long,d,'_remapcon_EUR.nc')
os.system('cdo remapcon,r360x181 ' + filein  + ' ' + fileout_tmp)
os.system('cdo remapcon,r360x181 ' + fileout_tmp  + ' ' + fileout_EUR)
os.system('rm ' + fileout_tmp)

