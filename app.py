# Python TwitterBot
# Author: Iden Morisha
# Username: @idenmorisha (Facebook, Twitter, Instagram)
# Email: identumu@gmail.com
# Licence: MIT
# Run pip install selenium in the terminal to install selinium
# Throught the entire app; you will find time.sleep(some number)
# time.sleep() is the set time to execute the given functions
# like_tweet() on line 52 is a function for liking Tweets
# bot.execute_script on line 57 will scroll through the search result so you dont have to manually do that
# for link in links: loops through all the results
# Replace 'youremail@example.com', 'yourpassword' on line 72 with your real login details
# Replace 'Insert your hashtag value' on line 74 with your prefered hashtag without a "#symbol"
# For support; email me at identumu@gmail.com
# ##################################################################################
# ##################################################################################

from selenium import webdriver 

from selenium.webdriver.common.keys import Keys
import time

# Create a twitter class which will be called back later
class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password

        # create an instance for the bot
        self.bot = webdriver.Firefox()


    # Create a login class
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')

        # pause the app for 3 seconds using time.sleep(3)
        # If you have a slow internet, you can change and increase the execution time
        time.sleep(5)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')

        # clear email and passwords that may be in the forms
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(keys.RETURN)
        time.sleep(3)

    # hashtag search function
    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q'+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            tweets = bot.find_element_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
        for link in links:
            bot.get('https://twitter.com' + link)
            try:
                bot.find_element_by_class_name('HeartAnimation').click()

                # use atleast 10sec as min execution time so that twitter wont detect spam
                time.sleep(15)
            except Exception as ex:
                    time.sleep(60)


ed = TwitterBot('email@example.com', 'password')
ed.login()
ed.like_tweet('webdevelopment')
