![logo](https://raw.githubusercontent.com/adrg/adrg.github.io/master/assets/projects/splash-py/logo.png)
======
[![License: MIT](http://img.shields.io/badge/license-MIT-red.svg?style=flat-square)](http://opensource.org/licenses/MIT)

Splash is a small Python 3 package which gives you the ability to style
terminal output.  It provides a set of types and functions to allow coloring
and styling of output text. It can be useful in CLI applications or logging
libraries.

The core of the package is the **Property** class. A property represents either
a color (foreground or background) or a text attribute (bold, underline, etc.).
The package also defines the **Style** class which is just a collection of
properties. Styles provide the ability to store a group of properties and
reuse them when needed. From a coding standpoint, there is no difference
between using a property and a style.

This package is a port of the [Splash](https://github.com/adrg/splash)
library, originally written for the Go language.

## Installation
```sh
git clone https://github.com/adrg/splash-py.git

# With distutils
cd splash-py
python3 setup.py install

# With pip3
pip3 install splash-py
```

## Usage

#### Properties
```python
#!/usr/bin/env python3
import splash

reset = splash.reset

# Using text attributes
print(splash.bold, 'To boldly go ', reset, sep='', end='')
print(splash.underline, 'where no man ', reset, ' ', sep='')
print(splash.reverse, 'has gone before\n', reset, sep='')

# Using foreground and background colors
print(splash.red, 'Roses are red', reset, sep='')
print(splash.bg_green, "Here's something new:", reset, sep='')
print(splash.magenta, 'Violets are violet', reset, sep='')
print(splash.bg_blue, 'Not freaking blue!\n', reset, sep='')

# Combining colors with text attributes
print(splash.bold, splash.green, 'Hint: lamp', reset, sep='')
print(splash.red, splash.bg_blue, 'Hint: famous plumbler\n', reset, sep='')

# Using formatting
print(splash.bg_yellow.format('Yellow there!'))
print('{0}The Wicked Witch of The West{1}'.format(splash.green, reset))
print(splash.bold.format('{0}{1}', splash.blue, "Don't feel blue!"))
```
Output:
![properties output](https://raw.githubusercontent.com/adrg/adrg.github.io/master/assets/projects/splash-py/properties.png)

#### Styles
```python
#!/usr/bin/env python3
import splash

# Using styles
info = splash.Style(splash.green, splash.bold)
warning = splash.Style(splash.yellow)
err = splash.Style(splash.red, splash.bold)
critical = splash.Style(splash.bold, splash.yellow, splash.bg_red)

print(info, "INFO: I'm so informative", splash.reset, sep='')
print(warning, 'WARNING: You should not ignore me', splash.reset, sep='')
print(err.format("ERROR: You can't say I didn't warn you"))
print(critical.format('{0} {1}\n', 'CRITICAL:', 'This should be good'))

# Parsing styles
# Format: foreground:background+attributes
attr = splash.Style.parse('+b')
print(attr.format('Bold'))

attrs = splash.Style.parse('+bu')
print(attrs.format('Bold, underline'))

fg = splash.Style.parse('yellow')
print(fg.format('Yellow foreground'))

bg = splash.Style.parse(':red')
print(bg.format('Red background'))

fgAttr = splash.Style.parse('green+b')
print(fgAttr.format('Green foreground, bold'))

bgAttr = splash.Style.parse(':magenta+u')
print(bgAttr.format('Magenta background, underline'))

fgBg = splash.Style.parse('cyan:red')
print(fgBg.format('Cyan foreground, red background'))

fgBgAttr = splash.Style.parse('yellow:blue+b')
print(fgBgAttr.format('Yellow foreground, blue background, bold'))

fgBgAttrs = splash.Style.parse('red:green+br')
print(fgBgAttrs.format('Red foreground, green background, bold, reverse'))
```
Output:
![styles output](https://raw.githubusercontent.com/adrg/adrg.github.io/master/assets/projects/splash-py/styles.png)

## Property reference
![property reference](https://raw.githubusercontent.com/adrg/adrg.github.io/master/assets/projects/splash-py/colors.png)

**Foreground colors**
```
black red green yellow blue magenta cyan white
```

**Background colors**
```
bg_black bg_red bg_green bg_yellow bg_blue bg_magenta bg_cyan bg_white
```

**Text attributes**
```
reset bold dim italic underline blink fast_blink reverse hidden crossed_out
```

 * Note: unfortunately not all text attributes are supported in all terminals.

## Style parsing reference

**Format**
```
foreground:background+attributes
```

**Colors**
```
black red green yellow blue magenta cyan white
```

**Text attributes**
```
b     - bold
d     - dim
i     - italic
u     - underline
B     - blink
f     - fast_blink
r     - reverse
h     - hidden
c     - crossed_out
reset - reset
```

## References
For more information see the [ANSI escape sequences](http://en.wikipedia.org/wiki/ANSI_escape_code#Colors)
and [Terminal colors and formatting](http://misc.flogisoft.com/bash/tip_colors_and_formatting)

## License
Copyright (c) 2014 Adrian-George Bostan.

This project is licensed under the [MIT license](http://opensource.org/licenses/MIT). See LICENSE for more details.
