import os
import discord

bot = discord.Client()
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.event
async def on_message(message):
    if message.content.startswith("superior"):
        await message.channel.send("The all time record is Dylan Sclater: 4 Dylan Feeney: 0")


if __name__ == "__main__":
    bot.run(TOKEN)
