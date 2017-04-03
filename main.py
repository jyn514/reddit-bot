import traceback
import praw
from time import sleep

#static values
USERNAME = "redirect-bot"
PASSWORD = "JyhwesNhtgDYElaHXYmrevv2QLZH1kSpggRXhvjRbMtfhbTcjdosZXugerHZQKqt"
USER_AGENT = "script: Python redirect bot for mistyped subreddits: v0.1 (by /u/_guy_fawkes)"               
CLIENT_ID = "a4m_rl_g0ZXdLg"
CLIENT_SECRET = "TdYWoWZlRHUk_B9v281dHDx4W3M"
access_token = {"access_token": "cWeR_jPSisffVghbI-YbqHbeTRI", "token_type": "bearer", "expires_in": 3600, "scope": "*"}
#account_info = {"is_employee": false, "features": {"live_happening_now": true, "adserver_reporting": true, "legacy_search_pref": true, "mobile_web_targeting": true, "ads_auction": true, "adzerk_do_not_track": true, "image_uploads": true, "show_user_sr_name": true, "whitelisted_pms": true, "show_rules_on_submit_page": {"owner": "commeng", "variant": "control_1", "experiment_id": 119}, "sticky_comments": true, "upgrade_cookies": true, "ads_prefs": true, "block_user_by_report": true, "ads_auto_refund": true, "orangereds_as_emails": true, "expando_events": true, "eu_cookie_policy": true, "utm_comment_links": true, "force_https": true, "activity_service_write": true, "mweb_rules_modal_on_submit": {"owner": "commeng", "variant": "control_2", "experiment_id": 158}, "do_not_track": true, "reddituploads_redirect": true, "outbound_clicktracking": true, "persistent_vote_a_a": {"owner": "content", "variant": "on", "experiment_id": 10}, "new_loggedin_cache_policy": true, "new_ads_styles": {"owner": "cheddar", "variant": "control_1", "experiment_id": 27}, "scroll_events": true, "https_redirect": true, "mweb_xpromo_interstitial_comments_ios": true, "pause_ads": true, "mweb_xpromo_listing_click_every_time": true, "programmatic_ads": true, "give_hsts_grants": true, "show_recommended_link": true, "mobile_native_banner": true, "mweb_xpromo_interstitial_comments_android": true, "screenview_events": true, "new_report_dialog": true, "moat_tracking": true, "subreddit_rules": true, "mobile_settings": true, "adzerk_reporting_2": true, "inbox_push": true, "ads_auto_extend": true, "interest_targeting": true, "post_embed": true, "mweb_rules_modal_on_comment": {"owner": "commeng", "variant": "control_1", "experiment_id": 159}, "mweb_xpromo_interstitial_frequency_android": {"owner": "channels", "variant": "control_2", "experiment_id": 152}, "adblock_test": true, "activity_service_read": true}, "is_suspended": false, "subreddit": null, "gold_expiration": null, "id": "16kyrp", "suspension_expiration_utc": null, "verified": false, "new_modmail_exists": null, "over_18": false, "is_gold": false, "is_mod": false, "has_verified_email": false, "has_mod_mail": false, "oauth_client_id": "a4m_rl_g0ZXdLg", "hide_from_robots": false, "link_karma": 1, "inbox_count": 1, "has_mail": true, "name": "redirect-bot", "created": 1490781063.0, "gold_creddits": 0, "created_utc": 1490752263.0, "in_beta": false, "comment_karma": 0}
KEYWORDS = []
KEYAUTHORS = []
REPLYSTRING = """You have the wrong subreddit. You want /r/personalfinance.

*I am a bot and this action was performed automatically. Contact u/_guy_fawkes for more info.*"""
MAXPOSTS = 100
print('Logging in . . . ')
reddit = praw.Reddit(client_id = CLIENT_ID,
                            client_secret = CLIENT_SECRET,
                            user_agent = USER_AGENT,
                            username = USERNAME,
                            password = PASSWORD)
WAIT = 10*60
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
                post.reply(REPLYSTRING) 
                print("Replied to a post. . . ")
        except AttributeError: #author is deleted
            continue

while True:
    try:
        reply()
        cycles += 1
    except Exception:
          traceback.print_exc()
          while True:
              print("Waiting for a command. Type 'break' to resume.")
              exec(input())
    print("Waiting {} seconds.".format(WAIT))
    sleep(WAIT)
