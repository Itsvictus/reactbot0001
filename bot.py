import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio

bot = commands.Bot(command_prefix='!')	#change the prefix silly if you want to use commands

@bot.event
async def on_ready():
    print ("hello")										#change this to whatever you want your bot to say, helps confirm your bot is running as well

custom_emojis = [										#no longer need the ID for emojis YAY!
    "goingyes",									#make sure you add that ',' if you want more than one emoji // order of appearance is descending	
	"goingno"									#obvioulsy change custom_emoji to whatever the name of your emoji is on your server
]

async def react(message):								#however we do need to call those emojis from the server... i mean guild
    for emoji in message.guild.emojis:
        if emoji.name in custom_emojis:
            await message.add_reaction(emoji)

@bot.event												
async def on_message(message):
    if message.channel.id == 509568123385544728:			#change this as well my dude
        await react(message)
		
bot.run("NjExOTY1NDIzNDI4MDQyNzcy.XVbfdg.GMFG-hPaL6Vzib5aTu1cUNFDDr4")									#hope you keNjEwOTU2OTcyNzc4NDU1MDYw.XVQ9Iw.jgX5uLmRqHp6p3uYmsrXNpt this somwhere safe >>
