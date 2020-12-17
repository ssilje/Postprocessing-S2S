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

HC='1'
        
#while [ ${HC} -le 20  ] ; do # 20 years hindcast
while [ ${HC} -le 1  ] ; do # 20 years hindcast
  yHC=`expr ${y} - $HC`
  echo ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}.grb
  if [ ! -d ${workdir}/tmp ]
     then
     mkdir ${workdir}/tmp
  else
     rm -r ${workdir}/tmp
     mkdir ${workdir}/tmp
  fi
  
  cdo remapcon,r720x360  ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}.grb ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}_r720x360.grb
  cdo sellonlatbox,-30,60,30,75  ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}_r720x360.grb ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}_r720x360_EUR.grb
  
  cdo -f nc copy  ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}_r720x360_EUR.grb ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}.nc
  cdo splitsel,1 ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}.nc ${workdir}/tmp/tmp_
  rm ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}_r720x360.grb ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}_r720x360_EUR.grb


#daynum=$(echo | ls -L | wc -l)

#echo $daynum
  n=0
  while [ ${n} -le 40  ] ; do 
  cd ${workdir}/tmp
  #echo $n
  nm=`expr ${n} - 1`
  #echo $nm
  if [ $n -le 10 ]; then
     if [ $n -eq 0 ]; then
       echo "lead time $n" 
       cp tmp_000000.nc TP_${n}.nc
  
     elif [ $n -eq 10  ]; then
       echo "lead time $n"
       ncdiff tmp_0000${n}.nc tmp_00000${nm}.nc TP_${n}.nc
     elif  [ $n -gt 0 ] && [ $n -lt 10 ]; then
       echo "lead time $n"
       ncdiff tmp_00000${n}.nc tmp_00000${nm}.nc TP_${n}.nc
     fi
  
   else 
      echo "lead time $n"
      ncdiff tmp_0000${n}.nc tmp_0000${nm}.nc TP_${n}.nc
   fi
   cdo showdate TP_${n}.nc
 #  elif [ $n -eq 10  ]; then
 #  ncdiff tmp_${n}.nc tmp_0${nm}.nc tp_cf_${date}_hc_${yHC}-${m}-${day}_f${n}.nc
  # else 
  # ncdiff tmp_${n}.nc tmp_${nm}.nc tp_cf_${date}_hc_${yHC}-${m}-${day}_f${n}.nc
  # fi
   
   
   
   n=`expr ${n} + 1`
 done
   cd ${workdir}/tmp
   #rm  ${workdir}/tmp/tmp_*.nc 
   
   cdo cat  ${workdir}/tmp/TP_*.nc ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}_daily.nc
  # rm  -r ${workdir}/tmp
  # rm   ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}.nc
   HC=`expr ${HC} + 1`
done

