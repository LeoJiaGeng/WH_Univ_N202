#!/bin/bash

echo "input the maximum cores";
max_core=$1
echo "the maximum cores is $max_core";

for file in *.gjf; do
    echo ${file} is ready # print the file name

    # endless loop infinite
    while true
    do
        # search the number of cores left
        vmstat > current_core.out
        sleep 1s
        vmstat > current_core.out
        sleep 1s
        vmstat > current_core.out
        echo refresh the information of cores once

        dataline=$(cat current_core.out)
        cur_cores=${dataline:159:160}
        cur_core=${cur_cores:2:4}

        # set every file cores and calculate the number of cores later
        file_core=16
        add_core=`expr $file_core + $cur_core`

        # check input valid
        if (($cur_core > $max_core))
        then
            echo error max cores in input
            break
        fi

        # compare the number of cores to the number of cores
        if ((($cur_core < $max_core) && ($add_core < $max_core)))
        then
            time g16 < ${file} > ${file//gjf/log} &
            echo ${file} has been submitted
            break
        else
            sleep 30s
            echo ${file} is waiting 
        fi
    done
done


