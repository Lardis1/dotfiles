#!/bin/sh

artist_and_title() {
    title=$(spotifyctl status --format '%title% - %artist%' \
        --max-length 45 --max-artist-length 20 \
        --max-title-length 35 --trunc '...')
    echo "  $title"
}

spotify_state() {
    delimeter='application.name = "Spotify"'
    pacmd list-sink-inputs | \
        tr '\n' ' '  | \
        sed 's/\s\s*/ /g' | \
        sed "s/${delimeter}.*/${delimeter}/" | \
        sed 's/\(.*\)state: //' | \
        cut -d ' ' -f 1
}

play_pause() {
    state=$(spotify_state)
    if [ "$state" = "RUNNING" ];
    then
        echo " "
    else
        echo " "
    fi
}


if [ "$1" = "title" ];
then
    artist_and_title
elif [ "$1" = "playpause" ];
then
    play_pause
fi