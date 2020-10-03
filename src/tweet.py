import sys
import tweepy



def tweeting(consumer_key, consumer_secret, my_access_token, my_access_token_secret, message):

    # Authentication
    my_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    my_auth.set_access_token(my_access_token, my_access_token_secret)
    my_api = tweepy.API(my_auth)
    my_api.update_status(message)

if __name__ == '__main__':

    if len(sys.argv) == 6:
        consumer_key = sys.argv[1]
        consumer_secret_key = sys.argv[2]
        my_access_token = sys.argv[3]
        my_access_token_secret = sys.argv[4]
        message = sys.argv[5]

        tweeting(consumer_key, consumer_secret_key, my_access_token, my_access_token_secret, message)
