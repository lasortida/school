from random import randrange

class Parrot:
    def __init__(self, phrase):
        self.phrases = []
        self.phrases.append(phrase)

    def say(self, repeat=1):
        phrase = self.phrases[randrange(len(self.phrases))]
        print((phrase + " ") * repeat)

    def newText(self, phrase):
        self.phrases.append(phrase)

    def learn(self, phrase):
        self.phrases.append(phrase)
