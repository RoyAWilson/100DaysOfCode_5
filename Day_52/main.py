"""_summary_
To login to Instagram and navigate to a followd account,
then to follow that account's followers.
"""
from my_insta_follower import InstaFollower

bot = InstaFollower()

bot.login()
bot.find_followers()
# bot.follow()
