import traceback
import praw
from time import sleep
import sqlite3

#static values
USERNAME = "redirect-bot"
PASSWORD = ""
USER_AGENT = "script: Python redirect bot for mistyped subreddits: v0.1 (by /u/_guy_fawkes)"               
CLIENT_ID = "a4m_rl_g0ZXdLg"
CLIENT_SECRET = ""
access_token = {"access_token": "cWeR_jPSisffVghbI-YbqHbeTRI", "token_type": "bearer", "expires_in": 3600, "scope": "*"}
#account_info = {"is_employee": false, "features": {"live_happening_now": true, "adserver_reporting": true, "legacy_search_pref": true, "mobile_web_targeting": true, "ads_auction": true, "adzerk_do_not_track": true, "image_uploads": true, "show_user_sr_name": true, "whitelisted_pms": true, "show_rules_on_submit_page": {"owner": "commeng", "variant": "control_1", "experiment_id": 119}, "sticky_comments": true, "upgrade_cookies": true, "ads_prefs": true, "block_user_by_report": true, "ads_auto_refund": true, "orangereds_as_emails": true, "expando_events": true, "eu_cookie_policy": true, "utm_comment_links": true, "force_https": true, "activity_service_write": true, "mweb_rules_modal_on_submit": {"owner": "commeng", "variant": "control_2", "experiment_id": 158}, "do_not_track": true, "reddituploads_redirect": true, "outbound_clicktracking": true, "persistent_vote_a_a": {"owner": "content", "variant": "on", "experiment_id": 10}, "new_loggedin_cache_policy": true, "new_ads_styles": {"owner": "cheddar", "variant": "control_1", "experiment_id": 27}, "scroll_events": true, "https_redirect": true, "mweb_xpromo_interstitial_comments_ios": true, "pause_ads": true, "mweb_xpromo_listing_click_every_time": true, "programmatic_ads": true, "give_hsts_grants": true, "show_recommended_link": true, "mobile_native_banner": true, "mweb_xpromo_interstitial_comments_android": true, "screenview_events": true, "new_report_dialog": true, "moat_tracking": true, "subreddit_rules": true, "mobile_settings": true, "adzerk_reporting_2": true, "inbox_push": true, "ads_auto_extend": true, "interest_targeting": true, "post_embed": true, "mweb_rules_modal_on_comment": {"owner": "commeng", "variant": "control_1", "experiment_id": 159}, "mweb_xpromo_interstitial_frequency_android": {"owner": "channels", "variant": "control_2", "experiment_id": 152}, "adblock_test": true, "activity_service_read": true}, "is_suspended": false, "subreddit": null, "gold_expiration": null, "id": "16kyrp", "suspension_expiration_utc": null, "verified": false, "new_modmail_exists": null, "over_18": false, "is_gold": false, "is_mod": false, "has_verified_email": false, "has_mod_mail": false, "oauth_client_id": "a4m_rl_g0ZXdLg", "hide_from_robots": false, "link_karma": 1, "inbox_count": 1, "has_mail": true, "name": "redirect-bot", "created": 1490781063.0, "gold_creddits": 0, "created_utc": 1490752263.0, "in_beta": false, "comment_karma": 0}
KEYWORDS = []
KEYAUTHORS = []
REPLYSTRING = """You have the wrong subreddit. You want /r/personalfinance.

*I am a bot. This action was performed automatically. Contact /u/_guy_fawkes for more info.*"""
MAXPOSTS = 100
WAIT = 10
#plan to change WAIT and CLEANCYCLES once I know what I'm doing
CLEANCYCLES = 10

#honestly I have no clue why I'm connecting to a database
sql = sqlite3.connect('sql.db')
print('Loaded SQL Database')
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS oldposts(id TEXT)')
sql.commit()
print('Logging in...')
r = praw.Reddit(client_id = CLIENT_ID,
                            client_secret = CLIENT_SECRET,
                            user_agent = USER_AGENT,
                            username = USERNAME,
                            password = PASSWORD)


def reply():
    print('Searching /r/personalfiance. . . '
    fiance = r.subreddit('personalfiance')
    posts = list(fiance.get_comments(limit=MAXPOSTS))
    posts.reverse()
    for post in posts:
        #occurs every loop
        try:
            pauthor = post.author.name
        except AttributeError: #author is deleted
            continue
        if pauther.lower() == USERNAME.lower() or pauther.lower() == "_guy_fawkes":
            continue
            #don't reply to self
        #if KEYAUTHORS != [] and all(for auth in KEYAUTHORS auth.lower() != pauther)
        #this syntax doesn't work
            #continue
        cur.execute("SELECT * FROM oldposts WHERE ID=?", [pid])
        if cur.fetchone():
            #post in database
            continue
        cur.execute('INSERT INTO oldposts VALUES(?)', [pid])
        sql.commit()
        pbody = post.body.lower()
        print("Replying to {} by {}".format(pid, pauthor))
        try:
            post.reply(REPLYSTING)
        except praw.requests.exceptions.HTTPError:
            if praw.requests.exceptions.HTTPError.response.status_code == 403:
                print("403 FORBIDDEN - Is the bot banned from {}?").format(post.subreddit.display_name)

cycles = 0
while True:
    try:
        reply()
        cycles += 1
    except Exception:
        traceback.print_exc()
"""    if cycles >= CLEANCYCLES:
            print('Cleaning database')
            cur.execute('DELETE FROM oldposts WHERE id NOT IN (SELECT id FROM oldposts ORDER BY id DESC LIMIT ?)', [MAXPOSTS * 2])
            sql.commit()
            cycles = 0
not sure why I'd want to do this
"""
print("Waiting {} seconds.".format(WAIT))
sleep(WAIT)

"""def reply_finance(post):
    json = ("api_type" : "json",
                "text" : "You have the wrong subreddit. You want /r/personalfinance. *I am a bot. This message was performed automatically.*",
                "thing_id" : post)
            
"""
