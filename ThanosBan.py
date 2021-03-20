from discord.ext import commands


class ThanosBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban_snap(self, ctx):
        members = self.bot.guild.members
        survivingMembers = self.bot.randomlyRemoveEntriesFromList(members)
        await self.bot.snap_end_message(ctx, survivingMembers)

    @commands.command()
    async def auto_ban_snap(self, ctx):
        members = self.bot.guild.members
        survivingMembers = self.bot.randomlyRemoveEntriesFromList(members)
        for x in range(len(self.bot.guild.members)):
            if members[x] not in survivingMembers:
                self.bot.guild.ban(members[x], reason='Thanos has found you unworthy', delete_message_days=0)
            else:
                pass
        await self.bot.snap_end_message(ctx, survivingMembers)
