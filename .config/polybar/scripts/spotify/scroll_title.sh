#!/bin/bash

zscroll -l 35 \
        --before-text "  " \
        --delay 0.3 \
		--match-command "`dirname $0`/full_title.sh --status" \
		--match-text "Playing" "--scroll 1" \
		--match-text "Paused" "--scroll 0" \
		--update-check true "`dirname $0`/full_title.sh" &

wait
