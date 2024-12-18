import random
def poker():
    hand = random.randint(1,50)
    if hand == 1:
        return "royal flush"
    else:
        hand = random.randint(1,40)
        if hand == 1:
            return "straight flush"
        else:
            hand = random.randint(1,35)
            if hand == 1:
                return "four of a kind"
            else:
                hand = random.randint(1,30)
                if hand == 1:
                    return "full house"
                else:
                    hand = random.randint(1,25)
                    if hand == 1:
                        return "flush"
                    else:
                        hand = random.randint(1,20)
                        if hand == 1:
                            return "straight"
                        else:
                            hand = random.randint(1,15)
                            if hand == 1:
                                return "three of a kind"
                            else:
                                hand = random.randint(1,10)
                                if hand == 1:
                                    return "two of a kind"
                                else:
                                    hand = random.randint(1,5)
                                    if hand == 1:
                                        return "pair"
                                    else:
                                        return "high card"
print(poker())
