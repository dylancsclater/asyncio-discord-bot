import os
from discord import Client

bot = Client()

TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.event
async def on_message(message):
    if message.content.contains("superior"):
        with open('image.png', 'rb') as fp:
            await channel.send(file=discord.File(fp, 'new_image.png'))


if __name__ == "__main__":
    bot.run(TOKEN)
