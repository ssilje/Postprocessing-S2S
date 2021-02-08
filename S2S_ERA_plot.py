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

var_long='sea_surface_temperature' 
var_short='sst' 

# 10m_u_component_of_wind 2m_temperature sea_surface_temperature total_precipitation 10m_v_component_of_wind mean_sea_level_pressure snowfall

cycle = 'CY46R1'
ftype= 'pf'
product = 'hindcast' # forecast



syr = 2000
eyr = 2005
climyear = 2018
dirbase = '/nird/projects/NS9001K/sso102/DATA/test'

for month in range(1,13):
    for y in range(syr,eyr):
        dates_month = pd.date_range(start='%s-%s-%s'%(y,month,'01'), periods=monthrange(y, month)[1], freq="D") 
        #print(dates_month)
#
## ERA5
        
        for i,d in enumerate(dates_month):
            dERA5 = '%s/%s_%s_%s'%(dirbase,var_long,d.strftime('%Y%m%d'),'EUR1deg.nc')
            dataopen = xr.open_dataset(dERA5)
            if i == 0 and y == syr:
                ERA5_BR_daily = dataopen.sst.sel(lat=lat, lon=lon, method='nearest').resample(time='D').mean().to_dataframe()
            else:
                ERA5_BR_daily = pd.concat([ERA5_BR_daily, dataopen.sst.sel(lat=lat, lon=lon, method='nearest').resample(time='D').mean().to_dataframe()])

    for i in range(len(monthcalendar(climyear,month))): # year without leap year

        for j in range(len(monthcalendar(climyear,month)[i])):

            if monthcalendar(climyear,month)[i][j] != 0:     
  
                day = '%s'%(monthcalendar(climyear,month)[i][j])
               
                if int(day) < 10:
                    daystr = '0%s'%(day)
                 
                else:
                    daystr = '%s'%(day)
   
                date = pd.date_range(datetime.date(climyear, month, int(day)),periods=1)
                ERA5_BR_day_clim_mean = ERA5_BR_daily.sst[ERA5_BR_daily.index.strftime('%d')==daystr].mean()
                ERA5_BR_day_clim_std = ERA5_BR_daily.sst[ERA5_BR_daily.index.strftime('%d')==daystr].std()
        
                if int(day) == 1 and month == 1:
                    ERA5_BR_dayclim_mean_df = pd.DataFrame(ERA5_BR_day_clim_mean, index=date, columns=["day-clim SST"])
                else:
                    tmp_mean = pd.DataFrame(ERA5_BR_day_clim_mean, index=date, columns=["day-clim SST"])
                    ERA5_BR_dayclim_mean_df = ERA5_BR_dayclim_mean_df.append(tmp_mean)   

                    

## S2S
dirbase_S2S = '/nird/projects/NS9001K/sso102/DATA/test2'
#fS2S='sst_CY46R1_2019-07-01_pf_2018-07-01.nc'
dates_monday = pd.date_range("20190701", periods=1, freq="7D") # forecats start Monday
dates_thursday = pd.date_range("20190704", periods=52, freq="7D") # forecats start Thursday

for idate in dates_monday: 
    d = idate.strftime('%Y-%m-%d')
   # print('d')
   # print(d)
    dates_hc = pd.date_range((idate-pd.DateOffset(years=20)), periods=20, freq="AS-JUL") #20 years hindcast
    #print(dates_hc)
    for hdate in dates_hc:
        dh = hdate.strftime('%Y-%m-%d')
        print(dh)
        dS2S = '%s/%s_%s_%s_%s_%s%s'%(dirbase_S2S,var_short,cycle,d,ftype,dh,'.nc')
        dataopen = xr.open_dataset(dS2S)
        S2S_BR_daily = dataopen.sst.sel(latitude=lat, longitude=lon, method='nearest').to_dataframe()
        ## Loop through the whole forecast
        forecast_leadtime = pd.date_range(dh, periods=46, freq="D")
        for fc_lt in forecast_leadtime: 
            s2s_mean = S2S_BR_daily.sst[S2S_BR_daily.index.get_level_values('time') == fc_lt].mean()
            s2s_std = S2S_BR_daily.sst[S2S_BR_daily.index.get_level_values('time') == fc_lt].std()
            print(d)
            print(dh)
            if d == "2019-07-01" and dh == "1999-07-01" and fc_lt == "1999-07-01": # first forecast day
                S2S_BR_df = pd.DataFrame({"ensmean SST": s2s_mean, "ensstd SST": s2s_std }, index=pd.date_range(fc_lt,periods=1), columns=["ensmean SST","ensstd SST"])
            else:
                tmp_mean = pd.DataFrame({"ensmean SST": s2s_mean, "ensstd SST": s2s_std }, index=pd.date_range(fc_lt,periods=1), columns=["ensmean SST","ensstd SST"])
                #tmp_mean = pd.DataFrame(s2s_mean, index=pd.date_range(hdate,periods=1), columns=["ensmean SST","ensstd SST"])
                S2S_BR_df = S2S_BR_df.append(tmp_mean)   
 


        #if i == 0 and y == syr:
             #   ERA5_BR_daily = dataopen.sst.sel(lat=lat, lon=lon, method='nearest').resample(time='D').mean().to_dataframe()
        #else:
         #       ERA5_BR_daily = pd.concat([ERA5_BR_daily, dataopen.sst.sel(lat=lat, lon=lon, method='nearest').resample(time='D').mean().to_dataframe()])
    
    
S2S_BR_mean = S2S_BR_daily.mean(dim='number')
ens_std = ds_en.std(dim='number')   
        

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
