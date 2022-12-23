#!/bin/bash

workspace_has_window=$(wmctrl -l | tr -s ' ' | cut -d ' ' -f 2 | grep "$1")
active_window=$(xdotool get_desktop | grep "$1")

#  

if [ ! -z "$active_window" ];
then
    echo "%{F#0f0}  %{F-}"
elif [ -z "$workspace_has_window" ];
then
    echo "%{F#3e3e3e}  %{F-}"
else
    echo "%{F#7e7e7e}  %{F-}"
fi