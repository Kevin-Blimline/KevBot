import discord
from discord.ext import commands

class RandomGame(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['game')
    async def RandomGame(self, ctx, *, games):
        gamesList = []
        gamesList.append(games.split(', '))
        print(gamesList)
        await ctx.send(gamesList)

def setup(client):
    client.add_cog(RandomGame(client))
