import tweepy

consumer_key = "U7y4hUX2s7JP1TchG6fMYDfRw"
consumer_secret = "0xFKthgBTOAdl3I4GTQ7tBX4h99gao8gFMm248NcdO8WJ3efwv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth_url = auth.get_authorization_url()
print ('Visit this URL and authorize the app to use your Twitter account: ' + auth_url)
verifier = input('Type in the generated PIN: ').strip()
auth.get_access_token(verifier)

# Print out the information for the user
print ("consumer_key        ='%s'" % consumer_key)
print ("consumer_secret     ='%s'" % consumer_secret)
print ("access_token        ='%s'" % auth.access_token)
print ("access_token_secret ='%s'" % auth.access_token_secret)
