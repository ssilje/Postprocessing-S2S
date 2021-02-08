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
import numpy as np
from calendar import monthrange,  monthcalendar, datetime

# Bergen
lat = 60.23
lon = 5.19
var_longname='sea_surface_temperature'
syr = 2000
eyr = 2005


for month in range(1,13):
    for y in range(syr,eyr):
        dates_month = pd.date_range(start='%s-%s-%s'%(y,month,'01'), periods=monthrange(y, month)[1], freq="D") 
        print(dates_month)
#
## ERA5
        dirbase = '/nird/projects/NS9001K/sso102/DATA/test'
        for i,d in enumerate(dates_month):
            dERA5 = '%s/%s_%s_%s'%(dirbase,var_longname,d.strftime('%Y%m%d'),'EUR1deg.nc')
            dataopen = xr.open_dataset(dERA5)
            if i == 0 and y == syr:
                ERA5_BR_daily = dataopen.sst.sel(lat=lat, lon=lon, method='nearest').resample(time='D').mean().to_dataframe()
            else:
                ERA5_BR_daily = pd.concat([ERA5_BR_daily, dataopen.sst.sel(lat=lat, lon=lon, method='nearest').resample(time='D').mean().to_dataframe()])

    for i in range(len(monthcalendar(2001,month))): # year without leap year

        for j in range(len(monthcalendar(2001,month)[i])):

            if monthcalendar(2001,month)[i][j] != 0:     
  
                day = '%s'%(monthcalendar(2001,month)[i][j])
               
                if int(day) < 10:
                    daystr = '0%s'%(day)
                 
                else:
                    daystr = '%s'%(day)
   
                date = pd.date_range(datetime.date(2001, month, int(day)),periods=1)

                
                ERA5_BR_day_clim = ERA5_BR_daily.sst[ERA5_BR_daily.index.strftime('%d')==daystr].mean()
        
                if int(day) == 1 and month == 1:
                    ERA5_BR_dayclim_df = pd.DataFrame(ERA5_BR_day_clim, index=date, columns=["day-clim SST"])
                    print('day = 1')
                else:
                    tmp = pd.DataFrame(ERA5_BR_day_clim, index=date, columns=["day-clim SST"])
               
                    ERA5_BR_dayclim_df = ERA5_BR_dayclim_df.append(tmp)   
    
                print(ERA5_BR_dayclim_df) 
                

 



                
                
           # print(i)
           # print(j)
        
for day in range(1,monthrange(2001, month)[1]): # just piked a year without leap year
    ERA5_BR_day_clim = ERA5_BR_daily.sst[ERA5_BR_daily.index.strftime('%d')==day].mean()



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
