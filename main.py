# coding=utf8

from Interfaces.layout import layout
from Interfaces.terminal import terminal

gui = True
if gui:
    layout()
else:
    terminal()
