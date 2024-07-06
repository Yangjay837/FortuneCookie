import random

fortunes = [
    "A new opportunity is coming your way.",
    "You will soon find yourself on a great adventure.",
    "Good things come to those who wait.",
    "Your kindness will be rewarded in the future.",
    "Believe in yourself and anything is possible."
]
random_fortune = random.choice(fortunes)
print("Your fortune cookie says:")
print(random_fortune)