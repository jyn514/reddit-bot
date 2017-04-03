import traceback
import praw
from time import sleep
from basic_login import *
#basic_login logs into reddit without further commands
#doesn't change variable names

#static values
REPLYSTRING = """You have the wrong subreddit. You want /r/personalfinance.  
*I am a bot and this action was performed automatically. Contact u/_guy_fawkes for more info.*"""
MAXPOSTS = 100
WAIT = 600 #10 minute limit below a certain karma

#read comments in inbox
for comment in reddit.inbox.unread(mark_read=True):
    print(comment.author)
    print(comment)
#what can I say, I'm vain
print(reddit.user.karma())

fiance = reddit.subreddit('personalfiance')
def reply():
    print("Searching /r/{} . . .".format(fiance.display_name))
    for post in fiance.stream.submissions() :
        try:
            pauthor = post.author.name
            if pauthor != USERNAME and pauthor != "_guy_fawkes":
            #don't reply to self
                all_comments = post.comments.list()
                if "/r/personalfinance" in all_comments:
                    continue
                    #don't reply if someone else has already corrected it
                print("Replying. . . ")
                post.reply(REPLYSTRING) 
                print("Replied to a post.")
        except AttributeError: #author is deleted
            continue

while True:
    try:
        reply()
        cycles += 1
    except Exception:
        traceback.print_exc()
        SECRETS.close()
    print("Waiting {} seconds.".format(WAIT))
    sleep(WAIT)
    
