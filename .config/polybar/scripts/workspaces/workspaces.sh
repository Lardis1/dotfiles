#!/bin/bash

monitor() {
    xrandr --listmonitors | grep $1 | cut -d: -f 1
}

workspace_windows() {
    qtile cmd-obj -o group $1 -f info | grep "'windows': " | tr -d ' ' | sed -s "s/'windows':\[//g" | cut -d ] -f1
}

screen() {
    qtile cmd-obj -o group $1 -f info | grep "'screen': " | tr -d ' ' | sed -s "s/'screen'://g" | cut -d , -f1
}

get_icon() {
    if [ "$(screen $1)" -eq "$(monitor $2)" ];
    then
        echo "%{F#0f0}  %{F-}"
    elif [ "$(screen $1)" != "None" ];
    then
        echo "%{F#f55}  %{F-}"
    elif [ ! -z "$(workspace_windows $1)" ];
    then
        echo "%{F#7e7e7e}  %{F-}"
    else
        echo "%{F#3e3e3e}  %{F-}"
    fi
}

get_icon $1 $2
