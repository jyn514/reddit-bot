#run from python shell or import directly 

import praw

SECRETS = open("./passwords.txt")
USERNAME = "redirect-bot"
PASSWORD = SECRETS.readline()
USER_AGENT = "script: Python redirect bot for mistyped subreddits: v0.1 (by /u/_guy_fawkes)"               
CLIENT_ID = "a4m_rl_g0ZXdLg"
CLIENT_SECRET = SECRETS.readline()

print('Logging in . . . ')
reddit = praw.Reddit(client_id = CLIENT_ID,
                            client_secret = CLIENT_SECRET,
                            user_agent = USER_AGENT,
                            username = USERNAME,
                            password = PASSWORD)
print("Logged in.")
