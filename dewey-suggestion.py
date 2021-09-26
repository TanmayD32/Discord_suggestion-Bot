import discord
from discord.ext import commands

token = 'REPLACE YOUR BOT TOKEN WITH THIS TEXT' # Bot token

client = commands.Bot(command_prefix='!') # bot prefix

@client.event
async def on_ready():
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="My Developer")) #bot rich presense (listening)
    print("Dewey is Online on discord!") #console print

@client.command(aliases=['suggestion']) # Suggestion command
async def s(ctx,*, message):
    await ctx.send(f'Your suggestion has been recorded: **{message}**')
    channel = client.get_channel() # put your channel ID which you want to recive member's suggestion
    embed = discord.Embed(title=f'New suggestion recived from ``{ctx.author}``', description=f'**{message}**', color=0x00ff00)
    await channel.send(embed=embed)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

client.run(token) #Token register