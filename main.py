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
dad_joke_chance = 20

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
	
def printDadJoke(inputStr):
    spacing = 2;
    inputStr = inputStr.lower();
    imIndex = inputStr.find("im");
    if(imIndex == -1):
        imIndex = inputStr.find("i'm");
        spacing+=1;
    return("Hi " + inputStr[imIndex + spacing:].strip().capitalize() + ", I'm dad.");

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
	
    if ("im" in message.content.lower() or "i'm" in message.content.lower()):
        if(randint(1, 100) <= dad_joke_chance):
            await message.channel.send(printDadJoke(message.content.lower()))

    if "rawr" in message.content.lower():
        await message.channel.send("Rawr x3 *nuzzles* how are you *pounces on you* you're so warm o3o *notices you have a bulge* o: someone's happy ;) *nuzzles your necky wecky~* murr~ hehehe *rubbies your bulgy wolgy* you're so big :oooo *rubbies more on your bulgy wolgy* it doesn't stop growing ·///· *kisses you and lickies your necky* daddy likies (; *nuzzles wuzzles* I hope daddy really likes $: *wiggles butt and squirms* I want to see your big daddy meat~ *wiggles butt* I have a little itch o3o *wags tail* can you please get my itch~ *puts paws on your chest* nyea~ its a seven inch itch *rubs your chest* can you help me pwease *squirms* pwetty pwease *sad face* I need to be punished *runs paws down your chest and bites lip* like I need to be punished really good~ *paws on your bulge as I lick my lips* I'm getting thirsty. I can go for some milk *unbuttons your pants as my eyes glow* you smell so musky :v *licks shaft* mmmm~ so musky *drools all over your cock* your daddy meat I like *fondles* Mr. Fuzzy Balls hehe *puts snout on balls and inhales deeply* oh god im so hard~ *licks balls* punish me daddy~ nyea~ *squirms more and wiggles butt* I love your musky goodness *bites lip* please punish me *licks lips* nyea~ *suckles on your tip* so good *licks pre of your cock* salty goodness~ *eyes role back and goes balls deep* mmmm~ *moans and suckles* o3o")

client.run(os.getenv("TOKEN"))
