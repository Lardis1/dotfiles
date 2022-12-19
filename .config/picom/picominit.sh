# Check for existing proccess
if ps -A | grep picom; then
	killall -q picom
fi

# Start Picom
sleep 0.8
picom --experimental-backends --config $HOME/.config/picom/picom.conf

