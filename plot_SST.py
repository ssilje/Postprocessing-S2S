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
print("ERA5 DS head 15")
print(ERA5_BR.to_dataframe().head(15))

fig = plt.figure(figsize=(15, 15))
ERA5_BR.SST.plot()

fig.savefig('SST_Bergen_v2.png')
