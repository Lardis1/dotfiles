#!/bin/sh

connected_devices() {
    nmcli con show --active | tail -n +2 | tr -s ' '  | rev | cut -d ' ' -f 2 | rev
}

WIRELESS="wlan"
WIRED="eth"

if [ -z "$(connected_devices | grep $WIRELESS)" ];
then
    WIRELESS_COL="#F00"
    wireless_state='disconnected '
else
    WIRELESS_COL="#0F0"
    wireless_state='connected '
fi

if [ -z "$(connected_devices | grep $WIRED)" ];
then
    WIRED_COL="#F00"
    wired_state='disconnected '
else
    WIRED_COL="#0F0"
    wired_state='connected '
fi

WIRED_OUTPUT="  %{F$WIRED_COL}$wired_state%{F-}"
WIRELESS_OUTPUT="  %{F$WIRELESS_COL}$wireless_state%{F-}"
echo "$WIRED_OUTPUT $WIRELESS_OUTPUT"
