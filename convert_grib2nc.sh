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

if [ ! -d ${workdir}/tmp ]
then
    mkdir ${workdir}/tmp
else
    rm -r ${workdir}/tmp
    mkdir ${workdir}/tmp
fi
date='2019-07-08'

y=$(echo ${date} | cut -d'-' -f1)
m=$(echo ${date} | cut -d'-' -f2)
day=$(echo ${date} | cut -d'-' -f3)

HC='1'
        
#while [ ${HC} -le 20  ] ; do # 20 years hindcast
while [ ${HC} -le 5  ] ; do # 20 years hindcast
yHC=`expr ${y} - $HC`

#echo $yHC
#echo $day
#echo $date

echo ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}.grb



cdo -f nc copy  ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}.grb ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}.nc
cdo splitsel,1 ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}.nc ${workdir}/tmp/tmp_

cd ${workdir}/tmp

#daynum=$(echo | ls -L | wc -l)

#echo $daynum
n=0
while [ ${n} -le 40  ] ; do 
#echo $n
nm=`expr ${n} - 1`
#echo $nm
if [ $n -lt 10 ]; then
   if [ $n -eq 0 ]; then
     #
    echo "lead time 0" 
    cp tmp_000000.nc TP_00.nc
  
   elif [ $n -eq 10  ]; then
     ncdiff tmp_0000${n}.nc tmp_00000${nm}.nc TP_${n}.nc
   else
   ncdiff tmp_00000${n}.nc tmp_00000${nm}.nc TP_${n}.nc
  fi
  else 
   ncdiff tmp_0000${n}.nc tmp_0000${nm}.nc TP_${n}.nc
   fi
   
 #  elif [ $n -eq 10  ]; then
 #  ncdiff tmp_${n}.nc tmp_0${nm}.nc tp_cf_${date}_hc_${yHC}-${m}-${day}_f${n}.nc
  # else 
  # ncdiff tmp_${n}.nc tmp_${nm}.nc tp_cf_${date}_hc_${yHC}-${m}-${day}_f${n}.nc
  # fi
   
   
   
   n=`expr ${n} + 1`
done
   rm tmp_*.nc 
   
   cdo cat TP_*.nc ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}_daily.nc

HC=`expr ${HC} + 1`
done

