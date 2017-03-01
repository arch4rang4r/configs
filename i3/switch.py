#!/usr/bin/env python3

from sys import argv
from i3ipc import Connection

i3 = Connection()
ws = i3.get_tree().find_focused().workspace().num 
ws = ws % 10 + 1 if argv[1] == 'right' else (ws - 2) % 10 + 1
i3.command("workspace {}".format(ws))
