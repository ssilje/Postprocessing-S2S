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

## S2S
dirbase = '/nird/projects/NS9001K/sso102/S2S/netcdf'
fhindcast_pf='sst_CY46R1_2019-07-01_hindcast_pf_EUR.nc'
fhindcast_cf='sst_CY46R1_2019-07-01_hindcast_cf_EUR.nc'
fforecast_pf='sst_CY46R1_2019-07-01_forecast_pf_EUR.nc'
fforecast_cf='sst_CY46R1_2019-07-01_forecast_cf_EUR.nc'

hindcast_pf = '%s/%s'%(dirbase,fhindcast_pf)
hindcast_cf = '%s/%s'%(dirbase,fhindcast_cf)
forecast_pf = '%s/%s'%(dirbase,fforecast_pf)
forecast_cf = '%s/%s'%(dirbase,fforecast_cf)

## hindcast_pf
dataopen = xr.open_dataset(hindcast_pf)
print(dataopen.variables.keys())
hindcast_pf_sst = dataopen['sst']
hindcast_pf_time = dataopen['time']
hindcast_pf_sst_BR = hindcast_pf_sst.sel(lat=lat, lon=lon, method='nearest')
#hindcast_ens_mean = hindcast_pf_sst_BR.mean(dim='number')

print('Shape of the data:')
print(' * all:', hindcast_pf_sst.shape)
print(' * BR:', hindcast_pf_sst_BR.shape)
print(' * time:', hindcast_pf_time.shape)
#print(' * mean:', hindcast_ens_mean.shape)

## hindcast_cf                                                                                                                                                                                          
dataopen = xr.open_dataset(hindcast_cf) 
hindcast_cf_sst = dataopen['sst']
hindcast_cf_time = dataopen['time']
hindcast_cf_sst_BR = hindcast_cf_sst.sel(lat=lat, lon=lon, method='nearest')

print('Shape of the data:')
print(' * all:', hindcast_cf_sst.shape)
print(' * BR:', hindcast_cf_sst_BR.shape)
print(' * time:', hindcast_cf_time.shape)

## forecast_cf                                                                                                                                                                                          
dataopen = xr.open_dataset(forecast_cf)
forecast_cf_sst = dataopen['sst']
forecast_cf_time = dataopen['time']
forecast_cf_sst_BR = forecast_cf_sst.sel(lat=lat, lon=lon, method='nearest')

print('Shape of the data:')
print(' * all:', forecast_cf_sst.shape)
print(' * BR:', forecast_cf_sst_BR.shape)
print(' * time:', forecast_cf_time.shape)

## forecast_cf                                                                                                                                                                                          
dataopen = xr.open_dataset(forecast_pf)
forecast_pf_sst = dataopen['sst']
forecast_pf_time = dataopen['time']
forecast_pf_sst_BR = forecast_pf_sst.sel(lat=lat, lon=lon, method='nearest')

print('Shape of the data:')
print(' * all:', forecast_pf_sst.shape)
print(' * BR:', forecast_pf_sst_BR.shape)
print(' * time:', forecast_pf_time.shape)


hindcast_pf_sst_dst=hindcast_pf_sst.to_dataframe()
print(hindcast_pf_sst_dst)

fig = plt.figure(figsize=(15, 15))
#ERA5_sst_BR.plot()
ERA5_BR
hindcast_pf_sst_BR.plot()
hindcast_cf_sst_BR.plot()
forecast_cf_sst_BR.plot()
forecast_pf_sst_BR.plot()
#dataopen.to_dataframe().head(15)
fig.savefig('SST_Bergen.png')
