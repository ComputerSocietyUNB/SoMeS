import os
from emoji import emojize
from mastodon import Mastodon


class MastodonBot:
    def __init__(self, config):
        Mastodon.create_app(
            'pytooterapp',
            api_base_url='https://mastodon.social',
            to_file='pytooter_clientcred.secret',
        )
        self.mastodon = Mastodon(
            client_id='pytooter_clientcred.secret',
            api_base_url='https://mastodon.social',
        )
        self.mastodon.log_in(
            config['email'], config['password'], to_file='pytooter_usercred.secret'
        )
        self.mastodon = Mastodon(
            access_token='pytooter_usercred.secret',
            api_base_url='https://mastodon.social',
        )

    def send_message(self, message):
        try:
            self.mastodon.toot(message)
            return 0
        except Exception as e:
            print(f'The following error was returned: {e.message}')
            return 1

    def send_image(self, image):
        try:
            media = self.mastodon.media_post(image)
            self.mastodon.status_post(
                emojize('Uploaded with :heart: via PyButler', use_aliases=True),
                media_ids=media,
            )
            return 0
        except Exception as e:
            print(f'The following error was returned: {e}')
            return 1
