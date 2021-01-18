import discord
from discord.ext import commands
import sys
import random
import asyncio

description = 'A discord bot to remove half of all unimportant roles on a discord server. Useful and fun way to clean up an excessive amount of meme roles in a server'
intents = discord.Intents.default()
importantRoles = None
botToken = 0
GUILD_ID = 0

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

def randomlyRemoveRolesFromList(preSnapRoles):
    newRoles = []
    numberToBeSnapped = len(preSnapRoles) // 2
    for x in range(numberToBeSnapped):
        randomNumber = random.randint(0, len(preSnapRoles) - 1)
        newRoles.append(preSnapRoles[randomNumber])
        del preSnapRoles[randomNumber]
    return newRoles


def removeImportantRolesFromList(oldRoles):
    newRoles = oldRoles
    x = 0
    while x < len(newRoles):
        if str(newRoles[x].id) in importantRoles:
            del newRoles[x]
        x = x + 1
    return newRoles


def removeImportantRoles(guild):
    if importantRoles is not None:
        return removeImportantRolesFromList(guild.roles)
    else:
        return guild.roles


def invalidSyntax():
    print("Invalid syntax, enter -h to receive more information")
    sys.exit(0)

@bot.event
async def on_ready():
    print('Logged in as: ')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')


@bot.command()
async def thanos(ctx, arg):
    guild = bot.get_guild(GUILD_ID)

    if arg == 'auto_snap':
        originalRoles = removeImportantRoles(guild)
        survivingRoles = randomlyRemoveRolesFromList(originalRoles)

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
        originalRoles = removeImportantRoles(guild)
        survivingRoles = randomlyRemoveRolesFromList(originalRoles)

        await ctx.send("The following roles have recieved Thanos\' mercy: ")
        for x in range(len(survivingRoles)):
            await ctx.send(survivingRoles[x].name)
    elif arg == 'help':
        await ctx.send("Everything seems to have loaded in correctly! Thanos is ready to restore balance. Use snap to list out the roles, and auto_snap to automatically remove them")

if len(sys.argv) == 2:
    if sys.argv[1] in {'-h','-help','help'}:
        print("Syntax for ThanosDiscordBot is as follows: ThanosDiscordBot.py SERVER_ID BOT_TOKEN_FILE [IMPORTANT_ROLES_FILE]")
        sys.exit(0)
    else:
        invalidSyntax()
elif len(sys.argv) == 3:
    GUILD_ID = int(sys.argv[1])
    with open(sys.argv[2]) as reader:
        botToken = reader.read()
elif len(sys.argv) == 4:
    GUILD_ID = int(sys.argv[1])
    with open(sys.argv[2]) as reader:
        botToken = reader.read()
    with open(sys.argv[3]) as file:
        importantRoles = file.read().splitlines()
else:
    invalidSyntax()

# Need to write in proper input validation

if botToken != '':
    bot.run(botToken)
else:
    print("Failure to read bot token from file")
