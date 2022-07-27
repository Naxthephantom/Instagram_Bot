
#First of you'll need to install instapy
#python -m pip install instapy

from instapy import Instapy

session = Instapy(username = " nax.d.phantom ", password = " Echezona2005 ")      #Replace the username and password with yours
session.login()
                                                                                  #This two lines of code does basically what the contents of Bot.py does

session.like_by_tags (['jordanbloodlines', 'travisxfragments'], amount = 5)       #Here gives the bot a list of tags to like and the number of posts to like for each tag
session.set_by_follow(True, percentage = 50)                                      #Here has the bot follow fifty percent of the users whose posts it liked
session.set_by_comment(true, percentage = 50)                                     #You can also leave comments on post by first enabling commenting which this line does
session.set_cpmments(['fire', 'pretty cool', 'Nice', 'Dope!!'])                   # and this line tells the bot what kind of comments to leave
session.set_dont_like(['naked', 'nsfw'])                                          #you can flag words so your bot won't interact with posts that match that discription
session.end()


#In addition to simply logging in to your profil, instapy also checks your internet connection and the status of your
# instagram servers.
#Instapy also logs every action it takes, when you run the code you'll notic in your shell that it'll take note of 
# the posts it liked as well as it's link, description, location and wether the bot commented on the post or followed the author
#It also has a little delay after every action to prevent your profile from being banned on instagram
