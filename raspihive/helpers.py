"""
Helpers File
"""

import os
import platform
import distro

__OS_CMD__ = {
    'ubuntu': 'apt',
    'raspbian': 'apt',
    'fedora': 'dnf',
    'linuxmint': 'apt',
    'honeycomb': 'apt-get',
    'debian': 'apt-get'
}

__default_message__ = f'Your Platform is not supported. Please raise a request for your OS on the discord server, on `#help` channel.'


def os_parse(cmd):
    os_cmd = f"echo {__default_message__}"
    # Detect OS and set global commands.
    # if platform.system() == 'Linux':
    __OS_BASE__ = __OS_CMD__.get(distro.id(), None)

    if __OS_BASE__ is None:
        print(__default_message__)
        os_cmd = 'exit'
    else:
        if __OS_BASE__ != 'apt':
            os_cmd = cmd.replace('apt', __OS_BASE__)
    return os_cmd
