import discord
from discord.ext import commands


class ThanosMute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mute_snap(self, ctx):
        members = self.bot.guild.members
        survivingMembers = self.bot.randomlyRemoveEntriesFromList(members)
        await self.bot.snap_end_message(ctx, survivingMembers)

    @commands.command()
    async def auto_mute_snap(self, ctx):
        members = self.bot.guild.members
        survivingMembers = self.bot.randomlyRemoveEntriesFromList(members)

        # Doesn't check to see if any new channels were added, should probably fix that
        if [x for x in self.bot.guild.roles if x.name == "ThanosMuted"]:
            pass
        else:
            thanosMutedRole = await self.bot.guild.create_role(name="ThanosMuted")
            for channel in self.bot.guild.channels:
                await channel.set_permissions(thanosMutedRole, speak=False, send_messages=False)
        thanosMutedRole = discord.utils.get(self.bot.guild.roles, name="ThanosMuted")
        for x in range(len(members)):
            if members[x] not in survivingMembers:
                await members[x].add_roles(thanosMutedRole, reason="Thanos has found you unworthy")
            else:
                pass
        self.bot.snap_end_message(ctx, survivingMembers)
