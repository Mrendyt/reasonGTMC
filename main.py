import requests # Import the 'requests' library for making HTTP requests to APIs.
import schedule # Import the 'schedule' library for scheduling tasks to run at specific intervals or times.
import time # Import the 'time' library for handling time-related tasks, such as pausing execution.
from api import API_KEY, SPREADSHEET_ID, RANGE_NAME, PAGE_ACCESS_TOKEN, PAGE_ID, get_twitter_api

#google sheets API setup url
GOOGLE_SHEETS_URL = f'https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{RANGE_NAME}?key={API_KEY}'

#Facebook API setup url
FACEBOOK_GRAPH_API_URL = f"https://graph.facebook.com/v12.0/{PAGE_ID}/feed"

# Twitter API setup
twitter_api = get_twitter_api()

def get_articles():

    # Fetches data from Google Sheets.
    #Returns a list of values from the specified range.
    try:
        response = requests.get(GOOGLE_SHEETS_URL)  # Make a GET request to the Google Sheets API
        if response.status_code == 200: #check if successful
            data = response.json()
            return data.get('values', []) # Return the values from the sheet
        else:
            print("Failed to fetch data from Google Sheets:", response.json()) #print an error if failed
            return []
    except Exception as e:
        print("Error fetching data from Google Sheets:", e)
        return []

def post_to_facebook(message):

    #Posts a message to Facebook using the Graph API.
    try:
        response = requests.post(
            FACEBOOK_GRAPH_API_URL, # Fetch URL from above 
            data={
                'message': message, # Message to be posted
                'access_token': PAGE_ACCESS_TOKEN
            }
        )
        if response.status_code == 200: # Check if the post was successful
            print("Post published successfully on Facebook!")
        else:
            print("Failed to post on Facebook:", response.json()) # Print error if the post failed
    except Exception as e:
        print("Error posting to Facebook:", e) # Print any exception that occurs


def post_to_twitter(message):
    # Posts a message to Twitter using Tweepy.
    try:
        twitter_api.update_status(message) # Update status with the message
        print("Tweet published successfully on Twitter!")
    except Exception as e:
        print("Error posting to Twitter:", e) # Print any exception that occurs


def main():

    #Main function to fetch articles and post to Facebook.

    articles = get_articles() # Fetch articles from Google Sheets
    if articles: 
        # Check if there are any articles
        topic = articles[0][0] # Get the topic from the first row
        url = articles[0][1] # Get the URL from the first row
        post_text = f"Check out this article on {topic}: {url}" # Create the post text

        
        # Post immediately (or you can schedule it)
        post_to_facebook(post_text)

        # Schedule the post for 8:00 AM daily
        schedule.every().day.at("08:00").do(post_to_facebook, post_text)

         # Run the scheduling loop
        while True:
            schedule.run_pending()# Run any pending scheduled tasks
            time.sleep(1) # Wait for 1 second before checking again
    else:
        print("No articles found.") # Print a message if no articles are found


if __name__ == '__main__':
    main() # Run the main function when the script is executed
