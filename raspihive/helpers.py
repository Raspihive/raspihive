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
    'honeycomb': 'apt-get'
}
__OS_BASE__ = __OS_CMD__[distro.id()]
__default_message__ = f'Your Platform is not supported. Please get in touch with us at '


def os_parse(cmd):
    os_cmd = f"echo {__default_message__}"
    # Detect OS and set global commands.
    # if platform.system() == 'Linux':

    if __OS_BASE__ != 'apt':
        os_cmd = cmd.replace('apt', __OS_BASE__)
    return os_cmd
