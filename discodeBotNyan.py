import discord
import random


TOKEN = 'MTE2MzAyNDEwOTE5ODkwOTU5Mg.Ge2NCH.0sGcvCms2uqyFJSYSTEzd6sxVYRQKnGgv3GDPY'
CHANNELID = 1162973977292062890,1162973977292062892

intents = discord.Intents.all()
intents.messages = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message: discord.Message):
    responses = ["にゃーん", "にゃー", "にゃっ！"]
    response = None
    valid_keywords = ('にゃー', 'にゃん', 'にゃーん', 'ねこ', '猫', 'ニャン','にゃ')

    if message.author == client.user:
        return
    if message.content.startswith(valid_keywords):
        response = random.choice(responses)
    if response is not None:
        await message.channel.send(response)

client.run(TOKEN)

