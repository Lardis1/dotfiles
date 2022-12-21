#!/bin/sh

# yad  --text-info \
#     --button=Cancel:0 \
#     --button=Restart:1 \
#     --button=Shutdown:2 \
#     --text "Power Options"

# echo $?

yad --height 100 --width 340 \
    --image dialog-question \
    --title "Power Options" \
    --button=Cancel:0 \
    --button=Restart:1 \
    --button=Shutdown:2 \
    --text "What would you like to do?" \
    --gtkrc ~/.config/polybar/scripts/power/popup.css

case "$?" in 
    "0")
        # Handle Cancel
        echo "you have chosen to cancel"
        exit 0
        ;;
    "1")
        # Handle Restart
        echo "you have chosen to Restart"
        exit 0
        ;;
    "2")
        # Handle Shutdown
        echo "you have chosen to Shutdown"
        exit 0
        ;;
    *)
        # Handle Unknown
        echo "window closed / unrecognized option"
        exit 1
        ;;
esac
