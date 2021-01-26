#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:43:49 2021

@author: siljesorland
"""
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs

dirbase = '/nird/projects/NS9001K/sso102/S2S/netcdf'
file='sst_CY46R1_2019-07-29_cf_EUR.nc'
data = '%s/%s'%(dirbase,file)

#fN = 'data/ARGO_ATL_20171230.nc'
#ATL = xr.open_dataset(fN)
