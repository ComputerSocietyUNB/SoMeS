import os
from configparser import ConfigParser


def config(section='MEDIA', filename='config.ini'):
    """
    Function to retrieve all informations from token file.
    Usually retrieves from config.ini
    """
    try:
        FILE_PATH = f'{str(os.getcwd())}/{filename}'
        config = ConfigParser()
        with open(FILE_PATH) as config_file:
            config.read_file(config_file)
        return(config[section])
    except FileNotFoundError:
        print('Configure file config.ini using config_sample.ini structure')
        raise FileNotFoundError
