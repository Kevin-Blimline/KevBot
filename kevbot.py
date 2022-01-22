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
    #member = discord.utils.get(ctx.message.guild.members, name='GoatMilk')
    #member = discord.utils.get(client.users, name="GoatMilk", discriminator="8908")
    member = "304791011635494913"
    await message.channel.send(f"<@{member}> is on the couch")
    #await ctx.send(member.mention + ' is on the couch')

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

@client.command(aliases = ['dadjoke', 'Dadjoke', 'DadJokes', 'dadjokes'], brief = 'Tells a dad joke')
async def DadJoke(ctx):
    jokeList = ["That's not a camel, that's my wife!","What's brown and sticky? A stick.","I like telling dad jokes. Sometimes he laughs!",
                "I ordered a chicken and an egg online, I'll let you know.","I have a genetic disposition for diarrhea, it runs in my jeans!",
                "It takes guts to be an organ donor.", "I tried to catch fog the other day, mist.","Zucchini, more like dumbkini."]
    random.shuffle(jokeList)
    jokeStr = jokeList[0]
    await ctx.send(jokeStr)

@client.command(aliases = ['extrainfo'], brief = '**ALL COMMANDS CAN BE DONE IN LOWERCASE**')
async def ExtraInfo(ctx):
    await ctx.send('**All commands can be done in lowercase**')

client.run(os.getenv('discordtoken'))
