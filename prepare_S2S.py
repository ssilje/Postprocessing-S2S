import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.dates as mdates
import os,sys

DATABASE = '/nird/projects/NS9853K/DATA'
workdir = '/nird/projects/NS9001K/sso102/DATA/test2'
var_long='sea_surface_temperature' 
var_short='sst' 

# 10m_u_component_of_wind 2m_temperature sea_surface_temperature total_precipitation 10m_v_component_of_wind mean_sea_level_pressure snowfall

cycle = 'CY46R1'
ftype= 'pf'

product = 'hindcast' # forecast

DATAS2S = '%s/%s/%s/%s/%s'%(DATABASE,'S2S', product,'/ECMWF/sfc',var_short)
dates_monday = pd.date_range("20190701", periods=52, freq="7D") # forecats start Monday
dates_monday_hc = pd.date_range("19990701", periods=20, freq="AS-JUL") 
dates_thursday = pd.date_range("20190704", periods=52, freq="7D") # forecats start Thursday

if not os.path.exists(workdir)  :
                os.makedirs(workdir)

for idate in dates_monday:
    d = idate.strftime('%Y-%m-%d')
    for hdate in dates_monday_hc:
        dh = hdate.strftime('%Y-%m-%d')
        filein = '%s/%s_%s_%s_%s_%s%s'%(DATAS2S,var_short,cycle,d,ftype,dh,'.grb')
        fileout = '%s/%s_%s_%s_%s_%s%s'%(workdir,var_short,cycle,d,ftype,dh,'.nc')
        if not os.path.isfile(fileout):
            os.system('grib_to_netcdf -I method,type,stream,refdate -o ' + fileout  + ' ' + filein)
    