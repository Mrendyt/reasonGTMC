import tweepy #import twitter authenticator 

# Google Sheets API setup
API_KEY = 'Insert your google api key'  # Replace with your Google Sheets API key
SPREADSHEET_ID = 'Insert your spreadsheet id' # Replace with your Google Sheets spreadsheet ID
RANGE_NAME = 'insert post range here ' # Replace with the range of cells you want to get

# Facebook API setup
PAGE_ACCESS_TOKEN = 'insert your page access token' # Replace with your Facebook Page access token
PAGE_ID = 'insert your page id' # Replace with your Facebook Page ID


# Twitter API setup
TWITTER_CONSUMER_KEY = 'insert your twitter consumer key' # Replace with your Twitter consumer key
TWITTER_CONSUMER_SECRET = 'insert your twitter consumer secret' # Replace with your Twitter consumer secret key
TWITTER_ACCESS_TOKEN = 'insert your twitter access token' # Replace with your Twitter access token
TWITTER_ACCESS_TOKEN_SECRET = 'insert your twitter access token secret' # Replace with your Twitter access token secret

def get_twitter_api():

# Set up and return Twitter API client.   
# Twitter API authentication
 auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
 auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)   
 return tweepy.API(auth) # Return the Twitter API client

