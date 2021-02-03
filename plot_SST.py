#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:43:49 2021
@author: siljesorland
"""
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.dates as mdates
# Bergen
lat = 60.23
lon = 5.19

## ERA5
dirbase = '/nird/projects/NS9001K/sso102/S2S/DATA/SST'
fERA5='ERA5_sst_1999-2019_07_daymean_ydaymean.nc'
fERA5_std='ERA5_sst_1999-2019_07_daymean_ydaystd.nc'
ERA5 = '%s/%s'%(dirbase,fERA5)
ERA5_std = '%s/%s'%(dirbase,fERA5_std)

dataopen = xr.open_dataset(ERA5) 
ERA5_BR = dataopen.sel(lat=lat, lon=lon, method='nearest')
ERA5_BR_df=ERA5_BR.to_dataframe()

dataopen_std = xr.open_dataset(ERA5_std) 
ERA5_BR_std = dataopen_std.sel(lat=lat, lon=lon, method='nearest')
ERA5_BR_std_df=ERA5_BR_std.to_dataframe()
print("ERA5 DS head 15")
print(ERA5_BR.to_dataframe().head(15))

print("ERA5 std DS head 15")
print(ERA5_BR_std.to_dataframe().head(15))

## S2S
dirbase_S2S = '/nird/projects/NS9001K/sso102/DATA/test2'
fS2S='sst_CY46R1_2019-07-01_pf_2018-07-01.nc'
S2S = '%s/%s'%(dirbase_S2S,fS2S)
dataopen_S2S = xr.open_dataset(S2S) 
S2S_BR = dataopen_S2S.sel(latitude=lat, longitude=lon, method='nearest')
S2S_BR_df=S2S_BR.to_dataframe()

#SST_mean2=S2S_BR.sst.mean(dim='hdate') # mean over hindcast date
SST_mean=S2S_BR.sst.mean(dim='number') # mean over hindcast date

f, ax = plt.subplots(1, 1)
ax.plot(ERA5_BR.time, ERA5_BR.SST, color='0.1')
ax.plot(ERA5_BR.time, ERA5_BR.SST-ERA5_BR_std.SST, color='0.5')
ax.plot(ERA5_BR.time, ERA5_BR.SST+ERA5_BR_std.SST, color='0.5')
ax.plot(ERA5_BR.time, ERA5_BR.SST+ERA5_BR_std.SST, color='0.5')

xfmt = mdates.DateFormatter('%d')
ax.xaxis.set_major_formatter(xfmt)

ax.set_xlabel('time')
ax.set_ylabel('SST [K]')
ax.set_title('SST July', fontsize=16)



#ERA5_BR.SST_std.plot()-ERA5_BR.SST
#ERA5_BR.groupby(ERA5_BR_df.index.1).mean().plot()
f.savefig('SST_Bergen_v2.png')
