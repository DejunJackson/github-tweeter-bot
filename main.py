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

# defines the number of current repos you started at as of now and the number of repos you have at time of request
base_num_of_repos = 27
current_num_of_repos = len(response)

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

# if you have more tweets than the base number, it gets the latest tweet and tweets stats about it
def tweet_about_latest_new_repo():
    if current_num_of_repos > base_num_of_repos:
        repo = get_latest_repo()
    client.create_tweet(
        text=f"Hi, I'm Dejun's Github Assistant and he created another repo!\nFeel free to look around or maybe contribute a few lines of code!\n\nName: {repo['name']}\nDescription: {repo['description']}\nMost Used Language: {repo['language']}\nURL: {repo['html_url']}")


if __name__ == "__main__":
    tweet_about_latest_new_repo()
