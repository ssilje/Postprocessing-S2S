#!/bin/bash
product='hindcast'
type='pf'
DATA_S2S=/nird/projects/NS9853K/DATA/S2S/${product}/ECMWF/sfc/sst/
workdir=/nird/projects/NS9001K/sso102/S2S/netcdf
 
if [ ! -d ${workdir}/ ]
then
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


d='2019-07-01'

#d='2019-07-01'

for date in ${d}; do # for (1)

    y=$(echo ${date} | cut -d'-' -f1)
    m=$(echo ${date} | cut -d'-' -f2)
    day=$(echo ${date} | cut -d'-' -f3)

  if [ -f ${DATA_S2S}/sst_CY46R1_${date}_${type}.grb ]; then 
            echo "file exist: "
	    echo ${DATA_S2S}/sst_CY46R1_${date}_${type}.grb
	    if [ ! -d ${workdir}/tmp ]
	    then
		mkdir ${workdir}/tmp
	    else
		rm -r ${workdir}/tmp
		mkdir ${workdir}/tmp
	    fi
  
	    cdo sellonlatbox,-30,60,30,75  ${DATA_S2S}//sst_CY46R1_${date}_${type}.grb ${workdir}/sst_CY46R1_${date}_${type}_EUR.grb
	    
	    cdo -f nc copy  ${workdir}/sst_CY46R1_${date}_${type}_EUR.grb ${workdir}/sst_CY46R1_${date}_${product}_${type}_EUR.nc
	    #ncl_convert2nc ${workdir}/sst_CY46R1_${date}_${type}_EUR.grb ${workdir}/sst_CY46R1_${date}_${product}_${type}_EUR_ncl.nc
	  	    
	else
	    echo "file does not exist: "
            echo ${DATA_S2S}/sst_CY46R1_${date}_${type}.grb
	fi    
    rm ${workdir}/*.grb
    rm  -r ${workdir}/tmp
done # for (1)

#done 
