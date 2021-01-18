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


You will need to have your bot token, and important roles ready in a txt file. The server ID can be added directly into the command line


The syntax to run this is ThanosDiscordBot.py SERVER_ID BOT_TOKEN_FILE [IMPORTANT_ROLES_FILE]


If you end up getting a SSL certificate error, it means that you either need to update your OS or manually update Discords SSL certificate on your computer.
## TODO
* Need to add input validation for the command line arguments
* Fix this mess of a naming scheme (honestly just clean up this code in general)
* Allow important server roles to be added via discord command rather than hard coded IDs
* Other new functions