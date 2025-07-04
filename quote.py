#!/usr/bin/env python3
import argparse, random, textwrap

QUOTES = [
    "Never give up 💪",
    "Move fast and break things 🏎️",
    "Stay hungry, stay foolish 🤓",
]

def main():
    parser = argparse.ArgumentParser(description="Print a random motivational quote.")
    parser.add_argument("-n", "--name", help="кому адресувати цитату")
    args = parser.parse_args()

    quote = random.choice(QUOTES)
    if args.name:
        quote = f"{args.name}, {quote.lower()}"
    print(textwrap.fill(quote, width=70))

if __name__ == "__main__":
    main()
