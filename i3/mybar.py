#!/usr/bin/env python3

from i3pystatus import Status

status = Status()

status.register(
    'clock',
    format = '%r %F'
)
status.register('pulseaudio')
status.register(
    'battery',
    format = 'BAT: [{status} ]{percentage:.2f}%[ {remaining} remaining]',
    not_present_text = '',
    status = {
        'DPL': 'DPL', # What actually is this? I don't think I've ever seen it show up
        'CHR': 'Charging',
        'DIS': 'Discharging',
        'FULL': '',
    }
)
status.register(
    'dpms',
    format = 'DPMS: on', # Workaround for #537
    format_disabled = 'DPMS: off'
)
status.register('window_title')

status.run()
