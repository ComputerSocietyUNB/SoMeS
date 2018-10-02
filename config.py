import os
from configparser import ConfigParser


def config(section='MAIN', filename='config.ini'):
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
        config_information = f'[{section}]\nconsumer_key=\nconsumer_secret=\n'
        with open(f'new_{filename}.ini', mode='w') as config_file:
            config_file.write(config_information)
        raise FileNotFoundError
