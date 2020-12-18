#!/bin/bash

Data_ERA='/cluster/work/users/sso102/ERA5/work.5263'
Data_S2S='/cluster/work/users/sso102/S2S/work.73783'
workdir=/cluster/work/users/sso102/S2S/VALIDATION/work.$$

date='2018-07'

if [ ! -d ${workdir}/ ]
then
    mkdir ${workdir}
else
    rm -r ${workdir}
    mkdir ${workdir}
fi

y=$(echo ${date} | cut -d'-' -f1)
m=$(echo ${date} | cut -d'-' -f2)

cdo splitday ${Data_ERA}/ERA5_${y}${m}_r720x360_EUR.nc ${workdir}/ERA_${y}-${m}-

