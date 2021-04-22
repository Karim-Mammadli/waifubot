import discord
import os
from dotenv import load_dotenv
import re
from make_markov import MarkovData
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

load_dotenv()

client = discord.Client()
general_channel = 806633861316345867

banned_words = [
    "hash", "map", "hashmap", "h4sh", "m4p", "h@sh", "m@p"
]
markov = MarkovData()
analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(text):
	score = analyzer.polarity_scores(text)
	lb = score['compound']
	if lb >= 0.05:
		return "that sounds like some CAP uwu"
	elif (lb > -0.05) and (lb < 0.05):
		return ":|"
	else:
		return "rather emo. Are you feeling depressed onii chan?"

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

    if "!sent" in message.content.lower()[0:5]:
        sentiment = sentiment_analyzer_scores(message.content[5::])
        await message.channel.send(str(sentiment))

    if "uwu" in message.content.lower():
        if "r" in message.content.lower():
            await message.channel.send( message.content.replace("r", "w"))
        else:
            await message.channel.send("UwU")

    if "owo" in message.content.lower():
        await message.channel.send("OwO")

    if "i think so" in message.content.lower():
        await message.channel.send("Dattebayo! OwO")

    if "thank" in message.content.lower():
        await message.channel.send("arigato gozaimasu UwU")

    if "hello" in message.content.lower().split() or "hi" in message.content.lower().split():
        await message.channel.send("yahallooo onii chan UwU")

    if "WHAT" in message.content.split():
        await message.channel.send("NANI? 0.0")

    if "faang" in message.content.lower():
        await message.channel.send("uwu i am a whitttle simpy for faangs uwu")

    if "sex" in message.content.lower():
    	await message.channel.send("so sexy ( U ω U )")

client.run(os.getenv("TOKEN"))