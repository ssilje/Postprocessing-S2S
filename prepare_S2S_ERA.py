import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.dates as mdates
import os,sys

DATABASE = '/nird/projects/NS9853K/DATA'
var_long='sea_surface_temperature' 
var_short='sst' 

# 10m_u_component_of_wind 2m_temperature sea_surface_temperature total_precipitation 10m_v_component_of_wind mean_sea_level_pressure snowfall


product = 'hindcast' # forecast



DATAERA = '%s/%s/'%(DATABASE,'SFE/ERA_daily_nc')
DATAS2S = '%s/%s/%s/%s'%(DATABASE,'S2S', product,'/ECMWF/sfc',var_short)



#,var_longname,forecastcycle,d,ftype,'.grb')
DATAERA='/nird/projects/NS9853K/DATA/SFE/ERA_daily_nc'

workdir='/cluster/work/users/sso102/ERA5/'



cdo remapcon,r360x181 $DATABASE/$varlongname_DATE.nc 

cdo sellonlatbox,-30,60,30,75 


os.system('grib_to_netcdf -I method,type,stream,refdate -o ' + 'era5_test.nc'  + ' ' + '/nird/projects/NS9001K/sso102/DATA/ERA5/sfc/sst/ERA5_sst_200312.grb')

dates_monday = pd.date_range("20190701", periods=52, freq="7D") # forecats start Monday
dates_thursday = pd.date_range("20190704", periods=52, freq="7D") # forecats start Thursday

#dates = pd.date_range("20190701", periods=52, freq="W") This one does not include the first date (20190701)

#for d in dates_monday
d = dates_monday[0].strftime('%Y-%m-%d')
file = '%s/%s/%s_%s_%s_%s%s'%(dir,var,var,forecastcycle,d,ftype,'.grb')
ds_grib = xr.open_dataset(file,engine='cfgrib')
