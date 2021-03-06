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

syear=1999
eyear=2019
month='01 02 03 04 05 06 07 08 09 10 11 12'
YYYY=${syear}

while [ ${YYYY} -le ${eyear} ]
do

for m in ${month}; do 

date=$YYYY-$m

#d='2018-07 2018-08'


#for date in $d; do


y=$(echo ${date} | cut -d'-' -f1)
m=$(echo ${date} | cut -d'-' -f2)


  
  cdo remapcon,r720x360  ${DATA_ERA5}/ERA5_${y}${m}.grb ${workdir}/ERA5_${y}${m}_r720x360.grb
  cdo sellonlatbox,-30,60,30,75  ${workdir}/ERA5_${y}${m}_r720x360.grb ${workdir}/ERA5_${y}${m}_r720x360_EUR.grb
  
  cdo -f nc copy  ${workdir}/ERA5_${y}${m}_r720x360_EUR.grb ${workdir}/tmp.nc 
  cdo mulc,1000 ${workdir}/tmp.nc ${workdir}/tmp2.nc # convert to kg/m2
  ncrename  -v var228,pr ${workdir}/tmp2.nc ${workdir}/ERA5_${y}${m}_r720x360_EUR.nc
  ncatted -O -a units,pr,o,c,mm/day ${workdir}/ERA5_${y}${m}_r720x360_EUR.nc
  rm ${workdir}/ERA5_${y}${m}_r720x360.grb ${workdir}/ERA5_${y}${m}_r720x360_EUR.grb ${workdir}/tmp2.nc ${workdir}/tmp.nc
  done
  YYYY=`expr ${YYYY} + 1`
  done
