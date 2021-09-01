import os
import discord

bot = Client()
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.event
async def on_message(message):
    if message.content.startswith('superior'):
        await message.channel.send("All-time Win Record: Dylan Sclater - 4 vs Dylan Feeney - 0")


if __name__ == "__main__":
    bot.run(TOKEN)
