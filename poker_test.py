import random
def poker():
    hand = random.randint(1,18)
    if hand == 1:
        return "royal flush"
    else:
        hand = random.randint(1,16)
        if hand == 1:
            return "straight flush"
        else:
            hand = random.randint(1,14)
            if hand == 1:
                return "four of a kind"
            else:
                hand = random.randint(1,12)
                if hand == 1:
                    return "full house"
                else:
                    hand = random.randint(1,10)
                    if hand == 1:
                        return "flush"
                    else:
                        hand = random.randint(1,8)
                        if hand == 1:
                            return "straight"
                        else:
                            hand = random.randint(1,6)
                            if hand == 1:
                                return "three of a kind"
                            else:
                                hand = random.randint(1,4)
                                if hand == 1:
                                    return "two pair"
                                else:
                                    hand = random.randint(1,2)
                                    if hand == 1:
                                        return "pair"
                                    else:
                                        return "high card"
poker_game = True
import time
money = 20
won = 0
toaster = False
tie = False
pool = 0
                                          while poker_game:
                                                 if tie == False:
                                                        pool = 0
                                                 else:
                                                        tie = False
                                                 opraise = 0
                                                 print(f"You have ${money}")
                                                 time.sleep(3)
                                                 world2ans6 = input("Pay $5 to start round? (yes/no) ")
                                                 time.sleep(1)
                                                 if world2ans6 == "yes":
                                                        money -= 5
                                                        print("You bet $5.")
                                                        time.sleep(3)
                                                        if won >= 5:
                                                               print("The boss puts the toaster in the betting pool.")
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
                                                        else:
                                                               print("You keep your hand.")
                                                               time.sleep(3)
                                                        ophand = poker()
                                                        if ophand == "high card" or ophand == "pair" or ophand == "two pair":
                                                               print("The boss redraws his hand.")
                                                               time.sleep(3)
                                                               ophand = poker()
                                                        if ophand == "royal flush" or ophand == "straight flush" or ophand == "four of a kind" or ophand == "three of a kind":
                                                               rand_pass = random.randint(1,8)
                                                               if rand_pass == 1:
                                                                      print("The boss checks.")
                                                                      time.sleep(3)
                                                                      world2ans7 = input("Match, raise, or fold? (match/raise/fold) ")
                                                                      time.sleep(1)
                                                               else:
                                                                      if ophand == "royal flush":
                                                                             opraise = random.randint(20,50)
                                                                             pool += opraise
                                                                      elif ophand == "straight flush":
                                                                             opraise = random.randint(15,40)
                                                                             pool += opraise
                                                                      elif ophand == "four of a kind":
                                                                             opraise = random.randint(10,30)
                                                                             pool += opraise
                                                                      else:
                                                                             opraise = random.randint(5,20)
                                                                             pool += opraise
                                                                      print(f"The boss raises by ${opraise}.")
                                                                      time.sleep(3)
                                                                      print(f"The current pool is worth ${pool}.")
                                                                      time.sleep(3)
                                                                      world2ans7 = input("Match, raise, or fold? (match/raise/fold) ")
                                                                      time.sleep(1)
                                                        else:
                                                               bet = random.randint(1,5)
                                                               if bet == 1:
                                                                      opraise = random.randint(5,25)
                                                                      print(f"The boss raises by ${opraise}")
                                                                      time.sleep(3)
                                                               else:
                                                                      print("The boss checks.")
                                                                      opraise = 0
                                                                      time.sleep(3)
                                                               world2ans7 = input("Match, raise, or fold? (match/raise/fold) ")
                                                               time.sleep(1)
                                                        if world2ans7 == "raise":
                                                               if money > 0 and money >= opraise:
                                                                      raise_func = True
                                                                      while raise_func:
                                                                             raise_pool = float(input(f"How much do you want to raise by? (up to ${money}) "))
                                                                             time.sleep(1)
                                                                             if raise_pool <= money and raise_pool > opraise:
                                                                                    money -= raise_pool
                                                                                    pool += raise_pool
                                                                                    print(f"You raise by ${raise_pool}.")
                                                                                    time.sleep(3)
                                                                                    break
                                                                             else:
                                                                                    print(f"You can't bet more money than ${money}!")
                                                                                    time.sleep(3)
                                                                                    continue
                                                                      if raise_pool <= opraise+raise_pool/2 and ophand == "royal flush" or hand == "straight flush" or hand == "four of a kind" or hand == "full house" or hand == "straight" or hand == "three of a kind" or hand == "two pair":
                                                                             print(f"The boss matches with ${raise_pool-opraise}.")
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
                                                                                    money += pool
                                                                                    pool = 0
                                                                                    won += 1
                                                                                    continue

                                                               else:
                                                                      print("You can't raise, you have to have more than the bet to raise.")
                                                                      time.sleep(3)
                                                                      world2ans7 = input("Match or fold? ")
                                                                      if world2ans7 == "match":
                                                                             print(f"You match with ${opraise}.")
                                                                             time.sleep(3)
                                                                             pool += opraise
                                                                             money -= opraise
                                                                      else:
                                                                             print("You folded!")
                                                                             time.sleep(3)
                                                                             print(f"The boss takes the prize pool, worth ${pool}.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                        elif world2ans7 == "match":
                                                               if pool == 10:
                                                                      print("You check.")
                                                                      time.sleep(3)
                                                               else:
                                                                      print(f"You match with ${opraise}.")
                                                                      time.sleep(3)
                                                                      money -= opraise
                                                                      pool += opraise
                                                        else:
                                                               print("You folded!")
                                                               time.sleep(3)
                                                               print(f"The boss takes the prize pool, worth ${pool}.")
                                                               time.sleep(3)
                                                               pool = 0
                                                               continue
                                                        if ophand == "royal flush":
                                                               if hand == "royal flush":
                                                                      print("No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print(f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print(f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "straight flush" and hand != "royal flush":
                                                               if hand == "straight flush":
                                                                      print("No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print(f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print(f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "four of a kind" and hand != "royal flush" and hand != "straight flush":
                                                               if hand == "four of a kind":
                                                                      print("No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print(f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print(f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "full house" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind":
                                                               if hand == "full house":
                                                                      print("No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print(f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print(f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "flush" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "flush":
                                                               if hand == "flush":
                                                                      print("No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print(f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print(f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "straight" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "flush":
                                                               if hand == "straight":
                                                                      print("No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print(f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print(f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "three of a kind" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "flush" and hand != "straight":
                                                               if hand == "three of a kind":
                                                                      print("No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print(f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print(f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "two pair" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "flush" and hand != "straight" and hand != "three of a kind":
                                                               if hand == "two pair":
                                                                      print("No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print(f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print(f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "pair" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "flush" and hand != "straight" and hand != "three of a kind" and hand != "two pair":
                                                               if hand == "pair":
                                                                      print("No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print(f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print(f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "high card" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "flush" and hand != "straight" and hand != "three of a kind" and hand != "two pair" and hand != "pair":
                                                               if hand == "high card":
                                                                      print("No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print(f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print(f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        else:
                                                               print(f"You win the round, your opponent had a {ophand}.")
                                                               won += 1
                                                               time.sleep(3)
                                                               if toaster:
                                                                      print("You win the toaster.")
                                                                      time.sleep(3)
                                                                      won = True
                                                                      break
                                                               else:
                                                                      print(f"You take the pool, worth ${pool}.")
                                                                      money += pool
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                 else:
                                                        print("You get up and go back to the lobby.")
                                                        time.sleep(3)
                                                        won = False
                                                        break
