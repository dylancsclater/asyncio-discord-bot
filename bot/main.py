import os
from discord import Client

bot = Client()

TOKEN = os.getenv("DISCORD_TOKEN")
keyword = "SUPERIOR"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.event
async def on_message(message):
    if message.content.startswith("superior"):
        await message.channel.send("The all time record is Dylan Sclater: 4 Dylan Feeney: 0")


# @bot.event
# async def on_message(message):
#     message_text = message.content.strip().upper()
#     if keyword in message_text:
#         await bot.send_message(message.channel, "it worked")

if __name__ == "__main__":
    bot.run(TOKEN)
