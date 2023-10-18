#!/bin/bash

max_core=$1
echo "the maximum cores is $max_core";
wait_times=0

for file in *.gjf
do
    # print the file name
    echo ${file} is ready >> print_history.log 

    # endless loop infinite
    while true
    do
        # search the number of cores left three times
        vmstat > current_core.out
        sleep 1s
        vmstat > current_core.out
        sleep 1s
        vmstat > current_core.out
        # echo refresh the information of cores once

        dataline=$(cat current_core.out)
        cur_cores=${dataline:159:160}
        cur_core=${cur_cores:2:4}

        # set every file cores and calculate the number of cores later
        file_core=16
        add_core=`expr $file_core + $cur_core`

        # check input valid
        if (($file_core > $max_core))
        then
            echo error max cores in input >> print_history.log
            break
        fi

        # compare the number of cores to the number of cores
        if ((($cur_core < $max_core) && ($add_core < $max_core)))
        then
            time g16 < ${file} > ${file//gjf/log} &
            echo ${file} has been submitted >> print_history.log
            wait_times=0
            break
        else
            let "wait_times++"
            sleep 1m
            echo ${file} is waiting for ${wait_times} minutes >> print_history.log
        fi
    done
done


