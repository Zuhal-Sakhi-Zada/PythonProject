

quotes = [
    {
        "quote": "Programs must be written for people to read, and only incidentally for machines to execute.",
        "author": "Harold Abelson",
        "year": "1984"
    },
    {
        "quote": "Talk is cheap. Show me the code.",
        "author": "Linus Torvalds",
        "year": "2000"
    },
    {
        "quote": "The best way to get a project done faster is to start sooner.",
        "author": "Jim Highsmith",
        "year": "2000"
    },
    {
        "quote": "There are only two hard things in Computer Science: cache invalidation and naming things.",
        "author": "Phil Karlton",
        "year": 1990
    },
    {
        "quote": "Premature optimization is the root of all evil.",
        "author": "Donald Knuth",
        "year": 1974
    },
    {
        "quote": "Science is a way of thinking much more than it is a body of knowledge.",
        "author": "Carl Sagan",
        "year": 1986
    },
    {
        "quote": "The good thing about science is that it's true whether or not you believe in it.",
        "author": "Neil deGrasse Tyson",
        "year": 2013
    },
    {
        "quote": "Any sufficiently advanced technology is indistinguishable from magic.",
        "author": "Arthur C. Clarke",
        "year": 1962
    },
    {
        "quote": "In theory, there is no difference between theory and practice. But, in practice, there is.",
        "author": "Jan L. A. van de Snepscheut",
        "year": 1983
    },
    {
        "quote": "If debugging is the process of removing software bugs, then programming must be the process of putting them in.",
        "author": "Edsger Dijkstra",
        "year": 1970
    },
    {
        "quote": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon",
        "year": 1980
    },
    {
        "quote": "Be yourself; everyone else is already taken.",
        "author": "Oscar Wilde",
        "year": 1890
    },
    {
        "quote": "Not everything that is faced can be changed, but nothing can be changed until it is faced.",
        "author": "James Baldwin",
        "year": 1962
    },
    {
        "quote": "Do what you can, with what you have, where you are.",
        "author": "Theodore Roosevelt",
        "year": 1910
    },
    {
        "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "author": "Winston Churchill",
        "year": 1940
    },
    {
        "quote": "You miss 100% of the shots you don’t take.",
        "author": "Wayne Gretzky",
        "year": 1983
    },
    {
        "quote": "Imagination is more important than knowledge.",
        "author": "Albert Einstein",
        "year": 1929
    },
    {
        "quote": "I have not failed. I've just found 10,000 ways that won't work.",
        "author": "Thomas Edison",
        "year": 1920
    },
    {
        "quote": "Happiness is not something ready made. It comes from your own actions.",
        "author": "Dalai Lama XIV",
        "year": 2000
    },
    {
        "quote": "He who opens a school door, closes a prison.",
        "author": "Victor Hugo",
        "year": 1870
    },
    {
        "quote": "Believe you can and you're halfway there.",
        "author": "Theodore Roosevelt",
        "year": 1900
    },
    {
        "quote": "It always seems impossible until it's done.",
        "author": "Nelson Mandela",
        "year": 1990
    },
    {
        "quote": "The journey of a thousand miles begins with one step.",
        "author": "Lao Tzu",
        "year": -500
    },
    {
        "quote": "What you get by achieving your goals is not as important as what you become by achieving your goals.",
        "author": "Zig Ziglar",
        "year": 1980
    },
    {
        "quote": "You must be the change you wish to see in the world.",
        "author": "Mahatma Gandhi",
        "year": 1913
    }
]



import tkinter as tk
root = tk.Tk()
root.title("Quote Generator")
root.geometry("400x300")
root.resizable(False, False) #unveränderbare Größe

import random

random_quote = random.choice(quotes)
print(f'"{random_quote["quote"]}\n- {random_quote["author"]}, {random_quote["year"]}')

root.mainloop()