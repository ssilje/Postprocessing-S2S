#!/bin/bash

DATA_S2S='/cluster/work/users/sso102/S2S/ECMWF/TOT_PR'
workdir=/cluster/work/users/sso102/S2S/work.$$
 
if [ ! -d ${workdir}/ ]
then
    mkdir ${workdir}
else
    rm -r ${workdir}
    mkdir ${workdir}
fi

date='2019-07-08'

y=$(echo ${date} | cut -d'-' -f1)
m=$(echo ${date} | cut -d'-' -f2)
day=$(echo ${date} | cut -d'-' -f3)

HC='0'
        
#while [ ${HC} -le 20  ] ; do # 20 years hindcast
while [ ${HC} -le 5  ] ; do # 20 years hindcast
yHC=`expr ${y} - $HC`
echo $yHC
echo $day
echo $date
echo ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}.grb
mkdir ${workdir}/tmp
cdo -f nc copy  ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}.grb ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}.nc
cdo splitday ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}.nc ${workdir}/tmp/tmp_

cd ${workdir}/tmp

daynum=$(echo | ls -L | wc -l)

echo $daynum

HC=`expr ${HC} + 1`


done
