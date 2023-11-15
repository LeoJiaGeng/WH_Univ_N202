#!/bin/bash

# function: read the number of cores in input file
# parms: file name; read lines; begin number; end number
get_cores()
{
    input_filename=$1   
    # number of cores in the $2 line
    aim_lines=$2 
    temp_times=1

    while read search_line
    do
        if [ $temp_times = $aim_lines ]
        then
            echo $search_line
            read_cores=${search_line:$3:$4}
            echo $read_cores
            break
        fi
        let "temp_times++"
    done < $input_filename
    return_value=$read_cores
}

# function: read the number of cores in system 
check_cores()
{
    max_try_times=4
    search_times=1
    sum_cores=0

    until [ ! $search_times -lt $max_try_times ]
    do
        vmstat > cur_core.out
        get_cores cur_core.out 3 0 3
        echo "$search_times time research, the core is $return_value"
        let "search_times++"
        sum_cores=`expr $a + $sum_cores`
        sleep 1
    done

    echo $sum_cores
    ave_cores=`expr $sum_cores / $max_times`
    echo $ave_cores
    return $ave_cores
}

ruler_cores()
{
    check_cores
    first_cores=$?
    check_cores
    second_cores=$?
    c1=`expr $first_cores - $second_cores`
    c2=`expr $first_cores - $second_cores`
    thread=10
    if ((($c1 < $thread) && ($c2 < $thread)))
    then
        echo ok
    else
        echo no
    fi
}

get_cores cur_core.out 3 0 3
echo $return_value
get_cores TS1-srcf-middle-ts.gjf 3 13 14
echo $return_value


