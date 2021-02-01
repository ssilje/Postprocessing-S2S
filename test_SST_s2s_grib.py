import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.dates as mdates

product = 'hindcast' # forecast hindcast
dirbase = '/nird/projects/NS9853K/DATA/S2S/'
dir = '%s/%s/%s/'%(dirbase,product,'/ECMWF/sfc')
forecastcycle = 'CY46R1'
var='sst'
ftype='pf' #cf, pf

dates_monday = pd.date_range("20190701", periods=52, freq="7D") # forecats start Monday
dates_thursday = pd.date_range("20190704", periods=52, freq="7D") # forecats start Thursday

#dates = pd.date_range("20190701", periods=52, freq="W") This one does not include the first date (20190701)

#for d in dates_monday
d = dates[0].strftime('%Y-%m-%d')
file = '%s/%s/%s_%s_'%(dir,var,var,forecastcycle,d,'_',ftype,'.grb')

