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
        'DPL': 'DPL',
        'CHR': 'Charging',
        'DIS': 'Discharging',
        'FULL': '',
    }
)
status.register('dpms')

status.run()
