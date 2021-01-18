#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:43:49 2021

@author: siljesorland
"""
import numpy as np
import xarray as xr
import netCDF4
#from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mpl
import cartopy as ccrs
import cartopy.feature as cfeature
import matplotlib.font_manager
from mpl_toolkits.basemap import Basemap,shiftgrid

ERAfile='ERA5_sst_1999-2019_07_Bergen_clim.nc'
f = Dataset(ERAfile, mode='r')
ERA_SST = f.variables['SST']
ERA_time = f.variables['time']

#time_var = nc.variables['time']
dtime = netCDF4.num2date(ERA_time[:],ERA_time.units)
first = netCDF4.num2date(ERA_time[0],ERA_time.units)
last = netCDF4.num2date(ERA_time[-1],ERA_time.units)
print(first.strftime('%Y-%b-%d %H:%M'))
print(last.strftime('%Y-%b-%d %H:%M'))


print(ERA_SST.shape)
#print(TP[-1,:,:].shape)
#print(TP[-1,:,:].min())
#print(TP[-1,:,:].max())
print(ERA_time)

#data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
#names = list(data.keys())
#values = list(data.values())

fig, ax = plt.subplots() # 
#fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
#axs[0].bar(names, values)
#axs[1].scatter(names, values)
#axs[2].plot(names, values)
ax.plot(time, dog, label="dog")
ax.plot(activity, cat, label="cat")
ax.legend()

plt.show()
fig.suptitle('Categorical Plotting')
