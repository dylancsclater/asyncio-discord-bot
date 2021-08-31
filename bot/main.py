import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.listen()
async def on_message(message):
    if message.content.startswith("Superior"):
	message.channel.send("Dylan Sclater is the Superior Dylan")

if __name__ == "__main__":
    bot.run(TOKEN)
