#!/usr/bin/env python3
import random, textwrap

QUOTES = [
    "Never give up 💪",
    "Move fast and break things 🏎️",
    "Stay hungry, stay foolish 🤓",
]

def main():
    print(textwrap.fill(random.choice(QUOTES), width=70))

if __name__ == "__main__":
    main()
