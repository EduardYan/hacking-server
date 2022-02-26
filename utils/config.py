"""
This module
have some functions for get
the configuration from the json file.

"""


from json import load


def get_configuration_object(PATH_CONFIG_FILE:str) -> dict:
    """
    Return a dictionary
    with the configuration
    of the file './config.json'

    """

    # path for the configuration file
    # PATH_CONFIG_FILE = './config.json'

    object = load(
        open(PATH_CONFIG_FILE)
    )


    return object


# configuration to use here
CONFIG = get_configuration_object('./config.json')
SCRIPTS_INFO = get_configuration_object('./scripts_info.json')
