import requests
import tweepy
import config

# creates an object with my keys in them
# replace each parameter with your on Twitter Dev keys
client = tweepy.Client(bearer_token=config.bearer_token, consumer_key=config.consumer_key,
                       consumer_secret=config.consumer_secret, access_token=config.access_token, access_token_secret=config.access_token_secret)


# Gets the URL for my github repo
# replace with your own
url = config.url
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
response = r.json()


# parses all of my repos and gets the latest one
def get_latest_repo_date():
    latest = response[0]['created_at']
    for x in range(len(response)):
        if latest < response[x]['created_at']:
            latest = response[x]['created_at']
    return latest

# matches the date of the latest repo to get all the data about the repo
def get_latest_repo():
    latest = get_latest_repo_date()
    for repo in response:
        if latest == repo['created_at']:
            latest_repo = repo

    return latest_repo

# gets repo info and tweets the formatted tweet
def tweet_about_latest_new_repo():
    repo = get_latest_repo()

    # change to fit what format you want
    current_tweet = f"Hi, I'm Dejun's Github Assistant and he created another repo!\nFeel free to look around or maybe contribute a few lines of code!\n\nName: {repo['name']}\nDescription: {repo['description']}\nMost Used Language: {repo['language']}\nURL: {repo['html_url']}"

    #checks the recent tweets to make sure name, description, and language are not the same as current tweet (replace config.id with your twitter id)
    tweets = client.get_users_tweets(config.id, exclude=['retweets', 'replies'])
    for tweets in tweets.data:
        if str(repo['name']) in tweets.text and str(repo['description']) in tweets.text and str(repo['language']) in tweets.text:
            return
        
    client.create_tweet(text=current_tweet)

if __name__ == "__main__":
    tweet_about_latest_new_repo()
