source ./read_content.sh

get_cur_cores()
{
    vmstat > current_core.out

    dataline=$(cat current_core.out)
    cur_cores=${dataline:159:160}
    cur_core=${cur_cores:2:4}

    return $cur_core
}

get_cur_core_1()
{
    vmstat > current_core.out
    filename=current_core.out

    line_times=1
    lines=3 # 第三行核数信息

    while read line
    do
        if [ $line_times = $lines ]
        then
            cur_cores=${line:0:3}
            echo $cur_cores
            break
        fi
        let "line_times++"
    done < $filename
    return $cur_cores
}

check_core()
{
    max_times=4
    times=0
    sum_cores=0

    until [ ! $times -lt $max_times ]
    do
        get_cur_core_2
        a=$?
        echo $a
        let "times++"
        sum_cores=`expr $a + $sum_cores`
        echo $sum_cores
        sleep 1
    done

    echo $sum_cores
    ave_cores=`expr $sum_cores / $max_times`
    echo $ave_cores
    return $ave_cores
}


check_core
a=$?
check_core
b=$?
c1=`expr $a - $b`
c2=`expr $a - $b`
d=10
if ((($c1 < $d) && ($c2 < $d)))
then
    echo ok
else
    echo no
fi
