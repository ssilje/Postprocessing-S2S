#!/bin/bash

Data_ERA='/cluster/work/users/sso102/ERA5/work.5263'
Data_S2S='/cluster/work/users/sso102/S2S/work.73783'
workdir=/cluster/work/users/sso102/S2S/VALIDATION/work.$$
savedir=/cluster/work/users/sso102/S2S/VALIDATION/BIAS
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


Df='2019-07-01 2019-07-04 2019-07-08 2019-07-11 2019-07-15 2019-07-18 2019-07-22 2019-07-25 2019-07-29' 
HC=1

if [ ! -d ${workdir}/ ]
then
    mkdir ${workdir}
else
    rm -r ${workdir}
    mkdir ${workdir}
fi

if [ ! -d ${savedir}/ ]
then
    mkdir ${savedir}
else
    rm -r ${savedir}
    mkdir ${savedir}
fi


for DATEforecasts in ${Df}; do

#date='2018-07'

yy=$(echo ${DATEforecasts} | cut -d'-' -f1)
y=`expr ${yy} - ${HC}`
m=$(echo ${DATEforecasts} | cut -d'-' -f2)


fday=$(echo ${DATEforecasts} | cut -d'-' -f3)
#echo ${fday}

cdo splitday ${Data_ERA}/ERA5_${y}${m}_r720x360_EUR.nc ${workdir}/ERA_${y}-${m}-
cd ${workdir}
daynum=$(echo | ls -L | wc -l)
cdo splitsel,1 ${Data_S2S}/tp_cf_${DATEforecasts}_hc_${y}-${m}-${fday}_daily.nc ${workdir}/S2S_${y}-${m}_${DATEforecasts}_leadtime
#echo $daynum

dd=1
while [ $dd -le ${daynum} ]; do
leadtime=0
valdd=${dd}
	if [ ${fday} -eq ${dd} ]; then
		while [ ${valdd} -le 31 ]; do
		echo ${valdd}
		if [ ${valdd} -lt 10 ]; then
		valdd=`expr 0${valdd}`
		fi
		if [ ${leadtime} -lt 10  ]; then
		leadtime=`expr 0${leadtime}`
		fi
             
	     echo ${valdd}
                 ncdiff S2S_${y}-${m}_${DATEforecasts}_leadtime0000${leadtime}.nc ERA_${y}-${m}-${valdd}.nc ${savedir}/BIAS_S2S-ERA_${y}-${m}-${valdd}_${DATEforecasts}_leadtime${leadtime}.nc
                leadtime=`expr ${leadtime} + 1`
		valdd=`expr ${valdd} + 1`
	    done
	fi
	dd=`expr ${dd} + 1`
 done


rm ERA_*.nc S2S_*.nc
done
