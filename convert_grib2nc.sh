#!/bin/bash

DATA_S2S='/cluster/work/users/sso102/S2S/ECMWF/TOT_PR'

date='2019-07-08'

y=$(echo ${date} | cut -d'-' -f1)
m=$(echo ${date} | cut -d'-' -f2)
day=$(echo ${date} | cut -d'-' -f3)

HC='0'
        
while [ ${HC} -le 20  ] ; do # 20 years hindcast
yHC=`expr ${y} - $HC`
echo $yHC
echo $d
HC=`expr ${HC} + 1`
done