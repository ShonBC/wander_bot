import rospy
import wander_bot

if __name__ == '__main__':
    Bot = wander_bot.WanderBot()
    Bot.WanderBotPubSub()
    rospy.spin()