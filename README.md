## Discord Thanos Role Bot
A discord bot to remove half of all unimportant roles, users, or users ability to speak on a discord server. Fun way to create a lot of chaos and/or memes on a server
## Table of contents
* [General Info](#general-info)
* [Setup/Dependencies](#setup/dependencies)
* [TODO](#todo)
## General info
This was created purely for a meme on a discord server I am on. I will be adding to this and making new features, but at the end of the day understand that this is still meme code written by a uni student. Its gonna be scuffed


With that warning out of the way, this is just the core functionality. The name of the bot, the profile picture, what it prints back to the server, are all up to you. Go wild in creating your own personal server villain


**WARNING: NEWLY ADDED BAN AND MUTE SNAPS HAVEN'T BEEN FULLY TESTED YET. USE AT YOUR OWN PERIL. WHEN IN DOUBT JUST USE REGULAR SNAPS INSTEAD OF AUTO SNAPS**
## Setup/Dependencies
You will need [discord.py](https://github.com/Rapptz/discord.py) and Python v3.5+. Additionally, to build the version with the GUI you will need [PyQt6](https://www.riverbankcomputing.com/software/pyqt/download) and [Qt](https://www.qt.io/download-open-source)


You will need to have your bot token, and important roles ready in a txt file. The server ID can be added directly into the command line


The syntax to run this on a command line is ThanosDiscordBot.py SERVER_ID BOT_TOKEN_FILE [IMPORTANT_ROLES_FILE]


If you end up getting a SSL certificate error, it means that you either need to update your OS or manually update Discords SSL certificate on your computer.
## TODO
* Need to add input validation for the command line arguments
* Need to continue work on GUI for this
* Allow important server roles to be added via discord command rather than hard coded IDs
* Possible realm of exploration into deleting half of all messages? Maybe granularity like deleting half of all images, links, regular text messages, etc. Skys the limit when I decide to get onto this point