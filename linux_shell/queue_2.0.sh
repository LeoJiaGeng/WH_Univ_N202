#!/bin/bash

# function: read the number of cores in any file
# parms: file name; read lines; begin number; end number
get_cores()
{
    filename=$1   

    times=1 # 起始行数
    lines=$2 # 第三行核数信息

    while read line
    do
        if [ $times = $lines ]
        then
            #echo $line
            read_cores=${line:$3:$4}
            #echo $read_cores
            break
        fi
        let "times++"
    done < $filename
}

# function: read the rest of the core numbers in the system
# parms: return $read_cores
get_sys_cores()
{
    vmstat > cur_core.log
    get_cores cur_core.log 3 0 3
}
 
# function: read the number of cores in the input file
# parms: return $read_cores
get_file_cores()
{
    get_cores $1 3 13 14
}

# function: calculate the rest of the core numbers in the system precisely
check_cores()
{
    max_try_times=3 # 每次连续查询三次
    search_times=0
    sum_cores=0
    cores_list=()
    thread=10
    err_num=255

    until [ ! $search_times -lt $max_try_times ]
    do
        get_sys_cores
        # echo "$search_times time research, the core is $read_cores"
        let "search_times++"
        sum_cores=`expr $read_cores + $sum_cores`
        sleep 1
        cores_list[$search_times]=$read_cores
    done

    # echo $sum_cores
    ave_cores=`expr $sum_cores / $max_try_times`
    # echo $ave_cores
    echo ${cores_list[@]} >> sh_history.log

    length=${#cores_list[@]}

    for num in ${cores_list[@]} 
    do
        gap=`expr $num - $ave_cores`
        if (($gap > $thread))
        then
            echo "get sys cores to err" >> sh_history.log
            return $err_num
        fi
    done
    echo "get sys cores to success" >> sh_history.log

    return $ave_cores
}

echo "---the program created by Leo!---"

max_core=$1
echo "the input maximum cores is $max_core, please check it";
wait_times=0
add_core=0 # define param first

# Cleaning old output files
if test -f sh_history.log
then
    rm sh_history.log
    # echo "sh_history.log is deleted"
fi

if test -f file.log
then
    rm file.log
    echo "file.log is deleted" >> sh_history.log
fi

if test -f cur_core.log
then
    rm cur_core.log
    echo "cur_core.log is deleted" >> sh_history.log
fi

# start 
echo "The program is starting !!!"

for file in *.gjf 
do
    # print the file name
    echo ${file} is ready >> sh_history.log 

    # endless loop infinite
    while true
    do
        # get the file cores
        get_file_cores ${file}
        cur_file_core=$read_cores
        echo "The current file core is $cur_file_core" >> sh_history.log

        # get the rest of the system cores
        check_cores
	cur_sys_core=$?
        echo "The current system core is $cur_sys_core" >> sh_history.log
        
        # set every file core and calculate the number of cores later
        add_core=`expr $cur_file_core + $cur_sys_core`

        # check input valid
        if (($cur_file_core > $max_core))
        then
            echo error max cores in input >> sh_history.log
            break
        fi

        echo "add core is $add_core" >> sh_history.log

        # compare the number of cores to the number of cores
        if ((($cur_sys_core < $max_core) && ($add_core < $max_core)))
        then
            time g16 < ${file} > ${file//gjf/log} &
            echo ${file} has been submitted >> sh_history.log
            echo ${file} has been submitted >> file.log
            wait_times=0
            break
        elif ((($cur_sys_core == 255)))
        then
            echo -e "err, search sys cores again 1 sec later" >> sh_history.log
            sleep 1
        else
            let "wait_times++"
            echo -e "${file} is waiting for ${wait_times} minutes" >> file.log
            sleep 1m
        fi
    done
done

echo "---The program finished !!!---"

