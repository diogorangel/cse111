import random

def append_random_numbers(numbers_list, quantity=1):
    """Appends 'quantity' random float numbers (rounded to 1 decimal) to numbers_list."""
    for _ in range(quantity):
        numbers_list.append(round(random.uniform(0, 100), 1))

def append_random_words(words_list, quantity=1):
    """Appends 'quantity' random words from a predefined list to words_list."""
    word_choices = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    for _ in range(quantity):
        words_list.append(random.choice(word_choices))

def main():
    numbers = [16.2, 75.1, 52.3]
    print("Initial numbers list:", numbers)
    
    append_random_numbers(numbers)
    print("After adding one random number:", numbers)
    
    append_random_numbers(numbers, 3)
    print("After adding three random numbers:", numbers)
    
    words = ["hello", "world"]
    print("Initial words list:", words)
    
    append_random_words(words, 2)
    print("After adding two random words:", words)

if __name__ == "__main__":
    main()
