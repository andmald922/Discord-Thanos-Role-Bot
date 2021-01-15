import discord
from discord.ext import commands
import random

description = 'A discord bot to remove half of all unimportant roles on a discord server. Useful and fun way to clean up an excessive amount of meme roles in a server'
intents = discord.Intents.default()
# ENTER SERVER ID HERE
GUILD_ID = 0

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

def removeImportantRolesFromList(oldRoles):
    newRoles = oldRoles
    #ADD IMPORTANT SERVER ROLE IDS HERE
    with open("") as file:
        importantRoles = file.read().splitlines()

    x = 0
    while x < len(newRoles):
        if str(newRoles[x].id) in importantRoles:
            del newRoles[x]
        x = x + 1
    return newRoles

def randomlyRemoveRoles(preSnapRoles):
    newRoles = []
    numberToBeSnapped = len(preSnapRoles) // 2
    for x in range(numberToBeSnapped):
        randomNumber = random.randint(0, len(preSnapRoles) - 1)
        newRoles.append(preSnapRoles[randomNumber])
        del preSnapRoles[randomNumber]
    return newRoles

@bot.event
async def on_ready():
    print('Logged in as: ')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')

@bot.command()
async def thanos(ctx, arg):
    if arg == 'auto_snap':
        guild = bot.get_guild(GUILD_ID)
        originalRoles = removeImportantRolesFromList(guild.roles)
        survivingRoles = randomlyRemoveRoles(originalRoles)

        for x in range(len(originalRoles)):
            if originalRoles[x] in survivingRoles:
                pass
            else:
                roleObject = guild.get_role(originalRoles[x].id)
                if roleObject is not None:
                    await roleObject.delete()
                else:
                    print("None found during role get")

        await ctx.send("The following roles have recieved Thanos\' mercy: ")
        for x in range(len(survivingRoles)):
            await ctx.send(survivingRoles[x].name)

    elif arg == 'snap':
        guild = bot.get_guild(GUILD_ID)
        originalRoles = removeImportantRolesFromList(guild.roles)
        survivingRoles = randomlyRemoveRoles(originalRoles)

        await ctx.send("The following roles have recieved Thanos\' mercy: ")
        for x in range(len(survivingRoles)):
            await ctx.send(survivingRoles[x].name)

    elif arg == 'help':
        await ctx.send("Everything seems to have loaded in correctly! Thanos is ready to restore balance. Use snap to list out the roles, and auto_snap to automatically remove them")

# ENTER BOT TOKEN HERE
with open("bot_token.txt") as reader:
    botToken = reader.read()

if botToken != '':
    bot.run(botToken)
else:
    print("Failure to read bot token from file")
