class Parrot:
    def __init__(self, phrase):
        self.phrase = phrase

    def say(self, repeat=1):
        print((self.phrase + " ") * repeat)

    def newText(self, phrase):
        self.phrase = phrase

