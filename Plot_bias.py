#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:40:35 2020

@author: ssilje
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


nc_file='/nird/projects/NS9001K/sso102/S2S/VALIDATION/BIAS/BIAS_S2S-ERA_2018-07-27_2019-07-18_leadtime09.nc'
f = Dataset(nc_file, mode='r')
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
TP = f.variables['pr'][:]
time = f.variables['time'][:]

print(TP.shape)
#print(TP[-1,:,:].shape)
print(TP[-1,:,:].min())
print(TP[-1,:,:].max())
print(time)

fig = plt.figure(figsize=(15, 15))

#ax = Basemap(llcrnrlon=-25.,llcrnrlat=30.,urcrnrlon=45.,urcrnrlat=70.,\
#            rsphere=(6378137.00,6356752.3142),\
#            resolution='l',projection='merc',\
 #           lat_0=40.,lon_0=-20.,lat_ts=20.)

ax = Basemap(llcrnrlon=lon[0],llcrnrlat=lat[0],urcrnrlon=lon[-1],urcrnrlat=lat[-1],\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=40.,lon_0=-20.,lat_ts=20.)
#value,lon2=shiftgrid(180,TP[-1,:,:],lon,start=False)
value=TP[-1,:,:]
#ax.set_extent([5.75, 10.6, 45.7, 47.9])

#lines = cfeature.NaturalEarthFeature(
#    category='cultural',
#    name='admin_0_boundary_lines_land',
#    scale='10m',
#)

#ax.add_feature(lines, edgecolor='#000000', facecolor='none',
#    linewidth=2)

#ax.fillcontinents(color='gray',alpha=0.2) # Pavles favourite plotting style
ax.drawcoastlines()
ax.drawcountries()
#ax.fillcontinents(color='coral')
#ax.drawmapboundary()

ax.drawmeridians(np.arange(0, 360, 30))
ax.drawparallels(np.arange(-90, 90, 30))


xi,yi=np.meshgrid(lon,lat)
x,y=ax(xi,yi)

plt.title(time)

clev=np.linspace(-7,7,15)
ax.contourf(x, y, value, clev,  cmap='bwr', alpha=0.3, extend='both')
ax.colorbar()
fig.savefig('test.png')
