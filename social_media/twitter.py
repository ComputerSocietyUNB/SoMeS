import tweepy
from emoji import emojize


class TwitterBot:
    def __init__(self, config):
        self.auth = tweepy.OAuthHandler(
            config['consumer_key'], config['consumer_secret']
        )
        self.auth.set_access_token(
            config['access_token'], config['access_token_secret']
        )
        self.api = tweepy.API(self.auth)

    def send_message(self, message):
        try:
            self.api.update_status(message)
            return 0
        except Exception as e:
            print(f'The following error was returned: {e}')
            return 1

    def send_image(self, image):
        try:
            self.api.update_with_media(
                image, emojize('Uploaded with :heart: via PyButler', use_aliases=True)
            )
            return 0
        except Exception as e:
            print(f'The following error was returned: {e}')
            return 1
