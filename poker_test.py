import random
def poker():
    hand = random.randint(1,20)
    if hand == 1:
        return "royal flush"
    else:
        hand = random.randint(1,18)
        if hand == 1:
            return "straight flush"
        else:
            hand = random.randint(1,16)
            if hand == 1:
                return "four of a kind"
            else:
                hand = random.randint(1,14)
                if hand == 1:
                    return "full house"
                else:
                    hand = random.randint(1,12)
                    if hand == 1:
                        return "flush"
                    else:
                        hand = random.randint(1,10)
                        if hand == 1:
                            return "straight"
                        else:
                            hand = random.randint(1,8)
                            if hand == 1:
                                return "three of a kind"
                            else:
                                hand = random.randint(1,6)
                                if hand == 1:
                                    return "two of a kind"
                                else:
                                    hand = random.randint(1,4)
                                    if hand == 1:
                                        return "pair"
                                    else:
                                        return "high card"
print(poker())
