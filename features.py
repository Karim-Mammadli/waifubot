import discord

def make_uwu(message):
    if "uwu" in message.content.lower():
        await message.channel.send(message.author + ":", message.content.replaceAll("r", w))