#!/usr/bin/env python3
from splash.property import Style
from splash.property import Property

__author__ = 'Adrian-George Bostan <adi@fractor.ro>'
__email__ = 'adi@fractor.ro'

__version__ = '1.0.0'
__version_info__ = (1, 0, 0)

__url__ = 'https://github.com/adrg'
__description__ = 'Add a splash of color to your CLI apps'

# Attributes
reset = Property(0)
bold = Property(1)
dim = Property(2)
italic = Property(3)
underline = Property(4)
blink = Property(5)
fast_blink = Property(6)
reverse = Property(7)
hidden = Property(8)
crossed_out = Property(9)

# Foreground colors
black = Property(30)
red = Property(31)
green = Property(32)
yellow = Property(33)
blue = Property(34)
magenta = Property(35)
cyan = Property(36)
white = Property(37)

# Background colors
bg_black = Property(40)
bg_red = Property(41)
bg_green = Property(42)
bg_yellow = Property(43)
bg_blue = Property(44)
bg_magenta = Property(45)
bg_cyan = Property(46)
bg_white = Property(47)
