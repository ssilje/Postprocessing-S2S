#!/bin/bash

DATA_ERA5='/cluster/work/users/sso102/ERA5/TP_daily/'
workdir=/cluster/work/users/sso102/ERA5/work.$$


if [ ! -d ${workdir}/ ]
then
    mkdir ${workdir}
else
    rm -r ${workdir}
    mkdir ${workdir}
fi


date='2018-02'

y=$(echo ${date} | cut -d'-' -f1)
m=$(echo ${date} | cut -d'-' -f2)


  
  cdo remapcon,r720x360  ${DATA_ERA5}/ERA5_${y}${m}.grb ${workdir}/ERA5_${y}${m}_r720x360.grb
  cdo sellonlatbox,-30,60,30,75  ${workdir}/ERA5_${y}${m}_r720x360.grb ${workdir}/ERA5_${y}${m}_r720x360_EUR.grb
  
  cdo -f nc copy  ${workdir}/ERA5_${y}${m}_r720x360_EUR.grb ${workdir}/tmp.nc 
  cdo mulc,1000 $${workdir}/tmp.nc ${workdir}/tmp2.nc # convert to kg/m2
  ncrename  -v var228,PR ${workdir}/tmp2.nc ${workdir}/ERA5_${y}${m}_r720x360_EUR.nc
  ncatted -O -a units,pr,o,c,mm/day ${workdir}/ERA5_${y}${m}_r720x360_EUR.nc
  rm ${workdir}/ERA5_${y}${m}_r720x360.grb ${workdir}/ERA5_${y}${m}_r720x360_EUR.grb 
  
