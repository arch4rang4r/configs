#!/usr/bin/env bash

##
#  Allows switching i3 workspaces by left/right
#  numerical direction thing.  Basically emulates
#  having 10 static workspaces
#

if [ $# == 0 ]
then
	echo "usage: $0 [left|right]" 1>&2
	exit
fi

DESK=$(i3-msg -t get_workspaces | jq 'map(select(.focused))[0].num')

if [ $1 == "right" ]
then
	let DESK+=1
	[ $DESK -eq 11 ] && DESK=1
elif [ $1 == "left" ]
then
	let DESK-=1
	[ $DESK -eq 0 ] && DESK=10
fi

i3-msg workspace $DESK
