import os
import importlib
from os import listdir
from os.path import isfile, join
from time import strftime
from config import config


def main():
    available_medias = config()
    bots = {}
    for media in available_medias:
        if available_medias[media] == 'true':
            module = importlib.import_module(f'social_media.{media}')
            media_obj = f'{media.title()}Bot'
            bots[media] = dict(config(section=media.upper()))
            bots[media]['bot'] = getattr(module, media_obj)(bots[media])
            # bots[media]['bot'].send_message(get_message_file())
            bots[media]['bot'].send_image(get_image_file())


def get_message_file(msg_file='msg.txt'):
    try:
        now = strftime('%Y_%m_%d_%H%M')
        msg_file = f'{os.getcwd()}/message/{msg_file}'
        old_msg_file = f'{os.getcwd()}/message/sent/msg_{now}.txt'
        with open(msg_file, mode='r') as message:
            os.rename(msg_file, old_msg_file)
            return message.read()
    except Exception as e:
        print(e)
        exit()

def get_image_file():
    mypath = f'{os.getcwd()}/image'
    all_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for img_file in all_files:
        return f'{mypath}/{img_file}'


if __name__ == '__main__':
    main()
