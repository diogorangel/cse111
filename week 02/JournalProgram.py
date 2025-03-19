#Author : Diogo Rangel Dos Santos
#Week 2 - Journal Program

import random
def get_determiner(quantity):
    """Return a random determiner for the quantity."""
    determiners = ["a", "one", "the"] if quantity == 1 else ["some", "many", "the"]
    return random.choice(determiners)

def get_noun(quantity):
    """Return a random noun for the quantity."""
    nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"] if quantity == 1 else ["birds", "boys", "cars", "cats", "children", "dogs","girls", "men","rabbits", "women"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb based on tense."""
    
    verbs = {
        "past": ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
        "present_singular": ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"],
        "present_plural": ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"],
        "future": ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    }
    key = "present_singular" if tense == "present" and quantity == 1 else "present_plural" if tense == "present" else tense
    return random.choice(verbs[key])

def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Return a prepositional phrase."""
    return f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"

def make_sentence(quantity, tense):
    """Build and return a sentence with determiner, noun, verb, and prepositional phrase."""
    determiner = get_determiner(quantity).capitalize()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    return f"{determiner} {noun} {verb} {prepositional_phrase}."

def main():
    """Generate and print six sentences with different quantities and tenses."""
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

if __name__ == "__main__":
    main()
