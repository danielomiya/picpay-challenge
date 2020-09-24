"""
Wrapper around configparser to retrieve info from config files

Author: Daniel Omiya
"""

from configparser import ConfigParser


class ConfigLoader:
    """
    Loads configurations from a config file
    """

    def __init__(self):
        """
        ConfigLoader constructor
        """
        self._config = ConfigParser()


    def add_config(self, path):
        """
        Adds a config to this instance

        Args:
            path (str): path to config file
        """
        self._config.read(path)
        return self


    def get_string(self, key, default=None, section='DEFAULT'):
        """
        Gets a string from config file.

        Args:
            key (str): key to search for on config
            default (any, optional): value to return if key doesn't exist
            section (str, optional): section where key is in. Defaults to 'DEFAULT'.

        Returns:
            str: string value
        """
        return self._config.get(section, key, fallback=default)
