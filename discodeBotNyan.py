import discord
import random

from decouple import config


TOKEN = config('DISCORD_TOKEN')
CHANNELID = config('DISCODE_CHANELID')

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

