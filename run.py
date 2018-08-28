from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import logging
import logging.handlers

consumer_key = "lICzxWHsc4RFVhfTyN6M89PUy"
consumer_secret = "6Cq7FgKybBdoR3nfCrAmS2Grcmsj1End3vngmcCcXcIEqTUhqt"

access_token = "970197561133977600-oo0QpSiKjKYy0kRzkU8KOLDhvQwa8SV"
access_token_secret = "AYFVqyIhPiSRwJ6mWjfmiMhh6vKiNcOXvcrOdb32p0NuU"


class TweetListener(StreamListener):

    def __init__(self, api=None):
        super(TweetListener, self).__init__(api)
        self.logger = logging.getLogger('tweetlogger')

        statusHandler = logging.handlers.TimedRotatingFileHandler('status.log', when='H', encoding='bz2', utc=True)
        statusHandler.setLevel(logging.INFO)
        self.logger.addHandler(statusHandler)

        warningHandler = logging.handlers.TimedRotatingFileHandler('warning.log', when='H', encoding='bz2', utc=True)
        warningHandler.setLevel(logging.WARN)
        self.logger.addHandler(warningHandler)
        logging.captureWarnings(True);

        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.WARN)
        self.logger.addHandler(consoleHandler)

        self.logger.setLevel(logging.INFO)
        self.count = 0

    def on_data(self, data):
        self.count += 1
        self.logger.info(data)
        if self.count % 100 == 0:
            print("%d statuses processed" % self.count)
        return True

    def on_error(self, exception):
        self.logger.warn(str(exception))


if __name__ == '__main__':
    listener = TweetListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    while True:
        try:
            stream.sample(languages=['en'])
        except Exception as ex:
            print(str(ex))
            pass
