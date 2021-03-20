from discord.ext import commands


class ThanosRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def removeImportantRolesFromList(self, oldRoles):
        # Been doing way too much java lately, I'm almost positive this assignment isn't necessary like at all
        newRoles = oldRoles
        x = 0
        while x < len(newRoles):
            if str(newRoles[x].id) in self.bot.getImportantRoles():
                del newRoles[x]
            x = x + 1
        return newRoles

    def removeImportantRoles(self, guild):
        if self.bot.getImportantRoles() is not None:
            return self.removeImportantRolesFromList(guild.roles)
        else:
            return guild.roles

    @commands.command()
    async def role_snap(self, ctx):
        originalRoles = self.removeImportantRoles(self.bot.guild)
        survivingRoles = self.bot.randomlyRemoveEntriesFromList(originalRoles)
        await self.bot.snap_end_message(ctx, survivingRoles)

    @commands.command()
    async def auto_role_snap(self, ctx):
        originalRoles = self.removeImportantRoles(self.bot.guild)
        survivingRoles = self.bot.randomlyRemoveEntriesFromList(originalRoles)

        for x in range(len(originalRoles)):
            if originalRoles[x] in survivingRoles:
                pass
            else:
                roleObject = self.bot.guild.get_role(originalRoles[x].id)
                if roleObject is not None:
                    await roleObject.delete()
                else:
                    print("None found during role get")
        await self.bot.snap_end_message(ctx, survivingRoles)
