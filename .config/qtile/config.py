# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod1"
terminal = "kitty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle Floating"),
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn("rofi -show drun -display-drun '>>> '"), desc="Launch rofi"),
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod , "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Multimedia Keys
    Key([], "xF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+ unmute"), desc="Inc. Volume"),
    Key([], "xF86AudioLowerVolume", lazy.spawn("amixer set Master 5%- unmute"), desc="Dec. Volume"),
    Key([], "xF86AudioMute", lazy.spawn("amixer -q set Master toggle"), desc="Mute Audio"),
    Key([], "xF86MonBrightnessUp", lazy.spawn("brightnessctl set +2%"), desc="Inc. Brightness"),
    Key([], "xF86MonBrightnessDown", lazy.spawn("brightnessctl set 2%-"), desc="Dec. Brightness"),

    
]

# Workspace/Groups Keybinds
groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
    
# Layouts
layouts = [
    layout.Columns(
        
        border_focus = "#000000",
        border_normal = "#555555",
        border_on_single = True, 
        border_width = 3,
        
        grow_amount = 10,
        
        margin_on_single = 10,
        margin = 8
        
    ),
    layout.Max(border_focus_stack=["#444444", "#000000"], border_width=3, margin=8),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Default props for widgets
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
# Screens
col1="2e2e2e"
col2="4e4e4e"
fsize=24
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background=None,
                    scale=0.7,
                    foreground='ff2222'
                ),
                widget.GroupBox(
                    highlight_method='line', # 'border', 'block', 'text', 'line'
                    active='ffffff',
                    inactive='404040',
                    margin_x=10,
                    padding_x=15,
                    
                    this_current_screen_border='ffffff',
                    this_screen_border='ffffff',
                    
                    other_current_screen_border='ff9e9e',
                    other_screen_border='9e9e9e',
                    
                    scroll=True,
                    rounded=False,
                    spacing=0,
                    
                    # invert_mouse_wheel=False,
                    # hide_unused=False,
                ),
                widget.Prompt(
                    prompt=">>>  ",
                    background='3e3e3e',
                    padding=10
                ),
                widget.WindowName(
                    max_chars=40,
                    padding=10
                ),
                
                
                widget.TextBox(
                    text='',
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.Net(
                    background=col1,
                    format="  W: {down}↓ {up}↑ ",
                    use_bits=False,
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.CPUGraph(
                    background=col2,
                    border_width=0,
                    frequency=0.5,
                    core='all',
                    graph_color='ff5e5e',
                    type='linefill',
                    line_width=2,
                    fill_color='5e995e'
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col2,
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.MemoryGraph(
                    background=col1,
                    border_width=0,
                    frequency=0.5,
                    graph_color='ff5e5e',
                    type='linefill',
                    line_width=2,
                    fill_color='5e995e'
                ),


                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.Battery(
                    background=col2,
                    battery="BAT0",
                    update_interval=5,
                    format="B: {percent}"
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col2,
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.TextBox(
                    text='   B: ',
                    background=col1,
                    foreground="#ffffff",
                    padding=0,
                ),
                widget.Backlight(
                    background=col1,
                    backlight_name="intel_backlight",
                    padding=5,
                    scroll=True,
                    step=5,
                    change_command="brightnessctl set {0}%"
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.TextBox(
                    text='   V: ',
                    background=col2,
                    foreground="#ffffff",
                    padding=0,
                ),
                widget.PulseVolume(
                    background=col2,
                    foreground="#ffffff",
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col2,
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.Clock(
                    background=col1,
                    format="%A, %B %d - %H:%M:%S %p"
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.QuickExit(
                    background=col2,
                    countdown_start=10,
                    countdown_format="{} seconds",
                    default_text=" shutdown "   
                ),
                # widget.Systray(),
                #
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background=None,
                    scale=0.7,
                    foreground='ff2222'
                ),
                widget.GroupBox(
                    highlight_method='line', # 'border', 'block', 'text', 'line'
                    active='ffffff',
                    inactive='404040',
                    margin_x=10,
                    padding_x=15,
                    
                    this_current_screen_border='ffffff',
                    this_screen_border='ffffff',
                    
                    other_current_screen_border='ff9e9e',
                    other_screen_border='9e9e9e',
                    
                    scroll=True,
                    rounded=False,
                    spacing=0,
                    
                    # invert_mouse_wheel=False,
                    # hide_unused=False,
                ),
                widget.Prompt(
                    prompt=">>>  ",
                    background='3e3e3e',
                    padding=10
                ),
                widget.WindowName(
                    max_chars=40,
                    padding=10
                ),
                
                
                widget.TextBox(
                    text='',
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.Net(
                    background=col1,
                    format="  W: {down}↓ {up}↑ ",
                    use_bits=False,
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.CPUGraph(
                    background=col2,
                    border_width=0,
                    frequency=0.5,
                    core='all',
                    graph_color='ff5e5e',
                    type='linefill',
                    line_width=2,
                    fill_color='5e995e'
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col2,
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.MemoryGraph(
                    background=col1,
                    border_width=0,
                    frequency=0.5,
                    graph_color='ff5e5e',
                    type='linefill',
                    line_width=2,
                    fill_color='5e995e'
                ),


                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.Battery(
                    background=col2,
                    battery="BAT0",
                    update_interval=5,
                    format="B: {percent}"
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col2,
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.TextBox(
                    text='   B: ',
                    background=col1,
                    foreground="#ffffff",
                    padding=0,
                ),
                widget.Backlight(
                    background=col1,
                    backlight_name="intel_backlight",
                    padding=5,
                    scroll=True,
                    step=5,
                    change_command="brightnessctl set {0}%"
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.TextBox(
                    text='   V: ',
                    background=col2,
                    foreground="#ffffff",
                    padding=0,
                ),
                widget.PulseVolume(
                    background=col2,
                    foreground="#ffffff",
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col2,
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.Clock(
                    background=col1,
                    format="%A, %B %d - %H:%M:%S %p"
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.QuickExit(
                    background=col2,
                    countdown_start=10,
                    countdown_format="{} seconds",
                    default_text=" shutdown "   
                ),
                # widget.Systray(),
                #
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background=None,
                    scale=0.7,
                    foreground='ff2222'
                ),
                widget.GroupBox(
                    highlight_method='line', # 'border', 'block', 'text', 'line'
                    active='ffffff',
                    inactive='404040',
                    margin_x=10,
                    padding_x=15,
                    
                    this_current_screen_border='ffffff',
                    this_screen_border='ffffff',
                    
                    other_current_screen_border='ff9e9e',
                    other_screen_border='9e9e9e',
                    
                    scroll=True,
                    rounded=False,
                    spacing=0,
                    
                    # invert_mouse_wheel=False,
                    # hide_unused=False,
                ),
                widget.Prompt(
                    prompt=">>>  ",
                    background='3e3e3e',
                    padding=10
                ),
                widget.WindowName(
                    max_chars=40,
                    padding=10
                ),
                
                
                widget.TextBox(
                    text='',
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.Net(
                    background=col1,
                    format="  W: {down}↓ {up}↑ ",
                    use_bits=False,
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.CPUGraph(
                    background=col2,
                    border_width=0,
                    frequency=0.5,
                    core='all',
                    graph_color='ff5e5e',
                    type='linefill',
                    line_width=2,
                    fill_color='5e995e'
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col2,
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.MemoryGraph(
                    background=col1,
                    border_width=0,
                    frequency=0.5,
                    graph_color='ff5e5e',
                    type='linefill',
                    line_width=2,
                    fill_color='5e995e'
                ),


                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.Battery(
                    background=col2,
                    battery="BAT0",
                    update_interval=5,
                    format="B: {percent}"
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col2,
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.TextBox(
                    text='   B: ',
                    background=col1,
                    foreground="#ffffff",
                    padding=0,
                ),
                widget.Backlight(
                    background=col1,
                    backlight_name="intel_backlight",
                    padding=5,
                    scroll=True,
                    step=5,
                    change_command="brightnessctl set {0}%"
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.TextBox(
                    text='   V: ',
                    background=col2,
                    foreground="#ffffff",
                    padding=0,
                ),
                widget.PulseVolume(
                    background=col2,
                    foreground="#ffffff",
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col2,
                    foreground=col1,
                    padding=0,
                    fontsize=fsize
                ),
                widget.Clock(
                    background=col1,
                    format="%A, %B %d - %H:%M:%S %p"
                ),
                
                
                widget.TextBox(
                    text='',
                    background=col1,
                    foreground=col2,
                    padding=0,
                    fontsize=fsize
                ),
                widget.QuickExit(
                    background=col2,
                    countdown_start=10,
                    countdown_format="{} seconds",
                    default_text=" shutdown "   
                ),
                # widget.Systray(),
                #
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


import os
import subprocess
from libqtile import hook

# startup_once to not include restarts 
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
    
    
# Event triggered on new window events
# makes all dialog boxes floating
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True


