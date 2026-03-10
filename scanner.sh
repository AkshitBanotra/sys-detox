#!/usr/bin/env bash

block_list=( "steam" "lutris" )
while true;do
	for i in "${block_list[@]}";do
		if pgrep -f ${i}  > /dev/null 2>&1;then
			notify-send "Focus Mode Active" "A restricted process was detected and has been terminated."
			pkill -f ${i}
		fi
	done
	sleep 2s
done
