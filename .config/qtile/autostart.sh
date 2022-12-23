#!/bin/bash

$HOME/.config/qtile/pc-dp-hdmi.sh
feh --bg-fill $HOME/.config/wallpapers/favourites/deer-vector.png &
sh ~/.config/picom/picominit.sh &
thunar --daemon & 
dunst &
/cos/.config/polybar/launch.sh

# feh --bg-fill ~/.config/wallpapers/c2.jpg &
