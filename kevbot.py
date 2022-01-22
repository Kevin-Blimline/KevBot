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
    myid = '<@201909896357216256>'
    await ctx.send('Matt is on the couch')

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
                "I ordered a chicken and an egg online, I'll let you know.",
                "I have a genetic disposition for diarrhea, it runs in my jeans!",
                "It takes guts to be an organ donor.", 
                "I tried to catch fog the other day, mist.","Zucchini, more like dumbkini.",
                "I'm afraid for the calendar. Its days are numbered.",
                "My wife said I should do lunges to stay in shape. That would be a big step forward.",
                "What do a tick and the Eiffel Tower have in common?" "They're both Paris sites",
                "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along.",
                "Dear Math, grow up and solve your own problems.",
                "Have you heard about the chocolate record player? It sounds pretty sweet.",
                "I only know 25 letters of the alphabet. I don't know y.",
                "A skeleton walks into a bar and says, 'Hey, bartender. I'll have one beer and a mop.'",
                "I asked my dog what's two minus two. He said nothing.",
                "I got carded at a liquor store, and my Blockbuster card accidentally fell out. The cashier said never mind.",
                "My ex-wife left me and took the kids, I have never been so alone",
                "I don't trust those trees. They seem kind of shady.",
                "My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right!",
                "How do you get a squirrel to like you? Act like a nut.",
                "I don't trust stairs. They're always up to something.",
                "What do you call someone with no body and no nose? Nobody knows.",
                "Did you hear the rumor about butter? Well, I'm not going to spread it!",
                "Why did Billy get fired from the banana factory? He kept throwing away the bent ones.",
                "Why can't a ding-a-ling be 12 inches long? Because then it would be a foot.",
                "This graveyard looks overcrowded. People must be dying to get in.",
                "How many tickles does it take to make an octopus laugh? Ten tickles.",
                "I have a joke about chemistry, but I don't think it will get a reaction.",
                "What concert costs just 45 cents? 50 Cent featuring Nickelback!",
                "How do you make a tissue dance? You put a little boogie in it.",
                "What do you call cheese that isn't yours? Nacho cheese.",
                "My dad told me a joke about boxing. I guess I missed the punch line.",
                "I used to be addicted to soap, but I'm clean now.",
                "A guy walks into a bar...and he was disqualified from the limbo contest. \n\neditors note: this one is acutally pretty good",
                "You think swimming with sharks is expensive? Swimming with sharks cost me an arm and a leg.",
                "That car looks nice but the muffler seems exhausted.",
                "If a child refuses to nap, are they guilty of resisting a rest?",
                "Ever notice that Matt smells like bitch?"]
    random.shuffle(jokeList)
    jokeStr = jokeList[0]
    await ctx.send(jokeStr)

@client.command(aliases = ['extrainfo'], brief = '**ALL COMMANDS CAN BE DONE IN LOWERCASE**')
async def ExtraInfo(ctx):
    await ctx.send('**All commands can be done in lowercase**')

client.run(os.getenv('discordtoken'))
