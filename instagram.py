from instabot import Bot
import sys
try:

     bot = Bot()
     bot.login(username="pythonhub123",password='Python123')
     bot.follow("jainkratiiii")
     bot.unfollow('bbcnews')
     bot.follow_users(["jainkratiiii","motivationuv"])
     bot.unfollow_non_followers()
     bot.upload_photo("pythonn.jpg",caption="hey")
     bot.send_message("i like python",["unitednations","bbcnews"])
     followers=bot.get_user_followers("pythonhub123")
     for follower in followers:
      print(bot.get_user_info(follower))



except Exception:
      print(sys.exc_info()[0])