#!/usr/bin/env python3
import splash
from distutils.core import setup

LONG_DESCRIPTION = '''
Splash is a small package which gives you the ability to style terminal output.
It provides a set of types and functions to allow coloring and styling of
output text. It can be useful in CLI applications or logging libraries.
'''

setup(
    name='splash-py',
    version=splash.__version__,
    author=splash.__author__,
    author_email=splash.__email__,
    maintainer=splash.__author__,
    maintainer_email=splash.__email__,
    url=splash.__url__,
    download_url=splash.__url__,
    description=splash.__description__,
    long_description=LONG_DESCRIPTION,
    license='LICENSE',
    packages=['splash'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
