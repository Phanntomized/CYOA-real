import random
def poker():
    hand = random.randint(1,20)
    if hand == 1:
        hand = "royal flush"
    else:
        hand = random.randint(1,18)
    if hand == 1:
        hand = "straight flush"
    else:
        hand = random.randint(1,16)
    if hand == 1:
        hand = "four of a kind"
    else:
        hand = random.randint(1,14)
    if hand == 1:
        hand = "full house"
    else:
        hand = random.randint(1,12)
    if hand == 1:
        hand = "flush"
    else:
        hand = random.randint(1,10)
    if hand == 1:
        hand = "straight"
    else:
        hand = random.randint(1,8)
    if hand == 1:
        hand = "three of a kind"
    else:
        hand = random.randint(1,6)
    if hand == 1:
        hand = "two of a kind"
    else:
        hand = random.randint(1,4)
    if hand == 1:
        hand = "pair"
    else:
        hand = "high card"
