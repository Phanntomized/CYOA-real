import time
import random
def blackjack():
              new_game = False
              round_over = False
              opbust = 0
              bust = 0
              round = 1
              print("Round 1")
              time.sleep(3)
              while new_game == False:
                     ace = False
                     round_over = False
                     num = random.randint(2,11)
                     name1 = num
                     num2 = random.randint(2,11)
                     name2 = num2
                     total = num + num2
                     if num == 11:
                            name = "an ace"
                     if num2 == 11:
                            name2 = "an ace"

                     opnum = random.randint(2,11)
                     opname = opnum
                     opnum2 = random.randint(2,11)
                     opname2 = opnum2
                     optotal = opnum + opnum2
                     if opnum == 11:
                            opname = "an ace"
                     if opnum2 == 11:
                            opname2 = "an ace"
                     print("You get dealt 2 cards.")
                     time.sleep(3)
                     print(f"Your card's values are {name1} and {name2}.")
                     time.sleep(3)
                     print(f"Your opponent has {opname} and {opname2}.")
                     time.sleep(3)
                     while round_over == False:
                            hit_stand = input("Hit or stand? (hit/stand) ")
                            time.sleep(1)
                            if hit_stand == "hit":
                                   num = random.randint(2,11)
                                   total += num
                                   if num == 11:
                                          name = "an ace"
                                          ace = True
                                   else:
                                          name = False
                                   if name == "an ace":
                                          print(f"You drew {name}.")
                                   else:
                                          print(f"You drew {num}")
                                   time.sleep(3)
                                   if ace and total > 21:
                                          total -= 10
                                          print(f"Your ace's value changes to 1 and your total is {total}.")
                                          time.sleep(3)
                                   if total <= 21:
                                          continue
                                   if total > 21:
                                          print("You busted!")
                                          time.sleep(3)
                                          bust += 1
                                          round += 1
                                          round_over = True
                                          break
                            else:
                                   print(f"You stood with {total}.")
                                   time.sleep(3)

                            opace = False
                            opnum = random.randint(2,11)
                            optotal += opnum
                            if opnum == 11:
                                   opname = "an ace"
                                   opace = True
                            else:
                                   opname = False
                            if opname == "an ace":
                                   print(f"Your opponent draws {opname}")
                            else:
                                   print(f"Your opponent draws {opnum}.")
                            time.sleep(3)
                            if opace and optotal > 21:
                                   optotal -= 10
                                   print(f"Their ace's value changes to 1 and their total is {optotal}.")
                                   time.sleep(3)
                            if optotal > 21:
                                   print("Your opponent has busted!")
                                   time.sleep(3)
                                   opbust += 1
                            elif 11 < optotal <= 21:
                                   print(f"Your opponent has stood with {optotal}")
                                   time.sleep(3)
                            if total <= 21 and optotal <= 21:
                                   if optotal > total:
                                          print("Your opponent has a higher value than you, so your opponent wins the round.")
                                          time.sleep(3)
                                          bust += 1
                                          break
                                   elif total > optotal:
                                          print("You have a higher value than your opponent, so you win the round.")
                                          time.sleep(3)
                                          bust += 1
                                          break

                     if bust <= 3:
                            round += 1
                            print(f"Round {round}.")
                            time.sleep(3)
                            continue
                     else:
                            print("You lost and were thrown out of the casino.")
                            time.sleep(3)
                            return "lost"

blackjack()