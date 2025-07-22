#!/usr/bin/python3
import random

def get_random_word():
    with open("wordlist.txt", "r") as file:
        words = [line.strip() for line in file if line.strip().isalpha()]
    
    print(random.choice(words))