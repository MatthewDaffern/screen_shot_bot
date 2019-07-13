#What is this?

I wanted to make a bot that'll track website changes for me.

I'm trying to make it as light as possible, so I can upload it to cloud-formation on AWS.

#How are you going to track changes?

I am going to try capture state changes in a website. I was going to hash the page, but that failed suprisingly fast in testing.

Right now I'm looking into creating image renders of the page and hashing those, but I'm not too sure.

#How do I use it?

Double click config_email.py and fill out the prompt for your username and password.

Double click config.py to add what website you're going to be tracking.

I'll probably also have a separate JSON file for the server configuration details since I'll be using SMTP with SSL to send out emails, but I haven't gotten that far yet.

After you've configured your website, either start running the script on a device or upload it to cloud formation. I have two options available.

use invoker.py for aws, and bot.py for a script with a while loop.