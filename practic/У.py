from random import random

class Parrot:
    def __init__(self, phrase):
        self.phrases = []
        self.phrases.append(phrase)

    def say(self, repeat=1):
        phrase = self.phrases[random() * (len(self.phrases) - 1)]
        print((phrase + " ") * repeat)

    def newText(self, phrase):
        self.phrases.append(phrase)

    def learn(self, phrase):
        self.phrases.append(phrase)
