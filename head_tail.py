import random
heads = 0
tails = 0


for i in range(100):
    outcome = random.randint(0, 1)
    if outcome == 0:
        tails += 1
    else:
        heads += 1
print("After flipping the coin 100 times:")
print(f"Heads: {heads}")
print(f"Tails: {tails}")