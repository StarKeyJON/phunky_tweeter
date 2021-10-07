# phunky_tweeter
## Retweets the PunkBot with their better half ;)

Apply for a developer account at https://developer.twitter.com It will enable you to make an app inside Twitter. Don’t worry, it is completely free to do so but may take a bit to verify. 

To apply for a Twitter developer account, you need to go to ‘developer.twitter.com’. Twitter will ask for a reason to apply for an account. Be clear with your intentions to avoid any issues in the future. Select the user profile that will be associated with the bot. It can be your personal profile but try to make a separate Twitter account for this purpose. Then you need to specify whether your bot is associated with an organization or is meant for your personal use. 

After agreeing to the terms and conditions of making a developer account and verifying it, you will be able to create your apps.

On the developer account’s dashboard, click on the button saying ‘Create an app’ on the right-hand upper corner. You will just have to fill in the following information to make your app live:

    App name: It will appear as the source of your tweets.
    App description: A little paragraph stating the purpose of your app. This will be visible to the users.
    Website URL: Just like your name, you can choose a URL.
    
Connect your app with the development environment. Then, locate the API keys and access tokens of your Twitter app. You can find them in the section of App details. After that, make sure to go through the app’s permissions precisely and regulate them. Enable the option of ‘read and write’.

Download the zip file, set up a python virtual environment and install tweepy with "pip install tweepy". This is the only external module we will need for this bot.

Enter your API key and secret and access key and secret into the fields between the quotations in config.py. (The consumer key/secret field is for the "API key/secret", and the token key/secret field is for the "access token key/secret" that is found in the dev portal.)

I added a file verify.py that you can run with the command "python3 verify.py" in your terminal to check if the keys/secrets are setup properly.

Then, run "python3 bot.py" to activate the bot.

It will retrieve the latest post from the PunkBot and save the timestamp to tweets.txt for a future record of sent tweets. If the current post's timestamp is not in the tweets.txt file, then it will automatically retweet the tweet along with all relevant info regarding the listing and save the timestamp so it won't duplicate the retweet.


If you have any questions, comments or suggestions, you can reach me on discord or twitter, 
PhunkyStarKeyJON

## Gifts are greatly appreciated but not necessary, always give from your heart.
0xF264C1dBf76205f09D79E77A1bc63b503D013204
