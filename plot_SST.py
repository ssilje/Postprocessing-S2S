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
# Bergen
lat = 60.23
lon = 5.19

## ERA5

dirbase = '/nird/projects/NS9001K/sso102/S2S/DATA/SST'
fERA5='ERA5_sst_1999-2019_07.nc'
ERA5 = '%s/%s'%(dirbase,fERA5)
dataopen = xr.open_dataset(ERA5) 
ERA5_BR = dataopen.sel(lat=lat, lon=lon, method='nearest').resample(time='D').mean()
#s = pd.Series(index=pd.date_range(start=dt.datetime(2014,1,1), end = dt.datetime(2015,6,1)), data = np.random.randn(517))
ERA5_BR_df=ERA5_BR.to_dataframe()
#ERA5_BR_mon = '/'.join([d.replace('%i'%refyear,'%i'%i) for i in range(refyear-20,refyear)])
#ERA5_BR_mon = ERA5_BR.groupby(ERA5_BR_df.index.'%i').mean()
#[d.replace('%i'%refyear,'%i'%i) for i in range(refyear-20,refyear)])

#for i in np.arange(1,32,1):
#    ERA5_BR.groupby(ERA5_BR_df.index.i).mean()
    


print("ERA5 DS head 15")
print(ERA5_BR.to_dataframe().head(15))
#star_ERA5_BR=ERA5_BR.stat()
fig = plt.figure(figsize=(15, 15))
#ERA5_BR.SST.plot()
ERA5_BR.groupby(ERA5_BR_df.index.day).mean().plot()
fig.savefig('SST_Bergen_v2.png')
