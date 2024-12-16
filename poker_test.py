import random
def poker():
    hand = random.randint(1,100)
    if hand == 1:
        hand = "royal flush"
    else:
        hand = random.randint(1,90)
    if hand == 1:
        hand = "straight flush"
    else:
        hand = random.randint(1,80)
    if hand == 1:
        hand = "four of a kind"
    else:

    if hand:
        hand = "full house"
    if hand:
        hand = "flush"
    if hand:
        hand = "straight"
    if hand:
        hand = "three of a kind"
    if hand:
        hand = "two of a kind"
    if hand:
        hand = "pair"
    else:
        hand = "high card"
