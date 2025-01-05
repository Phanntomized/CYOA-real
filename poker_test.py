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
poker_game = True
import time
money = 20
won = 0
pool = 0
while poker_game:
                                                 opraise = 0
                                                 world2ans6 = input("Pay $5 to start round? (yes/no) ")
                                                 time.sleep(1)
                                                 if world2ans6 == "yes":
                                                        money -= 5
                                                        print("You bet $5.")
                                                        time.sleep(3)
                                                        if won >= 5:
                                                               print("The boss brings out the golden toaster and puts it in the betting pool.")
                                                               time.sleep(3)
                                                               toaster = True
                                                        else:
                                                               print("The boss matches.")
                                                               time.sleep(3)
                                                               pool += 10
                                                        if money < 0:
                                                               print("You are in debt!")
                                                               time.sleep(3)
                                                        print("The boss starts the game of poker.")
                                                        time.sleep(3)
                                                        hand = poker()
                                                        print(f"Your hand type is a {hand}.")
                                                        time.sleep(3)
                                                        world2ans8 = input("Keep hand or redraw? (keep/draw) ")
                                                        time.sleep(1)
                                                        if world2ans8 == "draw":
                                                               hand = poker()
                                                               print(f"Your hand type is a {hand}.")
                                                               time.sleep(3)
                                                        ophand = poker()
                                                        if ophand == "high card" or ophand == "pair" or ophand == "two pair":
                                                               print("The boss redraws his hand.")
                                                               time.sleep(3)
                                                               ophand = poker()
                                                        if ophand == "royal flush" or ophand == "straight flush" or ophand == "four of a kind":
                                                               if ophand == "royal flush":
                                                                      opraise = random.randint(20,40)
                                                                      pool += opraise
                                                               elif ophand == "straight flush":
                                                                      opraise = random.randint(10,30)
                                                                      pool += opraise
                                                               else:
                                                                      opraise = random.randint(5,20)
                                                                      pool += opraise
                                                               print(f"The boss raises by ${opraise}.")
                                                               time.sleep(3)
                                                               print(f"The current pool is worth {pool}.")
                                                               time.sleep(3)
                                                               world2ans7 = input("Match, raise, or fold? (match/raise/fold) ")
                                                               time.sleep(1)
                                                        else:
                                                               print("The boss checks.")
                                                               time.sleep(3)
                                                               world2ans7 = input("Match, raise, or fold? (match/raise/fold) ")
                                                               time.sleep(1)
                                                        if world2ans7 == "raise":
                                                               raise_pool = float(input("How much do you want to raise by? "))
                                                               time.sleep(1)
                                                               pool += raise_pool
                                                               print(f"You raise by {raise_pool}.")
                                                               time.sleep(3)
                                                               if raise_pool <= opraise * 3 or ophand == "royal flush" or hand == "straight flush" or hand == "four of a kind" or hand == "full house" or hand == "straight" or hand == "three of a kind":
                                                                      print(f"The boss matches with {raise_pool}.")
                                                                      time.sleep(3)
                                                                      pool += raise_pool
                                                               else:
                                                                      print("The boss folds.")
                                                                      time.sleep(3)
                                                                      if won >= 5:
                                                                             print("You gained the golden toaster!")
                                                                             time.sleep(3)
                                                                             break
                                                                      else:
                                                                             print(f"You gain ${pool}.")
                                                                             time.sleep(1)
                                                                             money += pool
                                                                             pool = 0
                                                                             won += 1
                                                                             continue
                                                        if world2ans7 == "match":
                                                               print(f"You match with ${opraise}.")
                                                               time.sleep(3)
                                                               money -= opraise
                                                               pool += opraise
                                                               if ophand == "royal flush":
                                                                      if hand == "royal flush":
                                                                             print("No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "straight flush" and hand != "royal flush":
                                                                      if hand == "straight flush":
                                                                             print("No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "four of a kind" and hand != "royal flush" and hand != "straight flush":
                                                                      if hand == "four of a kind":
                                                                             print("No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "full house" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind":
                                                                      if hand == "full house":
                                                                             print("No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "straight" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house":
                                                                      if hand == "straight":
                                                                             print("No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "three of a kind" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "straight":
                                                                      if hand == "three of a kind":
                                                                             print("No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "two pair" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "straight" and hand != "three of a kind":
                                                                      if hand == "two pair":
                                                                             print("No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "pair" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "straight" and hand != "three of a kind" and hand != "two pair":
                                                                      if hand == "pair":
                                                                             print("No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "high card" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "straight" and hand != "three of a kind" and hand != "two pair" and hand != "pair":
                                                                      if hand == "high card":
                                                                             print("No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               else:
                                                                      print(f"You win the round, your opponent had a {ophand}.")
                                                                      time.sleep(3)
                                                                      if toaster:
                                                                             print("You take the toaster.")
                                                                             time.sleep(3)
                                                                             break
                                                                      else:
                                                                             print(f"You take the prize pool of ${pool}.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                        if world2ans7 == "fold":
                                                               print("You folded!")
                                                               time.sleep(3)
                                                               print("The boss takes the prize pool.")
                                                               time.sleep(3)
                                                               pool = 0
                                                               continue

                                                 else:
                                                        print("You get up and leave.")
                                                        time.sleep(3)
                                                        break
