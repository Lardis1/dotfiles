#!/usr/bin/env bash

# Terminate already running bar instances
killall polybar

# env vars
# export WIRELESS_OUTPUT="loading ..."
# export WIRED_OUTPUT="loading ..."

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch polybar
for mon in $(polybar --list-monitors | cut -d":" -f1); do
    # MONITOR=$m polybar --reload workspaces &
    for bar in rofi launchers spotify workspaces volume network date time power; do
        MONITOR=$mon polybar --reload -c ~/.config/polybar/config.ini "$bar" &
    done
done

