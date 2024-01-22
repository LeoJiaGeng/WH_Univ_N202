#!/bin/bash
for inf in *.gjf
do
echo Running ${inf} ...
# 可以选择不加&符号，可以使其执行完自动提示
time g16 < ${inf} > ${inf//gjf/log} & 
echo ${inf} is finished
echo
done