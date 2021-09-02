import os
import discord

bot = discord.Client()
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")


@bot.event
async def on_message(message):
    """ When a message comes in, pauses the event loop, checks the message, if its superior, return the shit talk"""
    if "superior" in (message.content.lower()):
        await message.channel.send("The all time record is Dylan Sclater: 4 Dylan Feeney: 0")
        await message.channel.send(file=discord.File('image.png'))


if __name__ == "__main__":
    bot.run(TOKEN)
