#!/usr/bin/env python3

_ATTRIBUTES = {
    'b': 1,
    'd': 2,
    'i': 3,
    'u': 4,
    'B': 5,
    'f': 6,
    'r': 7,
    'h': 8,
    'c': 9
}

_COLORS = {
    'black': 0,
    'red': 1,
    'green': 2,
    'yellow': 3,
    'blue': 4,
    'magenta': 5,
    'cyan': 6,
    'white': 7
}


def _property_str(value):
    return '\u001b[{0}m'.format(value)


def _style_str(properties):
    return ''.join(map(str, properties))


class Property:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return _property_str(self.value)

    def __repr__(self):
        return _property_str(self.value)

    def __format__(self, fmt):
        return _property_str(self.value)

    def format(self, fmt, *args, **kwargs):
        fmt = _property_str(self.value) + fmt + _property_str(0)
        return fmt.format(*args, **kwargs)


class Style:
    def __init__(self, *properties):
        self.properties = [property for property in properties]

    def __str__(self):
        return _style_str(self.properties)

    def __repr__(self):
        return _style_str(self.properties)

    def __format__(self, format_string):
        return _style_str(self.properties)

    def format(self, fmt, *args, **kwargs):
        fmt = _style_str(self.properties) + fmt + _property_str(0)
        return fmt.format(*args, **kwargs)

    @staticmethod
    def parse(style_format):
        style = Style()

        style_format = style_format.replace(' ', '').strip()
        if not style_format:
            return style

        if style_format == 'reset':
            style.properties.append(Property(0))
            return style

        tokens = style_format.split('+')
        if len(tokens) > 1:
            for token in tokens[1]:
                attr = _ATTRIBUTES.get(token, None)
                if attr is not None:
                    style.properties.append(Property(attr))

        tokens = tokens[0].lower().split(':')
        foreground = _COLORS.get(tokens[0], None)
        if foreground is not None:
            style.properties.append(Property(30 + foreground))

        if len(tokens) > 1:
            background = _COLORS.get(tokens[1], None)
            if background is not None:
                style.properties.append(Property(40 + background))

        return style
