#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:43:49 2021

@author: siljesorland
"""
import numpy as np
import xarray as xr
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mpl
import cartopy as ccrs
import cartopy.feature as cfeature
import matplotlib.font_manager
from mpl_toolkits.basemap import Basemap,shiftgrid

ERAfile='ERA5_sst_1999-2019_07_Bergen_clim.nc'
f = Dataset(ERAfile, mode='r')
ERA_SST = f.variables['SST'][:]
ERA_time = f.variables['time'][:]

print(ERA_SST.shape)
#print(TP[-1,:,:].shape)
#print(TP[-1,:,:].min())
#print(TP[-1,:,:].max())
print(ERA_time)
