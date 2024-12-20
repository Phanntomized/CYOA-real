import time
import random

# Credit to ChatGPT for delayed letter code
text_delay = 0.001
def print_with_delay(text, delay=text_delay):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()

# Credit to ChatGPT for colored words code
class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

def the_end():
      print_with_delay(Colors.CYAN + "The end.")
      quit()
start = False

def intro():
       print_with_delay(Colors.RED + '''
             _____
            |\ ~ /|
            |}}:{{|
            |}}:{{|  _____
            |}}:{{| |Joker|
            |/_~_\| |==%, |
                    | \/>\|
                    | _>^^|           _____
          _____     |/_\/_|    _____ |6    |
         |2    | _____        |5    || ^ ^ | 
         |  ^  ||3    | _____ | ^ ^ || ^ ^ | _____
         |     || ^ ^ ||4    ||  ^  || ^ ^ ||7    |
         |  ^  ||     || ^ ^ || ^ ^ ||____9|| ^ ^ | _____
         |____Z||  ^  ||     ||____S|       |^ ^ ^||8    | _____
                |____E|| ^ ^ |              | ^ ^ ||^ ^ ^||9    |
                       |____h|              |____L|| ^ ^ ||^ ^ ^|
                                   _____           |^ ^ ^||^ ^ ^|
                           _____  |K  WW|          |____8||^ ^ ^|
                   _____  |Q  ww| | ^ {)|                 |____6|
            _____ |J  ww| | ^ {(| |(.)%%| _____
           |10 ^ || ^ {)| |(.)%%| | |%%%||A .  |
           |^ ^ ^||(.)% | | |%%%| |_%%%>|| /.\ |
           |^ ^ ^|| | % | |_%%%O|        |(_._)|
           |^ ^ ^||__%%[|                |  |  |
           |___0I|                       |____V|
                                      _____
          _____                _____ |6    |
         |2    | _____        |5    || & & | 
         |  &  ||3    | _____ | & & || & & | _____
         |     || & & ||4    ||  &  || & & ||7    |
         |  &  ||     || & & || & & ||____9|| & & | _____
         |____Z||  &  ||     ||____S|       |& & &||8    | _____
                |____E|| & & |              | & & ||& & &||9    |
                       |____h|              |____L|| & & ||& & &|
                                   _____           |& & &||& & &|
                           _____  |K  WW|          |____8||& & &|
                   _____  |Q  ww| | o {)|                 |____6|
            _____ |J  ww| | o {(| |o o%%| _____
           |10 & || o {)| |o o%%| | |%%%||A _  |
           |& & &||o o% | | |%%%| |_%%%>|| ( ) |
           |& & &|| | % | |_%%%O|        |(_'_)|
           |& & &||__%%[|                |  |  |
           |___0I|                       |____V|
                                      _____
          _____                _____ |6    |
         |2    | _____        |5    || v v | 
         |  v  ||3    | _____ | v v || v v | _____
         |     || v v ||4    ||  v  || v v ||7    |
         |  v  ||     || v v || v v ||____9|| v v | _____
         |____Z||  v  ||     ||____S|       |v v v||8    | _____
                |____E|| v v |              | v v ||v v v||9    |
                       |____h|              |____L|| v v ||v v v|
                                   _____           |v v v||v v v|
                           _____  |K  WW|          |____8||v v v|
                   _____  |Q  ww| |   {)|                 |____6|
            _____ |J  ww| |   {(| |(v)%%| _____
           |10 v ||   {)| |(v)%%| | v%%%||A_ _ |
           |v v v||(v)% | | v%%%| |_%%%>||( v )|
           |v v v|| v % | |_%%%O|        | \ / |
           |v v v||__%%[|                |  .  |
           |___0I|                       |____V|
                                      _____
          _____                _____ |6    |
         |2    | _____        |5    || o o | 
         |  o  ||3    | _____ | o o || o o | _____
         |     || o o ||4    ||  o  || o o ||7    |
         |  o  ||     || o o || o o ||____9|| o o | _____
         |____Z||  o  ||     ||____S|       |o o o||8    | _____
                |____E|| o o |              | o o ||o o o||9    |
                       |____h|              |____L|| o o ||o o o|
                                   _____           |o o o||o o o|
                           _____  |K  WW|          |____8||o o o|
                   _____  |Q  ww| | /\{)|                 |____6|
            _____ |J  ww| | /\{(| | \/%%| _____
           |10 o || /\{)| | \/%%| |  %%%||A ^  |
           |o o o|| \/% | |  %%%| |_%%%>|| / \ |
           |o o o||   % | |_%%%O|        | \ / |
           |o o o||__%%[|                |  .  |
           |___0I|                       |____V|
       ''')

       print_with_delay(Colors.CYAN + '''
                                                 
                                                 
                                                 
                                                 
       ___________.__                 ___________                      __    
       \__    ___/|__| _____   ____   \_   _____/______   ____ _____  |  | __
         |    |   |  |/     \_/ __ \   |    __) \_  __ \_/ __ \ \__ \ |  |/ /
         |    |   |  |  Y Y  \  ___/   |     \   |  | \/\  ___/ / __ \|    < 
         |____|   |__|__|_|__/\_____>  \_____/   |__|    \_____>______/__|_ \ 
                                   
                                   
                                   
                                   ''')

intro()
time.sleep(1)
#print("center".center(20,"-"))
x = input(Colors.BLUE + "                                Press x to start: " + Colors.RESET)
if x == "x":
       start = True
       text_delay = .5
       print_with_delay('''
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                      
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                      
       ''')
else:
       intro()

money = 10
health = 100
strength = 0
fall = False
clay_statue = False 
gold = 0
club = False
time1 = "present"

vip = False
necklace = False

def world1():
       global strength
       global health
       global money
       global club
       global gold
       global fall
       global clay_statue
       if world == 1:
              print_with_delay(Colors.GREEN + "You find yourself in a cave with some fresh cave paintings.")
              time.sleep(3)
              print_with_delay(Colors.BLUE + "That toaster sure wasn't lying.")
              time.sleep(3)
              print_with_delay("Speaking of the toaster, it's nowhere to be seen.")
              time.sleep(3)
              print_with_delay("I should probably look for that toaster, so it can take me back.")
              time.sleep(3)
              world1ans1 = input(Colors.MAGENTA + "Explore inside or explore outside? (inside/outside) ")
              time.sleep(1)
       else:
              return

       if world1ans1 == "inside":
              print_with_delay(Colors.GREEN + "You decide to explore the cave.")
              time.sleep(3)
              print_with_delay(Colors.WHITE + "You find a small, clay statue.")
              clay_statue = True
              time.sleep(3)
              print_with_delay(Colors.GREEN + "As you investigate the caves you realize you must be somewhere in the stone age.")
              time.sleep(3)
       elif world1ans1 == "outside":
              print_with_delay(Colors.GREEN + "You decide to explore outside the cave.")
              time.sleep(3)
              print_with_delay("It's hard to tell what time period you got warped into, because there's no sign of civilization apart from the cave.")
              time.sleep(3)
       
       print_with_delay(Colors.GREEN + "You notice two people that kind of look like neanderthals coming towards you.")
       time.sleep(3)
       print_with_delay("They are wearing crude sheepskins.")
       time.sleep(3)
       if world1ans1 == "outside":
             print_with_delay("You realize that they are neanderthals and you must be somewhere in the stone age.")
             time.sleep(3)
       print_with_delay("As they get closer, you notice they don't look too happy that you're in their territory.")
       time.sleep(3)
       world1ans2 = input(Colors.MAGENTA + "Run away or face the neanderthals? (run/stay) ")
       time.sleep(1)
       
       if world1ans2 == "run":
             print_with_delay(Colors.GREEN + "You decide to run away.")
             time.sleep(3)
             print_with_delay("Uh oh. The neanderthals decided to chase after you, and they have clubs!")
             time.sleep(3)
             print_with_delay("You run until you get to a waterfall.")
             time.sleep(3)
             print_with_delay("The neanderthals are still chasing you.")
             time.sleep(3)
             world1ans2 = input(Colors.MAGENTA + "Jump down the waterfall or face the neanderthals? (jump/stay) ")
             time.sleep(3)
       if world1ans2 == "stay":
             print_with_delay(Colors.GREEN + "You decide to stay and face the neanderthals.")
             time.sleep(3)
             print_with_delay("They approach you and make it clear they want you to give them something.")
             time.sleep(3)
             fall = True
             world1ans5 = "no"
             world1ans4 = "no"
             world1ans8 = "no"
             if clay_statue:
                   print_with_delay("You remember you still have the clay statue you took from the cave.")
                   time.sleep(3)   
                   print_with_delay(Colors.BLUE + "If I give them the statue, it may appease them...")
                   time.sleep(3)
                   print_with_delay("...But if I ever do get back to my time, I could probably sell it for a lot of money.")
                   time.sleep(3)
                   world1ans4 = input(Colors.MAGENTA + "Give the statue or keep it? (give/keep) ")
                   time.sleep(1)
                   if world1ans4 == "give":
                         print_with_delay(Colors.GREEN + "You decide to give the neanderthals the clay statue.")
                         time.sleep(3)
                         print_with_delay("One of them takes the statue and looks at it, then walks away, satisfied.")
                         time.sleep(3)
                         print_with_delay("The other one doesn't walk away but makes it clear that they want a statue as well.")
                         time.sleep(3)
                         print_with_delay("Now that there's only one, you might be able to take them in a fight.")
                         time.sleep(3)
                         world1ans5 = input(Colors.MAGENTA + "Fight the neanderthal or shrug apologetically? (fight/shrug) ")
                         time.sleep(1)
                         if world1ans5 == "shrug" or world1ans4 == "keep":
                               print_with_delay(Colors.GREEN + "You shrug apologetically.")
                               time.sleep(3)
                               print_with_delay("They aren't going to take it, and you get thrown off the waterfall.")
                         else:
                            neanderthal_health = 100
                            while neanderthal_health > 0:
                                   print_with_delay(Colors.GREEN + "You throw a punch at the neanderthal.")
                                   time.sleep(3)
                                   swing = random.randint(1,3)
                                   if swing == 1:
                                          print_with_delay(Colors.GREEN + "The blow dazes the neanderthal, but only for a second.")
                                          neanderthal_health = neanderthal_health - 10
                                          neanderthal_health = neanderthal_health - strength
                                          time.sleep(3)
                                          print_with_delay(Colors.WHITE + f"The neanderthal's health is now {neanderthal_health}.")
                                          time.sleep(3)
                                   elif swing == 2:
                                          print_with_delay(Colors.GREEN + "The blow knocks the neanderthal over.")
                                          neanderthal_health = neanderthal_health - 20
                                          neanderthal_health = neanderthal_health - strength
                                          time.sleep(3)
                                          print_with_delay(Colors.WHITE + f"The neanderthal's health is now {neanderthal_health}.")
                                          time.sleep(3)
                                          continue
                                   else:
                                          print_with_delay(Colors.GREEN + "The neanderthal evades your blow.")
                                          time.sleep(3)
                                   if neanderthal_health <= 0:
                                          print_with_delay("The neanderthal staggers backwards, and falls over.")
                                          time.sleep(3)
                                          print_with_delay("It appears you have knocked them unconscious.")
                                          time.sleep(3)
                                          print_with_delay("All that fighting has probably attracted some unwanted attention...")
                                          time.sleep(3)
                                          print_with_delay("You could loot the neanderthal but you might get caught.")
                                          time.sleep(3)
                                          world1ans8 = input(Colors.MAGENTA + "Stay a few more minutes to loot the neanderthal or run away? (loot/run) ")
                                          time.sleep(3)
                                          if world1ans8 == "loot":
                                                print_with_delay(Colors.WHITE + "You take the neanderthal's club and you find a small chunk of gold.")
                                                club = True
                                                gold = 5
                                                strength = strength + 10
                                                time.sleep(3)
                                                print_with_delay(Colors.WHITE + "You gain 10 strength.")
                                                time.sleep(3)
                                                break
                                   print_with_delay(Colors.WHITE + "Now its the neanderthal's turn to take a swing at you.")
                                   time.sleep(3)
                                   print_with_delay("You must predict where the neanderthal is going to swing so you can dodge it.")
                                   time.sleep(3)
                                   swing = random.randint(1,2)
                                   world1ans6 = input(Colors.MAGENTA + "Will the neanderthal swing left or right? (left/right) ")
                                   time.sleep(1)
                                   if world1ans6 == "right" and swing == 1:
                                          print_with_delay(Colors.GREEN + "You evade the neanderthal's attack.")
                                          time.sleep(3)
                                   elif world1ans6 == "right" and swing == 2:
                                          print_with_delay(Colors.GREEN + "You get hit with the neanderthal's club.")
                                          time.sleep(3)
                                          global health
                                          health = health - 20
                                          time.sleep(3)
                                          print_with_delay(Colors.WHITE + f"Your health is now {health}.")
                                          time.sleep(3)
                                   elif world1ans6 == "left" and swing == 1:
                                          print_with_delay(Colors.GREEN + "You evade the neanderthal's attack.")
                                          time.sleep(3)
                                   elif world1ans6 == "left" and swing == 2:
                                          print_with_delay(Colors.GREEN + "You get hit with the neanderthal's club.")
                                          time.sleep(3)
                                          health = health - 20
                                          print_with_delay(Colors.WHITE + f"Your health is now {health}.")
                                          time.sleep(3)
                                   if health <= 0:
                                          print_with_delay(Colors.WHITE + "You died: you have perished from injuries due to a neanderthal attack.")
                                          time.sleep(3)
                                          the_end()
                                   else:
                                          world1ans7 = input(Colors.MAGENTA + "Continue fighting or run away? (fight/run) ")
                                          if world1ans7 == "fight":
                                                 continue
                                          else:
                                                 world1ans8 = "run"
                                                 break
                   if world1ans4 == "keep":
                            print_with_delay(Colors.GREEN + "You decide to keep the statue.")
                            time.sleep(3)
                            print_with_delay("The neanderthals are not pleased, so they throw you off the waterfall.")
                            time.sleep(3)

             else:
                     if fall:
                            print_with_delay(Colors.GREEN + "You don't have anything to give them so you shrug apologetically.")
                            time.sleep(3)
                            print_with_delay("The neanderthals are not pleased, so they pick you up and fling you down the nearby waterfall.")
                            time.sleep(3)
                            
                            if world1ans5 == "shrug" or world1ans4 == "keep":
                                   if world1ans8 == "run":
                                          print_with_delay(Colors.GREEN + "You decide to flee the scene but then you accidentally slip and fall down a nearby waterfall.")
                                          time.sleep(3)
       print_with_delay(Colors.GREEN + "You fall down the waterfall and lose 5 health.")
       health -= 5
       time.sleep(3)
       print_with_delay("After walking a little ways away from the waterfall, you find the toaster. It still has a piece of toast in it.")
       time.sleep(3)
       print_with_delay(Colors.BLUE + "Why did you bring me here? I can't even make any money because it hasn't been invented yet?")
       time.sleep(3)
       print_with_delay(Colors.RED + "There must have been a mistake somewhere in between the present and now. But don't worry, with just a twist of my knob, you can be whisked away to a different time period.")
       time.sleep(3)
       global time1 
       time1 = input(Colors.MAGENTA + "Go to the present or the future? (present/future) ")
       time.sleep(1)

def world2():
       global vip
       global necklace
       global health
       global strength
       global money
       global world
       def roulette():
              global money
              global vip
              cont = True
              wins = 0
              while cont:
                     if money <= 0:
                            print_with_delay(Colors.GREEN + f"Warning, you have ${money}!")
                            time.sleep(3)
                            print_with_delay("If you gain too much debt, you might get into trouble...")
                            time.sleep(3)
                     else:
                            print_with_delay(Colors.WHITE + f"You have {money}.")
                            time.sleep(3)
                     cont = input(Colors.MAGENTA + "Play roulette? (yes/no) ")
                     time.sleep(1)
                     if cont != "yes":
                            return
                     wheel = random.randint(0,1)
                     bet = int(input(Colors.MAGENTA + f"How much do you want to bet? (up to ${money}) "))
                     time.sleep(1)
                     money -= bet
                     time.sleep(3)
                     choice = random.randint(0,1)
                     if choice == 0:
                            choice = input("Bet on white or black? (white/black) ")
                     else:
                            choice = input("Bet on odds or evens? (odds/evens) ")
                     time.sleep(1)
                     if choice == "white" or choice == "odds" and wheel == 0:
                            print_with_delay(Colors.GREEN + f"You win and earn ${bet*2}.")
                            time.sleep(3)
                            wins += 1
                            money += bet*2
                     elif choice == "black" or choice == "evens" and wheel == 1:
                            print_with_delay(Colors.GREEN + f"You win and earn ${bet * 2}.")
                            time.sleep(3)
                            wins += 1
                            money += bet*2
                     else:
                            print_with_delay(Colors.GREEN + "You don't win anything.")
                            time.sleep(3)
                            wins -= 1
                     if wins >= 3:
                            vip = True
                            print_with_delay(Colors.WHITE + "You gain a VIP pass for winning 3 times in a row.")
                            time.sleep(3)
                            continue
                     else:
                            print_with_delay(f"You've won {wins} times in a row.")
                            time.sleep(3)
                            continue

       def poker():
              hand = random.randint(1, 50)
              if hand == 1:
                     return "royal flush"
              else:
                     hand = random.randint(1, 40)
                     if hand == 1:
                            return "straight flush"
                     else:
                            hand = random.randint(1, 35)
                            if hand == 1:
                                   return "four of a kind"
                            else:
                                   hand = random.randint(1, 30)
                                   if hand == 1:
                                          return "full house"
                                   else:
                                          hand = random.randint(1, 25)
                                          if hand == 1:
                                                 return "flush"
                                          else:
                                                 hand = random.randint(1, 20)
                                                 if hand == 1:
                                                        return "straight"
                                                 else:
                                                        hand = random.randint(1, 15)
                                                        if hand == 1:
                                                               return "three of a kind"
                                                        else:
                                                               hand = random.randint(1, 10)
                                                               if hand == 1:
                                                                      return "two of a kind"
                                                               else:
                                                                      hand = random.randint(1, 5)
                                                                      if hand == 1:
                                                                             return "pair"
                                                                      else:
                                                                             return "high card"
       def blackjack():
              bj_won = False
              new_game = False
              round_over = False
              won = 0
              lost = 0
              game_round = 1
              opdone = False
              card_num = 2
              time.sleep(3)
              while not new_game:
                     card_num = 2
                     opcard_num = 2
                     total = 0
                     optotal = 0
                     ace = 0
                     opace = 0
                     print_with_delay(Colors.WHITE + f"Round {game_round}")
                     time.sleep(3)
                     game_round += 1
                     round_over = False
                     opdone = False
                     num = random.randint(2,11)
                     name = num
                     num2 = random.randint(2,11)
                     name2 = num2
                     total = num + num2
                     if num == 11:
                            name = "an ace"
                            ace += 1
                     if num2 == 11:
                            name2 = "an ace"
                            ace += 1
                     opnum = random.randint(2,11)
                     opname = opnum
                     opnum2 = random.randint(2,11)
                     opname2 = opnum2
                     optotal = opnum + opnum2
                     if opnum == 11:
                            opname = "an ace"
                            opace += 1
                     if opnum2 == 11:
                            opname2 = "an ace"
                            opace += 1
                     optotal = opnum + opnum2
                     print_with_delay(Colors.GREEN + "You each get dealt 2 cards.")
                     time.sleep(3)
                     print_with_delay(f"Your card's values are {name} and {name2}.")
                     time.sleep(3)
                     if ace > 0 and total > 21:
                            total -= 10
                            print_with_delay(f"Your ace's value changes to 1 and your total is {total}.")
                            name = False
                            time.sleep(3)
                     print_with_delay(f"Your opponent has {opname} and {opname2}.")
                     time.sleep(3)
                     if opace > 0 and optotal > 21:
                            optotal -= 10
                            print_with_delay(f"Their ace's value changes to 1 and their total is {optotal}.")
                            opace -= 1
                            opname = False
                            time.sleep(3)
                     while not round_over:
                            hit_stand = input(Colors.MAGENTA + "Hit or stand? (hit/stand) ")
                            time.sleep(1)
                            if hit_stand == "hit":
                                   card_num += 1
                                   num = random.randint(2,11)
                                   total += num
                                   if num == 11:
                                          name = "an ace"
                                          ace += 1
                                   else:
                                          name = False
                                   if name == "an ace":
                                          print_with_delay(Colors.GREEN + f"You drew {name}.")
                                   else:
                                          print_with_delay(Colors.GREEN + f"You drew {num}")
                                   time.sleep(3)
                                   if ace > 0 and total > 21:
                                          total -= 10
                                          print_with_delay(f"Your ace's value changes to 1 and your total is {total}.")
                                          ace -= 1
                                          time.sleep(3)
                                   if total <= 21:
                                          if card_num == 5:
                                                 print_with_delay("You win the round by holding 5 cards.")
                                                 won += 1
                                                 round_over = True
                                                 break
                                          else:
                                                 continue
                                   if total > 21:
                                          if total > 21 and ace == 22:
                                                 print_with_delay("Your opponent accuses you of cheating and you get thrown out of the casino.")
                                                 time.sleep(3)
                                                 return "lost"
                                          else:
                                                 print_with_delay("You busted!")
                                                 time.sleep(3)
                                                 lost += 1
                                                 round_over = True            
                                                 break
                            else:
                                   print_with_delay(f"You stood with {total}.")
                                   time.sleep(3)
                                   opdone = False
                            if ace > 11:
                                   print_with_delay("Your opponent becomes suspicious of you holding aces.")
                                   time.sleep(3)
                            while not opdone:
                                   if 17 <= optotal <= 21 and optotal >= total:
                                          print_with_delay(f"Your opponent stood with {optotal}")
                                          time.sleep(3)
                                          opdone = True
                                          break
                                   elif optotal <= 17 or optotal < total:
                                          opnum = random.randint(2,11)
                                          opcard_num += 1
                                          optotal += opnum
                                          if opnum == 11:
                                                 opname = "an ace"
                                                 opace += 1
                                          else:
                                                 opname = False
                                   if opname == "an ace":
                                          print_with_delay(f"Your opponent draws {opname}")
                                          time.sleep(3)
                                   else:
                                          print_with_delay(f"Your opponent draws {opnum}.")
                                          time.sleep(3)
                                   if opace > 0 and optotal > 21:
                                          optotal -= 10
                                          print_with_delay(f"Their ace's value changes to 1 and their total is {optotal}.")
                                          opace -= 1
                                          time.sleep(3)
                                   if optotal > 21:
                                          print_with_delay("Your opponent has busted!")
                                          time.sleep(3)
                                          won += 1
                                          round_over = True
                                          break
                                   if opcard_num == 5:
                                          print_with_delay("Yor opponent wins the round by holding 5 cards.")
                                          lost += 1
                                          round_over = True
                                          break
                                   continue
                            if total <= 21 and optotal <= 21:
                                   if optotal > total:
                                          print_with_delay("Your opponent has a higher value than you, so your opponent wins the round.")
                                          time.sleep(3)
                                          lost += 1
                                          round_over = True
                                          break
                                   elif total > optotal:
                                          print_with_delay(Colors.WHITE + "You have a higher value than your opponent, so you win the round.")
                                          time.sleep(3)
                                          won += 1
                                          round_over = True
                                          break
                                   else:
                                          print_with_delay(Colors.WHITE + "Your opponent wins due to a tie.")
                                          time.sleep(3)
                                          round_over = True
                                          lost += 1
                                          break
                     if won == 3:
                            print_with_delay(Colors.WHITE + "You beat your opponent.")
                            time.sleep(3)
                            return "won"
                     elif lost == 3:
                            print_with_delay(Colors.WHITE + "You lost and were thrown out of the casino.")
                            time.sleep(3)
                            return "lost"
                     else:
                            continue

       if world == 2:
              print_with_delay(Colors.GREEN + "You're standing outside of a casino.")
              time.sleep(3)
              print_with_delay(Colors.BLUE + "I want to find the toaster.")
              time.sleep(3)
              choice1 = True
       else:
              return
       while choice1:
              world2ans1 = input(Colors.MAGENTA + "Go to the casino restaurant or game rooms? (restaurant/game) ")
              time.sleep(1)
              while world2ans1 == "game":
                     world2ans2 = input(Colors.MAGENTA + "Go into the blackjack room, or roulette room? (blackjack/roulette) ")
                     time.sleep(1)
                     if world2ans2 == "blackjack" and bj_won:
                            print_with_delay("Nobody wants to play blackjack with you.")
                            time.sleep(3)
                     elif world2ans2 == "blackjack" and not bj_won:
                            print_with_delay(Colors.GREEN + "You go into the blackjack room and confront an important looking gambler")
                            time.sleep(3)
                            print_with_delay(Colors.BLUE + "Have you by chance seen a golden toaster?")
                            time.sleep(3)
                            print_with_delay(Colors.RED + "I might have, and I might not have, if you beat me in blackjack, I'll tell you what I know.")
                            time.sleep(3)
                            print_with_delay(Colors.WHITE + "You must beat the gambler 3 times to win, if you lose 3 times, you'll get kicked out or the casino.")
                            time.sleep(3)
                            blackjack()
                            if blackjack() != "won":
                                   break
                            elif blackjack() == "won":
                                   print_with_delay(Colors.WHITE + "The gambler gives you $50 for winning.")
                                   money += 50
                                   time.sleep(3)
                                   print_with_delay(f"Your total money is now {money}")
                                   time.sleep(3)
                                   print_with_delay(Colors.GREEN + "The gambler tells you that the boss gambler is going to gamble away the golden toaster, and instructs you to the room he'll be in.")
                                   time.sleep(3)
                                   bj_won = True
                                   if not vip:
                                          print_with_delay("You need a VIP pass to enter the boss gambler's room.")
                                          time.sleep(3)
                                          print_with_delay("You go off in search of a VIP pass.")
                                          time.sleep(3)
                                          world2ans1 = "restaurant"
                                   else:
                                          print_with_delay(Colors.GREEN + "You use your VIP pass to go onto the boss gambler's room.")
                                          time.sleep(3)
                                          print_with_delay("The boss gambler smirks as you enter and beckons for you to sit down.")
                                          time.sleep(3)
                                          print_with_delay(Colors.RED + "You gotta pay to enter kid.")
                                          time.sleep(3)
                                          poker_game = True
                                          won = 0
                                          toaster = False
                                          pool = 0
                                          while poker_game:
                                                 opraise = 0
                                                 world2ans6 = input(Colors.MAGENTA + "Pay $5 to start round? (yes/no) ")
                                                 time.sleep(1)
                                                 if world2ans6 == "yes":
                                                        money -= 5
                                                        print_with_delay(Colors.GREEN + "You bet $5.")
                                                        time.sleep(3)
                                                        if won >= 5:
                                                               print_with_delay("The boss brings out the golden toaster and puts it in the betting pool.")
                                                               time.sleep(3)
                                                               toaster = True
                                                        else:
                                                               print_with_delay("The boss matches.")
                                                               time.sleep(3)
                                                               pool += 10
                                                        if money < 0:
                                                               print_with_delay("You are in debt!")
                                                               time.sleep(3)
                                                        print_with_delay("The boss starts the game of poker.")
                                                        time.sleep(3)
                                                        hand = poker()
                                                        print_with_delay(f"Your hand type is a {hand}.")
                                                        time.sleep(3)
                                                        world2ans8 = input(Colors.MAGENTA + "Keep hand or redraw? (keep/draw) ")
                                                        time.sleep(1)
                                                        if world2ans8 == "draw":
                                                               hand = poker()
                                                               print_with_delay(Colors.GREEN + f"Your hand type is a {hand}.")
                                                               time.sleep(3)
                                                        ophand = poker()
                                                        if ophand == "high card" or ophand == "pair" or ophand == "two pair":
                                                               print_with_delay(Colors.GREEN + "The boss redraws his hand.")
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
                                                               print_with_delay(f"The boss raises by ${opraise}.")
                                                               time.sleep(3)
                                                               print_with_delay(f"The current pool is worth {pool}.")
                                                               time.sleep(3)
                                                               world2ans7 = input(Colors.MAGENTA + "Match, raise, or fold? (match/raise/fold) ")
                                                               time.sleep(1)
                                                        else:
                                                               print_with_delay("The boss checks.")
                                                               time.sleep(3)
                                                               world2ans7 = input("Match, raise, or fold? (match/raise/fold) ")
                                                               time.sleep(1)
                                                        if world2ans7 == "raise":
                                                               raise_pool = float(input(Colors.MAGENTA + "How much do you want to raise by? "))
                                                               time.sleep(1)
                                                               pool += raise_pool
                                                               print_with_delay(Colors.GREEN + f"You raise by {raise_pool}.")
                                                               time.sleep(3)
                                                               if raise_pool <= opraise * 3 or ophand == "royal flush" or hand == "straight flush" or hand == "four of a kind" or hand == "full house" or hand == "straight" or hand == "three of a kind":
                                                                      print_with_delay(f"The boss matches with {raise_pool}.")
                                                                      time.sleep(3)
                                                                      pool += raise_pool
                                                               else:
                                                                      print_with_delay("The boss folds.")
                                                                      time.sleep(3)
                                                                      if won >= 5:
                                                                             print_with_delay(Colors.WHITE + "You gained the golden toaster!")
                                                                             time.sleep(3)
                                                                             break
                                                                      else:
                                                                             print_with_delay(Colors.WHITE + f"You gain ${pool}.")
                                                                             time.sleep(1)
                                                                             money += pool
                                                                             pool = 0
                                                                             won += 1
                                                                             continue
                                                        if world2ans7 == "match":
                                                               print_with_delay(Colors.GREEN + f"You match with ${opraise}.")
                                                               time.sleep(3)
                                                               money -= opraise
                                                               pool += opraise
                                                               if ophand == "royal flush":
                                                                      if hand == "royal flush":
                                                                             print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print_with_delay(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print_with_delay("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "straight flush" and hand != "royal flush":
                                                                      if hand == "straight flush":
                                                                             print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print_with_delay(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print_with_delay("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "four of a kind" and hand != "royal flush" and hand != "straight flush":
                                                                      if hand == "four of a kind":
                                                                             print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print_with_delay(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print_with_delay("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "full house" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind":
                                                                      if hand == "full house":
                                                                             print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print_with_delay(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print_with_delay("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "straight" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house":
                                                                      if hand == "straight":
                                                                             print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print_with_delay(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print_with_delay("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "three of a kind" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "straight":
                                                                      if hand == "three of a kind":
                                                                             print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print_with_delay(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print_with_delay("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "two pair" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "straight" and hand != "three of a kind":
                                                                      if hand == "two pair":
                                                                             print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print_with_delay(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print_with_delay("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "pair" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "straight" and hand != "three of a kind" and hand != "two pair":
                                                                      if hand == "pair":
                                                                             print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print_with_delay(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print_with_delay("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               elif ophand == "high card" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "straight" and hand != "three of a kind" and hand != "two pair" and hand != "pair":
                                                                      if hand == "high card":
                                                                             print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                             time.sleep(3)
                                                                      else:
                                                                             print_with_delay(f"Your opponent wins the round, he had a {ophand}")
                                                                             time.sleep(3)
                                                                             print_with_delay("He takes the pool.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                               else:
                                                                      print_with_delay(f"You win the round, your opponent had a {ophand}.")
                                                                      time.sleep(3)
                                                                      if toaster:
                                                                             print_with_delay("You take the toaster.")
                                                                             time.sleep(3)
                                                                             break
                                                                      else:
                                                                             print_with_delay(f"You take the prize pool of ${pool}.")
                                                                             time.sleep(3)
                                                                             pool = 0
                                                                             continue
                                                        if world2ans7 == "fold":
                                                               print_with_delay(Colors.GREEN + "You folded!")
                                                               time.sleep(3)
                                                               print_with_delay("The boss takes the prize pool.")
                                                               time.sleep(3)
                                                               pool = 0
                                                               continue

                                                 else:
                                                        print_with_delay(Colors.GREEN + "You get up and leave.")
                                                        time.sleep(3)
                                                        break
                            else:
                                   print_with_delay(Colors.GREEN + "You lose $50 for losing.")
                                   money -= 50
                                   time.sleep(3)
                                   if money < 0:
                                          print_with_delay(Colors.WHITE + f"You ${money} are in debt!")
                                   world2()
                     else:
                            print_with_delay(Colors.GREEN + "You go into the roulette room.")
                            time.sleep(3)
                            print_with_delay("There's no information about the golden toaster.")
                            time.sleep(3)
                            print_with_delay("You notice a VIP pass you could win.")
                            time.sleep(3)
                            print_with_delay(Colors.BLUE + "Since I'm here anyways, I could play a few rounds of roulette.")
                            time.sleep(3)
                            world2ans5 = input(Colors.MAGENTA + "Stay and play roulette or go look for the toaster? (stay/leave) ")
                            time.sleep(1)
                            if world2ans5 == "stay":
                                   roulette()
                            else:
                                   continue
              if world2ans1 == "restaurant":
                     print_with_delay(Colors.GREEN + "You decide to go to the restaurant.")
                     time.sleep(3)
                     world2ans2 = input(Colors.MAGENTA + "Go into the kitchen or search around the dining area? (kitchen/dining) ")
                     time.sleep(1)
                     if world2ans2 == "dining":
                            print_with_delay(Colors.GREEN + "You decide to look around the dining area.")
                            time.sleep(3)
                            if not necklace:
                                   jewelry = random.randint(1,3)
                                   if jewelry == 1:
                                          jewelry = "bracelet"
                                   elif jewelry == 2:
                                          jewelry = "necklace"
                                   elif jewelry == 3:
                                          jewelry = "ring"
                                   print_with_delay(f"You find a beautiful golden {jewelry} lying on a table. It might be useful later.")
                                   time.sleep(3)
                                   steal = input(Colors.MAGENTA + "Steal the piece of jewelry? (yes/no) ")
                                   time.sleep(1)
                                   if steal == "yes":
                                          print_with_delay(Colors.GREEN + f"You grab the {jewelry} and stuff it into your pocket.")
                                          necklace = True
                                          time.sleep(3)
                                          print_with_delay("Someone sees you steal the necklace, and comes over to confront you.")
                                          world2ans3 = input(Colors.MAGENTA + "Attempt to start a food fight or wait for them to come to you. (food/wait) ")
                                          time.sleep(1)
                                          if world2ans3 == "food":
                                                 print_with_delay(Colors.GREEN + "You successfully start a food fight.")
                                                 time.sleep(3)
                                                 print_with_delay("In the confusion, you sneak out of the restaurant.")
                                                 time.sleep(3)
                                                 continue
                                          elif world2ans3 == "wait":
                                                 print_with_delay(Colors.GREEN + "You decide to wait for the person to come over to you.")
                                                 time.sleep(3)
                                                 print_with_delay(f"The guest asks you if the {jewelry} was yours.")
                                                 time.sleep(3)
                                                 lie = input(Colors.MAGENTA + "Lie about the necklace belonging to your or tell the truth? (lie/truth) ")
                                                 time.sleep(1)
                                                 if lie == "lie":
                                                        print_with_delay(Colors.GREEN + f"You lie about the {jewelry}.")
                                                        time.sleep(3)
                                                        print_with_delay("The person believes you and goes back to their table.")
                                                        time.sleep(3)
                                                 elif lie == "truth":
                                                        print_with_delay(Colors.GREEN + "You tell the truth.")
                                                        time.sleep(3)
                                                        print_with_delay("The person thinks you are being sarcastic and goes back to their table.")
                                                        time.sleep(3)
                                   elif steal == "no":
                                          print_with_delay(Colors.GREEN + f"You decide not to steal the {jewelry}.")
                                          time.sleep(3)
                                          world2ans2 = "kitchen"
                            else:
                                   print_with_delay(Colors.GREEN + "You don't find anything.")
                                   time.sleep(3)
                            world2ans4 = input(Colors.MAGENTA + "Go into the kitchen or go back to the lobby? (kitchen/lobby) ")
                            time.sleep(1)
                            if world2ans2 == "lobby":
                                   print_with_delay(Colors.GREEN + "You leave the restaurant.")
                                   time.sleep(3)
                                   continue
                            elif world2ans4 == "kitchen":
                                   world2ans2 = "kitchen"
                     if world2ans2 == "kitchen":
                            print_with_delay(Colors.GREEN + "You go into the kitchen and ask about a golden toaster.")
                            time.sleep(3)
                            print_with_delay("The chefs want you to prove yourself before they give you any information, so they challenge you to a cook off.")
                            time.sleep(3)
                            world2ans3 = input(Colors.MAGENTA + "Do you want to make bread, spaghetti, or a creme pie? (bread/spaghetti/pie) ")
                            time.sleep(1)
                            goodbake = True
                            if world2ans3 == "bread":
                                   print_with_delay(Colors.GREEN + "You decide to make bread.")
                                   time.sleep(3)
                                   flour = input(Colors.MAGENTA + "What is one main ingredient in bread that starts with f? ")
                                   time.sleep(1)
                                   if flour == "flour":
                                          goodbake = True
                                   else:
                                          goodbake = False
                                   if goodbake:
                                          salt = input("What is one main ingredient in bread that starts with s? ")
                                          time.sleep(1)
                                          if salt == "salt":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          yeast = input("What is one main ingredient in bread that starts with y? ")
                                          time.sleep(1)
                                          if yeast == "yeast":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          water = input("What is one main ingredient in bread that starts with w? ")
                                          time.sleep(1)
                                          if water == "water" or water == "wheat":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                            elif world2ans2 == "spaghetti":
                                   print_with_delay(Colors.GREEN + "You decide to make spaghetti.")
                                   time.sleep(3)
                                   noodles = input(Colors.MAGENTA + "What is one main ingredient in spaghetti that starts with n? ")
                                   time.sleep(1)
                                   if noodles == "noodles" or noodles == "noodle":
                                          goodbake = True
                                   else:
                                          goodbake = False
                                   if goodbake:
                                          tomato = input("What is one main ingredient in spaghetti that is two words and starts with t and s? ")
                                          time.sleep(1)
                                          if tomato == "tomato sauce":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          meat = input("What is one main ingredient in spaghetti that starts with m? ")
                                          time.sleep(1)
                                          if meat == "meat" or meat == "meatball" or meat == "meatballs":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          cheese = input("What is one main ingredient in spaghetti that starts with c? ")
                                          time.sleep(1)
                                          if cheese == "cheese":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                            else:
                                   print_with_delay(Colors.GREEN + "You decide to make a creme pie.")
                                   time.sleep(3)
                                   milk = input(Colors.MAGENTA + "What is one main ingredient in creme pie that starts with m? ")
                                   time.sleep(1)
                                   if milk == "milk":
                                          goodbake = True
                                   else:
                                          goodbake = False
                                   if goodbake:
                                          cream = input("What is one main ingredient in creme pie that starts with c? ")
                                          time.sleep(1)
                                          if cream == "creme" or cream == "cream" or cream == "crust" or cream == "custard":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          sugar = input("What is one main ingredient in creme pie that starts with s? ")
                                          time.sleep(1)
                                          if sugar == "sugar":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          eggs = input("What is one main ingredient in creme pie that starts with e? ")
                                          time.sleep(1)
                                          if eggs == "egg" or eggs == "eggs":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                            
                            if goodbake:
                                   print_with_delay(Colors.GREEN + "The chefs are impressed in your skills. One of them saw a golden shaped toaster object being taken into one of the game rooms by a gambler.")
                                   time.sleep(3)
                                   print_with_delay("Before you leave, they give you a VIP pass.")
                                   vip = True
                                   time.sleep(3)
                                   world2ans1 = "game"
                                   time.sleep(3)
                                   world = False
                                   world2()
                                   break
                            else:
                                   print_with_delay(Colors.GREEN + "The chefs are not impressed with your skills.")
                                   time.sleep(3)
                                   if world2ans3 == "pie":
                                          print_with_delay("You smash the pie into the nearest chef's face and walk out.")
                                          time.sleep(3)
                                          continue
                                   else:
                                          print_with_delay("They throw you out of the restaurant.")
                                          time.sleep(3)
                                          continue
              
def world3():
       if world == 3:
              pass

def world4():
       if world == 4:
              pass

def world5():
       if world == 5:
              pass

def world6():
       if world == 6:
              pass
       

if start:
       time.sleep(3)
       print_with_delay(Colors.GREEN + "You live in a run down apartment in one of the worst parts of town.")
       time.sleep(3)
       print_with_delay(f"You have {health} health, {strength} strength, and {money} dollars.")
       time.sleep(3)
       print_with_delay("One day while wandering through a junk shop in search of cheap furniture, you see something shining between two pieces of junk.")
       time.sleep(3)
       print_with_delay("You pull it out and you discover that it's' a golden toaster.")
       time.sleep(3)
       print_with_delay("It looks a little strange though, because instead of toasting settings on the knob, all it says is 'Past', 'Present', and 'Future'.")
       time.sleep(3)
       print_with_delay(Colors.BLUE + "Interesting, I think I'll buy this as a gag gift.")
       time.sleep(3)
       print_with_delay(Colors.GREEN + "Later when you get home, you decide to plug in the toaster to try to toast a slice of bread.")
       time.sleep(3)
       print_with_delay("When you plug in the toaster and insert a piece fo bread, you hear a strange voice start talking to you inside of your head.")
       time.sleep(3)
       print_with_delay(Colors.RED + "Hey kid, want to earn some sweet dough?")
       time.sleep(3)
       print_with_delay(Colors.BLUE + "I-I'm not sure, who are you and why are you talking to me?")
       time.sleep(3)
       print_with_delay(Colors.RED + "Come on kid, you know it's me, your toaster talking to you. And also I'm not a toaster, I'm a time travel machine. I can take you anywhere in time and you could become rich!")
       time.sleep(3)
       ans1 = input(Colors.MAGENTA + "Accept or decline the toaster's offer? (accept/decline) ")
       time.sleep(1)

       if ans1 == "decline":
              print_with_delay(Colors.BLUE + "I don't believe you.")
              time.sleep(3)
              print_with_delay(Colors.RED + "Well then let me show you...")
              time.sleep(3)
              print_with_delay(Colors.YELLOW + "Zroom!")
              time.sleep(3)
              world = random.randint(1,2)#(1,6)
       else:
              print_with_delay(Colors.BLUE + "Sounds fun, I need money.")
              time.sleep(3)
              print_with_delay(Colors.RED + "Great, would you like to go to the past or the future?")
              time.sleep(3)
              time1 = input(Colors.MAGENTA + "Go to the past or the future (<--- not coded yet don't go here)? (past/future) ")
              time.sleep(1)
              print_with_delay(Colors.YELLOW + "Zroom!")
              time.sleep(3)
              if time1 == "past":
                     world = random.randint(1,2)#(1,4)
              else:
                     world = random.randint(5,6)
       if world == 1:
              world1()
       elif world == 2:
              world2()
       elif world == 3:
              world3()
       elif world == 4:
              world4()
       elif world == 5:
              world5()
       elif world == 6:
              world6()
       if time1 == "present":
              print_with_delay(Colors.GREEN + "You find yourself back in your apartment. The toaster is plugged in next to you.")
              time.sleep(3)
              cash = input(Colors.MAGENTA + "Cash out in some of your items or move on to your next adventure? (cash/adventure) ")
              time.sleep(1)
              while cash == "cash":
                     if gold > 0:
                            cash = input(Colors.MAGENTA + "Cash in gold? (yes/no) ")
                            time.sleep(1)
                            if cash == "yes":
                                   gold = gold * 2
                                   print_with_delay(Colors.WHITE + f"You gain {gold} dollars.")
                                   cashed = True
                                   money = money + gold
                                   gold = 0
                     if clay_statue:
                            cash = input(Colors.MAGENTA + "Sell the clay statue? (yes/no) ")
                            time.sleep(1)
                            if cash == "yes":
                                   money = money + 50
                                   print_with_delay(Colors.WHITE + "You gain 50 dollars.")
                                   time.sleep(3)
                                   cashed = True
                                   clay_statue = False     
                     if club:
                            cash = input(Colors.MAGENTA + "Sell club? (yes/no) ")
                            time.sleep(1)
                            if cash == "yes":
                                   money = money + 10
                                   print_with_delay(Colors.WHITE + "You gain 10 dollars.")
                                   time.sleep(3)
                                   strength = strength - 10
                                   print_with_delay("You lose 10 strength.")
                                   cashed = True
                                   time.sleep(3)
                     cash = "adventure"
              
              print_with_delay(Colors.RED + "Alrighty kid, if your done dawdling, it's time for your next adventure. Turn my knob and go to the past or the future, there's not a minute to spare!")
              time.sleep(3)
              time1 = input(Colors.GREEN + "Go to the past or the future? (past/future) ")
              time.sleep(1)
              if time1 == "past":
                     world = random.randint(1,4)
                     if world == 1:
                            world1()
                     if world == 2:
                            world2()
                     if world == 3:
                            world3()
                     if world == 4:
                            world4()
              else:
                     world = random.randint(5,6)
                     if world == 5:
                            world5()
                     if world == 6:
                            world6()

