import discord
import sys
import random
from ThanosExceptions import *
import asyncio
from discord.ext import commands
from discord.ext.commands.bot import BotBase
import logging
from ThanosMute import ThanosMute
from ThanosBan import ThanosBan
from ThanosRoles import ThanosRoles

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class ThanosBotClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.importantRoles = None
        self.botToken = 0
        self.guild = None

    def setImportantRoles(self, roles):
        self.importantRoles = roles

    def getImportantRoles(self):
        return self.importantRoles

    def setBotToken(self, token):
        self.botToken = token

    def getBotToken(self):
        return self.botToken

    def setGuild(self, guild):
        self.guild = guild

    def getGuildID(self):
        return self.guild

    async def snap_end_message(self, ctx, survivors):
        await ctx.send("The following have received Thanos\' mercy: ")
        for x in range(len(survivors)):
            await ctx.send(survivors[x].name)

    def randomlyRemoveEntriesFromList(self, preSnapEntries):
        postSnapEntries = []
        numberToBeSnapped = len(preSnapEntries) // 2
        for x in range(numberToBeSnapped):
            randomNumber = random.randint(0, len(preSnapEntries) - 1)
            postSnapEntries.append(preSnapEntries[randomNumber])
            del preSnapEntries[randomNumber]
        return postSnapEntries


class ThanosBot(BotBase, ThanosBotClient):
    pass


class ThanosRunTime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as: ')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('-------')
        self.bot.guild = self.bot.get_guild(int(sys.argv[1]))

    @commands.command()
    async def h(self, ctx):
        await ctx.send(
            "Everything seems to have loaded in correctly! Thanos is ready to restore balance. Use snap to list out the roles, and auto_snap to automatically remove them"
        )


if __name__ == "__main__":
    description = 'A discord bot to remove half of all unimportant roles on a discord server. Useful and fun way to clean up an excessive amount of meme roles in a server'
    intents = discord.Intents.default()
    bot = ThanosBot(command_prefix='!thanos ', description=description, intents=intents)
    bot.add_cog(ThanosRoles(bot))
    bot.add_cog(ThanosBan(bot))
    bot.add_cog(ThanosMute(bot))
    bot.add_cog(ThanosRunTime(bot))

    if len(sys.argv) == 2:
        if sys.argv[1] in {'-h', '-help', 'help'}:
            print(
                "Syntax for ThanosDiscordBot is as follows: ThanosDiscordBot.py SERVER_ID BOT_TOKEN_FILE [IMPORTANT_ROLES_FILE]"
            )
            sys.exit(0)
        else:
            raise InvalidSyntaxError()
    elif len(sys.argv) == 3:
        with open(sys.argv[2]) as reader:
            botToken = reader.read()
    elif len(sys.argv) == 4:
        with open(sys.argv[2]) as reader:
            botToken = reader.read()
        with open(sys.argv[3]) as file:
            bot.importantRoles = file.read().splitlines()
    else:
        raise InvalidSyntaxError()
    if botToken != '':
        bot.run(botToken)
    else:
        print("Failure to read bot token from file")
