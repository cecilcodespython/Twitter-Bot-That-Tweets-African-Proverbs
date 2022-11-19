import json

import random

def collectProv():
    with open("prov.json") as provfile:
        prov = json.load(provfile)
    return prov



def getRandomProverb():
    provs = collectProv()
    prov = random.choice(provs)
    return prov['proverb']



def createTweet():
    tweet = getRandomProverb()
    return tweet