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

#DATE='2019-07-01 2019-07-04 2019-07-08 2019-07-11 2019-07-15 2019-07-18 2019-07-22 2019-07-25 2019-07-29 
#        2019-08-01 2019-08-05 2019-08-08 2019-08-12 2019-08-15 2019-08-19 2019-08-22 2019-08-26 2019-08-29 
#        2019-09-02 2019-09-05 2019-09-09 2019-09-12 2019-09-16 2019-09-19 2019-09-23 2019-09-26 2019-09-30 
#        2019-10-03 2019-10-07 2019-10-10 2019-10-14 2019-10-17 2019-10-21 2019-10-24 2019-10-28 2019-10-31 
#        2019-11-04 2019-11-07 2019-11-11 2019-11-14 2019-11-18 2019-11-21 2019-11-25 2019-11-28 
#        2019-12-02 2019-12-05 2019-12-09 2019-12-12 2019-12-16 2019-12-19 2019-12-23 2019-12-26 2019-12-30 
#        2020-01-02 2020-01-06 2020-01-09 2020-01-13 2020-01-16 2020-01-20 2020-01-23 2020-01-27 2020-01-30 
#        2020-02-03 2020-02-06 2020-02-10 2020-02-13 2020-02-17 2020-02-20 2020-02-24 2020-02-27 
#        2020-03-02 2020-03-05 2020-03-09 2020-03-12 2020-03-16 2020-03-19 2020-03-23 2020-03-26 2020-03-30 
#        2020-04-02 2020-04-06 2020-04-09 2020-04-13 2020-04-16 2020-04-20 2020-04-23 2020-04-27 2020-04-30 
#        2020-05-04 2020-05-07 2020-05-11 2020-05-14 2020-05-18 2020-05-21 2020-05-25 2020-05-28 
#        2020-06-01 2020-06-04 2020-06-08 2020-06-11 2020-06-15 2020-06-18 2020-06-22 2020-06-25 2020-06-29'


d='2019-07-01 2019-07-04 2019-07-08 2019-07-11 2019-07-15 2019-07-18 2019-07-22 2019-07-25 2019-07-29'

for date in ${d}; do

y=$(echo ${date} | cut -d'-' -f1)
m=$(echo ${date} | cut -d'-' -f2)
day=$(echo ${date} | cut -d'-' -f3)

HC='1'
        
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
  
  cdo -f nc copy  ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}_r720x360_EUR.grb ${workdir}/tmp.nc 
  ncks -A -v lon,lat /cluster/home/sso102/GRIDINFO/GRID_REGIONS/EUROPE/LAT_LON_r720x360_EUR.nc ${workdir}/tmp.nc 
  cdo divc,6 ${workdir}/tmp.nc ${workdir}/tmp2.nc # need to check if correct, but the TOT_PR is given as kms-2/6h
  ncrename  -v tp,pr ${workdir}/tmp2.nc ${workdir}/tmp3.nc
  ncatted -O -a units,pr,o,c,mm/day ${workdir}/tmp3.nc 
cdo splitsel,1 ${workdir}/tmp3.nc  ${workdir}/tmp/tmp_
rm ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}_r720x360.grb 
rm ${DATA_S2S}/tp_cf_${date}_hc_${yHC}-${m}-${day}_r720x360_EUR.grb 
rm ${DATA_S2S}/tmp*.nc ${workdir}/tmp*.nc 
pwd ${DATA_S2S} 
ls ${DATA_S2S}
pwd ${workdir}
ls ${workdir}

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
   
   cdo mergetime  ${workdir}/tmp/TP_*.nc ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}_daily.nc
  # rm  -r ${workdir}/tmp
  # rm   ${workdir}/tp_cf_${date}_hc_${yHC}-${m}-${day}.nc
   HC=`expr ${HC} + 1`
done
done
done
