import discord
from discord.ext import commands
import os
import random

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('captcha simulator'))
    print('Bot is online')

@client.command(aliases = ['game', 'RanGame','randomgame','rangame'], brief='Type in games seperated by commas')
async def RandomGame(ctx, *, games):
    gamesList = []
    selectedGame = None
    gamesList = (games.split(', '))
    random.shuffle(gamesList)
    selectedGame = gamesList[0]
    await ctx.send(f'The random game is: {selectedGame}')

@client.command(aliases = ['wheresmatt', 'Wheresmatt', 'WhereIsMatt', 'whereismatt'], brief = 'Tells user where Matt Crump is')
async def WheresMatt(ctx):
    member = discord.utils.get(ctx.message.guild.members, name='Crumpy61')
    await ctx.send(member.mention + ' is on his couch')

@client.command(aliases = ['ping'], brief = 'Tells user their ping')
async def Ping(ctx):
    await ctx.send(f'Your ping is {round(client.latency * 1000)}ms')

@client.command(aliases = ['online'], brief = 'Shows list of online users')
async def Online(ctx):
    userList = []
    for user in ctx.guild.members:
        if user.status != discord.Status.offline:
            userList.append(user.name)
    userStr = ', '.join(userList)
    await ctx.send(f'Online users: {userStr}')

@client.command(aliases = ['randomuser', 'Randomuser', 'RanUser', 'ranuser'], brief = 'Randomly selects online user')
async def RandomUser(ctx):
    userList = []
    for user in ctx.guild.members:
        if user.status != discord.Status.offline:
            userList.append(user.name)
    random.shuffle(userList)
    userStr = userList[0]
    await ctx.send(userStr)

@client.command(aliases = ['extrainfo'], brief = '**ALL COMMANDS CAN BE DONE IN LOWERCASE**')
async def ExtraInfo(ctx):
    await ctx.send('**All commands can be done in lowercase**')

client.run('NzA5ODIyMDAxNDYzOTUxNDUx.XrrfZw.Ph3OuyuVhed0gI9vc5bpk_Qq-Lk')
