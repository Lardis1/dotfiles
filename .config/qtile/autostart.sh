#!/bin/bash

$HOME/.config/qtile/pc-dp-hdmi.sh

feh --bg-fill $HOME/.config/wallpapers/favourites/deer-vector.png &
/cos/.config/polybar/launch.sh &
sh ~/.config/picom/picominit.sh &

thunar --daemon & 
dunst &
