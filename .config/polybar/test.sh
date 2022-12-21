#!/bin/bash

export GTK2_RC_FILES=/tmp/gtkrc

cat <<-'EOSTYLEDEF' > ${GTK2_RC_FILES}

pixmap_path "/usr/share/backgrounds/cosmos/:/usr/share/backgrounds/nature/:/usr/share/backgrounds/scenery/:/usr/share/icons/gnome/scalable/actions"

style "windowStyle" {
    engine "pixmap" {
    image
      {
          function        = FLAT_BOX
          file            = "Garden.jpg"
          border          = { 0, 0, 0, 0 }
          stretch         = TRUE
          overlay_file    = "media-playback-pause.svg"
          overlay_stretch = FALSE
      }
  }
}

style "contentStyle" {
    fg[NORMAL]      = "brown"    # colour of the content text
    font_name="CM Roman CE Regular 10"
    GtkLabel::use-markup = TRUE
}

style "buttonStyle" {
    fg[NORMAL]      = "white"   # button label text colour
    fg[PRELIGHT]    = "yellow"  # button label text colour when mouse is over the button
    bg[NORMAL]      = "blue"    # button background colour
    bg[PRELIGHT]    = "navy"    # button background colour when mouse is over the button
    font_name       = "Fixed Italic 14"
    xthickness      = 6         # adds "border" on either side of the button
    ythickness      = 6         # adds "border" above and below the button
}

## the paths below apply the named styles to the yad dialog text and button

# gives the entire dialogue background colour
widget_class "<GtkWindow>" style "windowStyle"

# give the Button background colour
widget_class "<GtkWindow><GtkVBox><GtkContainer><GtkButton>" style "buttonStyle"

# gives the button text colour
widget_class "<GtkWindow><GtkVBox><GtkContainer><GtkButton><GtkContainer><GtkHBox><GtkLabel>" style "buttonStyle"

# gives the dialog text colour
widget_class "<GtkWindow><GtkVBox><GtkHBox><GtkVBox><GtkLabel>" style "contentStyle"

EOSTYLEDEF

yad \
    --center --width=400 --image="gtk-dialog-authentication" --window-icon="gtk-dialog-authentication" \
    --title="Succesful connection" \
    --text="Succesfully <b>connected</b> to <span size='large' color='black'>database</span> schema" \
    --button=" Dismiss!gtk-ok!Dismiss this dialogue:0"

EODECK