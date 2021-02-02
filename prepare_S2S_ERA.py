import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.dates as mdates
import os,sys

DATABASE = '/nird/projects/NS9853K/DATA'
workdir = '/nird/projects/NS9001K/sso102/DATA/test'
var_long='sea_surface_temperature' 
var_short='sst' 

# 10m_u_component_of_wind 2m_temperature sea_surface_temperature total_precipitation 10m_v_component_of_wind mean_sea_level_pressure snowfall

cycle = 'CY46R1'
ftype= 'pf'

product = 'hindcast' # forecast
DATE = '20190701'


DATAERA = '%s/%s/'%(DATABASE,'SFE/ERA_daily_nc')
DATAS2S = '%s/%s/%s/%s/%s'%(DATABASE,'S2S', product,'/ECMWF/sfc',var_short)


## Regrid ERA
filein = '%s/%s_%s%s'%(DATAERA,var_long,DATE,'.nc')
fileout = '%s/%s_%s%s'%(workdir,var_long,DATE,'_remapcon.nc')
fileout_EUR = '%s/%s_%s%s'%(workdir,var_long,DATE,'_remapcon_EUR.nc')
os.system('cdo remapcon,r360x181 ' + filein  + ' ' + fileout)
os.system('cdo remapcon,r360x181 ' + fileout  + ' ' + fileout_EUR)


## convert S2S
dates = pd.date_range(DATE, periods=52, freq="7D") # forecats start Monday
#sst_CY46R1_2020-03-02_pf.grb 
d = dates[0].strftime('%Y-%m-%d')
filein_S2S = '%s/%s_%s_%s_%s%s'%(DATAS2S,var_short,cycle,d,ftype,'.grb')
fileout_S2S = '%s/%s_%s_%s_%s%s'%(workdir,var_short,cycle,d,ftype,'.nc')
os.system('grib_to_netcdf -I method,type,stream,refdate -o ' + fileout_S2S  + ' ' + filein_S2S)

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
