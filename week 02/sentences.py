#Author : Diogo Rangel Dos Santos
import random

def main():
    # Generate and print 5 random sentences
    for _ in range(5):
        print(make_sentence())

def make_sentence():
    # Generate a random sentence by calling other functions
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    
    # Combine the words into a sentence
    sentence = f"{determiner} {noun} {verb}."
    return sentence

def get_determiner():
    # List of possible determiners
    determiners = ["A", "One", "The", "Some", "Many"]
    return random.choice(determiners)

def get_noun():
    # List of possible nouns
    nouns = ["cat", "dog", "man", "woman", "bird", "girl", "boy", "animal", "car"]
    return random.choice(nouns)

def get_verb():
    # List of possible verbs
    verbs = ["runs", "eats", "laughs", "drinks", "flies", "thinks", "writes", "reads", "drives"]
    return random.choice(verbs)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()