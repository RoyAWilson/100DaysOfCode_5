'''
To check internet connection speed
And report through to Twitter (now X)
Using classes to deal with setting up selenium
browser and extracting the speed.
Maybe also to set up the tweet and post to X
'''


from internet_speed_x_bot import InternetSpeedXBot

bot = InternetSpeedXBot()
bot.get_internet_speed()
bot.tweet_at_provider()
