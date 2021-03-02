import markovify

# TODO: save models in json
# TODO: add markov for every user
class MarkovData:
    def __init__(self):
        with open("data/insults.txt", "r", encoding="utf-8") as f:
            text = f.read()
        self.insult_model = markovify.NewlineText(text)
        self.insult_model.compile()
        with open("data/pickuplines.txt", "r", encoding="utf-8") as f:
            text = f.read()
        self.pickup_model = markovify.NewlineText(text)
        self.pickup_model.compile()
    def get_insult(self):
        return self.insult_model.make_sentence()
    def get_pickup(self):
        return self.pickup_model.make_sentence()
