import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key        = 'U7y4hUX2s7JP1TchG6fMYDfRw'
consumer_secret     = '0xFKthgBTOAdl3I4GTQ7tBX4h99gao8gFMm248NcdO8WJ3efwv'
access_token        = '394350512-9JoZwMbygGt3QQPB2qld9cndIweujpxwS6jmC4G7'
access_token_secret = 'fgx4GAD50f9wMPjhvpSB9PuD9jRq9zFYQck5sWVlKobr2'

#OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Creation of the actual interface, using authentication
api = tweepy.API(auth)

#Send the tweet
message = 'This is a test'
api.update_status(message)
