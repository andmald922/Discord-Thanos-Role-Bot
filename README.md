## Discord Thanos Role Bot
A discord bot to remove half of all unimportant roles on a discord server. Useful and fun way to clean up an excessive amount of meme roles in a server
## Table of contents
* [General Info](#general-info)
* [Setup/Dependencies](#setup/dependencies)
* [TODO](#todo)
## General info
This was created purely for a meme on a discord server I am on. I will be adding to this and making new features, but at the end of the day understand that this is still meme code written by a uni student. Its gonna be scuffed
With that warning out of the way, this is just the core functionality. The name of the bot, the profile picture, what it prints back to the server, are all up to you. Go wild in creating your own personal server villain
## Setup/Dependencies
You will need [discord.py](https://github.com/Rapptz/discord.py) and Python v3.5+.
As of right now you will need manually add the server ID and bot token to the .py file. I will be adding ways to simply pass these along in the command line in the future. Any server roles that need to be preserved such as moderation roles can also be added to the .py by listing their ids in a .txt file and hard coding it (working on having this not be hard coded as well)
After all of that, simply run ThanosDiscordBot.py.
If you end up getting a SSL certificate error, it means that you either need to update your OS or manually update Discords SSL certificate on your computer.
## TODO
* Have the server ID not be hard coded into the .py file
* Fix this mess of a naming scheme (honestly just clean up this code in general)
* Allow important server roles to be added via discord command rather than hard coded IDs
* Other new functions