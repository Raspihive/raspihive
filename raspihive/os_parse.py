"""
Under Development. Not ready for production yet.
"""

import os
import platform
import distro


class OSParser():
    """
    Parse commands for your Operating System.
    """

    def __init__(self):
        print("Parsing OS commands for Raspihive.")
        self.__OS_CMD__ = {
            'ubuntu': 'apt',
            'raspbian': 'apt',
            'fedora': 'dnf',
            'linuxmint': 'apt',
            'honeycomb': 'apt-get',
            'debian': 'apt-get',
            'manjaro': 'pacman'
        }
        self.__default_message__ = f'Your Platform is not supported. Please raise a request for your OS on the discord server, on `#help` channel.'

    def parse(self, cmd):
        """
        The Parser of Parser.
        To be used to identify and call the respective parser function.
        """
        print("cmd:", cmd)
        os = detect_os_pm(cmd)
        print("detect os:")
        os_cmd = f"echo {self.__default_message__}"
        if os_pm == 'apt':
            os_cmd = parse_for_apt(cmd)
        elif os_pm == 'apt-get':
            os_cmd = parse_for_apt_get(cmd)
        elif os_pm == 'dnf':
            os_cmd = parse_for_dnf(cmd)
        elif os_pm == 'pacman':
            os_cmd = parse_for_pacman(cmd)
        return os_cmd

    def detect_os_pm(self, cmd):
        os_pm = self.__OS_CMD__.get(distro.id(), None)
        return os_pm

    def parse_for_apt(self, cmd):
        """
        Parse for apt commands.
        Supported distros:
        - Ubuntu
        - Raspbian
        - LinuxMint
        """
        print("cmd for apt:", cmd)
        # Assuming all default cmd are in apt.
        return cmd

    def parse_for_apt_get(self, cmd):
        """
        Parse for apt commands.
        Supported distros:
        - Debian
        - HoneyComb
        """
        print("cmd for apt_get:", cmd)
        return cmd.replace("apt", "apt-get")

    def parse_for_dnf(self, cmd):
        """
        Parse for dnf commands.
        Supported distros:
        - Fedora
        """
        print("cmd for dnf:", cmd)
        return cmd.replace("apt", "dnf")

    def parse_for_pacman(self, cmd):
        """
        Parse for pacman.
        Supported distros:
        - Manjaro
        - Arch Linux
        """
        print("cmd for pacman:", cmd)
        os_cmd = cmd.replace("apt", "pacman")
        return os_cmd
