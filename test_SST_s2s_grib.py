import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.dates as mdates
import os,sys

meta = {
    'sst': {
        'param': '228228',  
        'levtype': 'sfc',
        'grid': '1/1',
        'step': '/'.join(['%i'%i for i in range(0,1104,24)]) # 40 days forecast
    }

}

for filename in (
    'VAR',
):

for k,v in meta[filename].items():
                    dic[k] = v



product = 'hindcast' # forecast hindcast
dirbase = '/nird/projects/NS9853K/DATA/S2S'
dir = '%s/%s/%s/'%(dirbase,product,'/ECMWF/sfc')
forecastcycle = 'CY46R1'
var='sst'
ftype='pf' #cf, pf
lat=60.23
lon=5.19
dates_monday = pd.date_range("20190701", periods=52, freq="7D") # forecats start Monday
dates_thursday = pd.date_range("20190704", periods=52, freq="7D") # forecats start Thursday

#dates = pd.date_range("20190701", periods=52, freq="W") This one does not include the first date (20190701)

#for d in dates_monday
d = dates_monday[0].strftime('%Y-%m-%d')
file = '%s/%s/%s_%s_%s_%s%s'%(dir,var,var,forecastcycle,d,ftype,'.grb')
ds_grib = xr.open_dataset(file,engine='cfgrib')

ds_grib_crop = ds_grib.sel(latitude=lat, longitude=lon, method='nearest')
#ds_grib_reg = ds_grib.sel(latitude=slice(50,30), longitude=slice(180,240)) to select a whole region

ds_crop= ds_grib_crop.to_dataframe()

ds_crop_mean = ds_crop.mean(level=0) # level 0 shape 10,4
ds_crop_mean = ds_crop.mean(level=1) # level 1 shape 46,4




