# github-tweeter-bot
If you are like me, and hate getting on Twitter every single day, but you want to get your newer projects out there then this is may help. This script is designed to post
about your latest repos, but it can be edited to do way more. This uses the Github API and Twitter API.

# Set Up
1. Before you can run this on your machine, you need to make a Twitter Developer account. Just sign in [here](https://developer.twitter.com/en/portal/dashboard) if you already have an account
2. Once you sign in, you should be about to apply for a developer key (it's free and application is usually approved pretty fast)
3. Once you get approved, you need to get your Consumer Keys, and Authentication Tokens and add them to the main.py file (replace mine).
4. Make sure you installed all packages with ```pip install -r requirements.txt``` in the shell of whatever directory you downloaded the project in. 
5. Changes that should be made are mentioned in the comments of main.py file

# Resources
- [Tweepy](https://www.tweepy.org/) The python package I used to interact with the twitter API
- [Twitter API docs](https://developer.twitter.com/en/docs)
- [Github API](https://docs.github.com/en/rest)

# To do
- add more functions?
- add testing

# Notes
This is made to be an automated script, so a Windows app like Task Scheduler should be able to run it whenever (if you have the computer on whenever it's suppose to run I think)
[Here](https://datatofish.com/python-script-windows-scheduler/) is a good guide on how to turn script into a batch file and automating it with Task Scheduler for Windows PC.
I have also included my batch file as a reference.
