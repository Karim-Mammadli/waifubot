import discord
import os
from dotenv import load_dotenv
import re
from make_markov import MarkovData
import time

load_dotenv()

client = discord.Client()
general_channel = 806633861316345867

banned_words = [
    "hash", "map", "hashmap", "h4sh", "m4p", "h@sh", "m@p"
]
markov = MarkovData()

@client.event
async def on_ready():
    print("{0.user} has joined the server Uwu".format(client))
    await client.get_channel(general_channel).send("im here onii chan!")
    await client.change_presence(activity=discord.Game(name="with onii chan"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    for word in banned_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send("we don't say those words in here uwu")
            return

    if "!insult" in message.content.lower():
        await message.channel.send(markov.get_insult())

    if "!pickup" in message.content.lower():
        await message.channel.send(markov.get_pickup())
    
    if "uwu" in message.content.lower():
        if "r" in message.content.lower():
            await message.channel.send( message.content.replace("r", "w"))
        else:
            await message.channel.send("UwU")

    if "owo" in message.content.lower():
        await message.channel.send("OwO")

    if "think" in message.content.lower() or "ok" in message.content.lower():
        await message.channel.send("Dattebayo! uWu")

    if "thank" in message.content.lower():
        await message.channel.send("arigato gozaimasu UwU")

    if "hello" in message.content.lower().split() or "hi" in message.content.lower().split():
        await message.channel.send("yahallooo onii chan UwU")

    if "what" in message.content.lower() or "?" in message.content.lower():
        await message.channel.send("NANI? 0.0")

    if "faang" in message.content.lower():
        await message.channel.send("uwu i am a whitttle simpy for faangs uwu")

client.run(os.getenv("TOKEN"))