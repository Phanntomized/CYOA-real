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
       global health
       global strength
       global money
       global health_high
       global strength_high
       global money_high
       avg_money = money + money_high /2
       avg_health = health + health_high / 2
       avg_strength = strength + strength_high / 2
       print_with_delay(Colors.CYAN + "The end.")
       time.sleep(3)
       print()
       print_with_delay(Colors.WHITE + f"Your Scores: \nCurrent Money: ${round(money,2)}\nMost Money: ${round(money_high,2)}\nMoney Points: {round(avg_money,0)}\nCurrent Strength: {round(strength,0)}\nMost Strength: {round(strength_high,0)}\nStrength Points: {round(avg_strength,0)}\nCurrent Health: {round(health,0)}\nMost Health: {round(health_high,0)}\nHealth Points: {round(avg_health,0)}\nTotal Points: {round(avg_money+avg_health+avg_strength,0)}")
       time.sleep(3)
       print()
       print_with_delay(Colors.CYAN + "Thanks for playing Time Freak by Phann Boon.")
       time.sleep(3)
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
                                                 
                                                 
                                                 
                                   Phann Boon's              
       ___________.__                 ___________                      __    
       \__    ___/|__| _____   ____   \_   _____/______   ____ _____  |  | __
         |    |   |  |/     \_/ __ \   |    __) \_  __ \_/ __ \ \__ \ |  |/ /
         |    |   |  |  Y Y  \  ___/   |     \   |  | \/\  ___/ / __ \|    < 
         |____|   |__|__|_|__/\_____>  \_____/   |__|    \_____>______/__|_ \ 
                                                 
                                   ''')
def cards_intro():
       print_with_delay(Colors.YELLOW + '''
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

intro()
time.sleep(1)
#print("center".center(20,"-"))
x = input(Colors.BLUE + "                                Press x to start: " + Colors.RESET)
if x == "x":
       start = True
       skip = False
       cheat = False
       text_delay = .5
       print_with_delay('''
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
       ''')
       print_with_delay(
       Colors.YELLOW + "Warning, this is no ordinary story. Your choices will influence the outcome of this adventure. \nIf you try to make your character do something it doesn't want to do, your character may act on it's own. You have been warned...")
       time.sleep(7)
       print_with_delay('''
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                        
                                                        
                                                        
                                                        
                                                        
                                                                                                   
       ''')
       print_with_delay(Colors.MAGENTA + "When purple appears, this usually means you have to make a choice in the story. (like this/or this)")
       print_with_delay(Colors.BLUE + "When blue text appears, this usually means you are speaking.")
       print_with_delay(Colors.RED + "When red text appears, this usually means a different character is speaking.")
       print_with_delay(Colors.WHITE + "When white text appears, this usually means that either your stats have changed or you gained an item.")
       time.sleep(14)
       print_with_delay('''
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
       ''')
elif x == "skip":
       cheat = False
       skip = True
       start = True
elif x == "cheat":
       skip = False
       cheat = True
       start = True
       text_delay = 0.0
       print("god mode enabled")
       time.sleep(3)
else:
       skip = False
       cheat = False
       intro()
def high_score():
       global money
       global health
       global strength
       global money_high
       global health_high
       global strength_high
       if health > health_high:
              health_high = health
       if strength > strength_high:
              strength_high = strength
       if money > money_high:
              money_high = money

health_high = 0
strength_high = 0
money_high = 0
money = 10
health = 100
strength = 0
fall = False
clay_statue = False 
gold = 0
club = False
time1 = "present"
world2_meter = False
sick = False
food = 0
known_lotto = False
sus_lotto = 0
rand_bill = 0
wanted = 0
world5counter = 0
lottery = 99999
open_door = False
anvil = False
known_bitcoin = 0
buy_bitcoin = 0
vr = False
iphone = False
robot = False
save_food = 0
food_type = 1
world5counter = 0
jewelry = random.randint(1,3)
if jewelry == 1:
       jewelry = "bracelet"
elif jewelry == 2:
       jewelry = "necklace"
elif jewelry == 3:
       jewelry = "ring"
known_world1 = "Undiscovered Location"
known_world2 = "Undiscovered Location"
known_world3 = "Undiscovered Location"
known_world4 = "Undiscovered Location"
known_world5 = "Undiscovered Location"
known_world6 = "Undiscovered Location"

vip = False
necklace = False
def prison(time_period):
       global strength
       global health
       global money
       global wanted
       in_prison = True
       money -= money/2+wanted*10
       print()
       print_with_delay(Colors.WHITE + f"You lose ${money/2+wanted*10} for going to jail. You now have ${money}.")
       time.sleep(3)
       print()
       print_with_delay(Colors.GREEN + "Jail is very boring.")
       time.sleep(3)
       print_with_delay("As time passes, you formulate a plan.")
       time.sleep(3)
       while in_prison:
              if wanted > 4:
                     print_with_delay("You've been such a bad criminal that they give you a life sentence.")
                     time.sleep(3)
                     print_with_delay("They lock you up, and you never see the light of day again.")
                     time.sleep(3)
                     print()
                     print_with_delay(Colors.WHITE + "You Lose: You're stuck in jail for the rest of your days.")
                     time.sleep(3)
                     print()
                     the_end()
                     quit()
              print()
              prisonans1 = input(Colors.MAGENTA + "Decide to be a good prisoner, or be a bad prisoner? (good/bad) ")
              time.sleep(1)
              if prisonans1 == "good":
                     print()
                     print_with_delay(Colors.GREEN + "You decide to be good.")
                     time.sleep(3)
                     if wanted > 0:
                            if time_period == "past":
                                   health -= wanted*2
                                   strength += wanted
                                   print_with_delay(Colors.WHITE + f"You gain {wanted} strength and lose {wanted*2} health.")
                                   time.sleep(3)
                                   if health <= 0:
                                          print()
                                          print_with_delay(Colors.WHITE + "You died: you have perished in prison")
                                          time.sleep(3)
                                          print()
                                          the_end()
                                          quit()
                                   else:
                                          print_with_delay(Colors.GREEN + f"You now have {health} health and {strength} strength.")
                            elif time_period == "present":
                                   health -= wanted
                                   strength -= wanted
                                   print_with_delay(Colors.WHITE + f"You lose {wanted} strength and {wanted} health.")
                                   time.sleep(3)
                                   if health <= 0:
                                          print()
                                          print_with_delay(Colors.WHITE + "You died: you have perished in prison.")
                                          time.sleep(3)
                                          the_end()
                                          quit()
                                   else:
                                          print_with_delay(Colors.GREEN + f"You now have {health} health and {strength} strength.")
                            else:
                                   health += wanted
                                   strength -= wanted
                                   print_with_delay(Colors.WHITE + f"You lose {wanted*2} strength and gain {wanted} health.")
                                   time.sleep(3)
                                   if health <= 0:
                                          print()
                                          print_with_delay(Colors.WHITE + "You died: you have perished in prison")
                                          time.sleep(3)
                                          print()
                                          the_end()
                                          quit()
                                   else:
                                          print_with_delay(Colors.GREEN + f"You now have {health} health and {strength} strength.")
                     else:
                            if time_period == "past":
                                   print_with_delay(Colors.WHITE + "You gain 15 strength and 5 health.")
                                   health += 15
                                   high_score()
                                   strength += 5
                                   time.sleep(3)
                            elif time_period == "present":
                                   print_with_delay(Colors.WHITE + "You gain 10 strength and 10 health.")
                                   health += 15
                                   high_score()
                                   strength += 5
                                   time.sleep(3)
                            else:
                                   print_with_delay(Colors.WHITE + "You gain 5 strength and 15 health.")
                                   health += 5
                                   high_score()
                                   strength += 15
                                   time.sleep(3)
                     print_with_delay(Colors.GREEN + "You soon get let out.")
                     time.sleep(3)
                     print_with_delay("Somehow, the toaster bailed you out of jail.")
                     time.sleep(3)
                     print()
                     if time_period == "past":
                            due = 10+wanted*5
                     elif time_period == "present":
                            due = money/10+wanted*5
                     else:
                            due = money/5+wanted*5
                     print_with_delay(Colors.RED + f"Sorry kid, but I had to use ${due} of your money to bail you out. Anyways, let's go.")
                     time.sleep(3)
                     money -= due
                     print()
                     print_with_delay(Colors.CYAN + "Zroom!.")
                     time.sleep(3)
                     cards_intro()
                     print()
                     return
              else:
                     print()
                     prisonans2 = input(Colors.MAGENTA + "Attempt to escape or start a riot? (escape/riot) ")
                     time.sleep(1)
                     if prisonans2 == "escape":
                            if time_period == "past":
                                   escape = random.randint(1,3)
                            elif time_period == "present":
                                   escape = random.randint(1, 5)
                            else:
                                   escape = random.randint(1, 7)
                            if escape == 1:
                                   print()
                                   print_with_delay(Colors.GREEN + "You successfully escape jail.")
                                   time.sleep(3)
                                   wanted += 1
                                   return
                            else:
                                   print()
                                   print_with_delay(Colors.GREEN + "You attempt to escape jail but get caught.")
                                   time.sleep(3)
                                   wanted += 1
                                   continue
                     else:
                            print()
                            print_with_delay(Colors.GREEN + "You decide to start a riot.")
                            time.sleep(3)
                            if time_period == "past":
                                   riot = random.randint(1, 3)
                            elif time_period == "present":
                                   riot = random.randint(1, 4)
                            else:
                                   riot = random.randint(1, 5)
                            if time_period == "past":
                                   riot_damage = 5
                            elif time_period == "present":
                                   riot_damage = 4
                            else:
                                   riot_damage = 3
                            if riot == 1:
                                   print_with_delay(Colors.GREEN + "You successfully start a riot and escape.")
                                   time.sleep(3)
                                   wanted += 1
                                   health -= riot * riot_damage
                                   print_with_delay(f"You sustained injuries during the riot, and lost {riot*riot_damage} health. You now have {health} health.")
                                   time.sleep(3)
                                   if health <= 0:
                                          print()
                                          print_with_delay(Colors.WHITE + "You died: you have perished in a prison riot")
                                          time.sleep(3)
                                          print()
                                          the_end()
                                          quit()
                                   else:
                                          return
                            elif riot == 2 or riot == 4:
                                   print_with_delay(Colors.GREEN + "You successfully start a riot, but it gets shut down.")
                                   time.sleep(3)
                                   wanted += 1
                                   health -= riot * riot_damage
                                   print_with_delay(f"You sustained injuries during the riot, and lost {riot*riot_damage} health. You now have {health} health.")
                                   time.sleep(3)
                                   if health <= 0:
                                          print()
                                          print_with_delay(Colors.WHITE + "You died: you have perished in a prison riot")
                                          time.sleep(3)
                                          print()
                                          the_end()
                                          quit()
                                   else:
                                          continue
                            else:
                                   print_with_delay(Colors.GREEN + "You attempt to start a riot, except it doesn't work.")
                                   time.sleep(3)
                                   wanted += 1
                                   continue

def world1():
       global strength
       global health
       global money
       global club
       global gold
       global fall
       global clay_statue
       global known_world1
       known_world1 = "Stone Age"
       waterfall = False
       world1ans4 = False
       if cheat:
              clay_statue = 100
       water_dmg = random.randint(5, 10)
       world1ans7 = ""
       if world == 1:
              print_with_delay(Colors.GREEN + "You find yourself in a cave with some fresh cave paintings.")
              time.sleep(3)
              print_with_delay("The toaster is nowhere to be seen.")
              time.sleep(3)
              print()
              world1ans1 = input(Colors.MAGENTA + "Explore inside or explore outside? (inside/outside) ")
              time.sleep(1)
              print()
       else:
              return

       if world1ans1 == "inside":
              print_with_delay(Colors.GREEN + "You decide to explore the cave.")
              time.sleep(3)
              print()
              if clay_statue:
                     print_with_delay(Colors.WHITE + "You find another small, clay statue.")
                     clay_statue += 1
                     time.sleep(3)
                     print()
              else:
                     print_with_delay(Colors.WHITE + "You find a small, clay statue.")
                     clay_statue += 1
                     time.sleep(3)
                     print()
              print_with_delay(Colors.GREEN + "As you investigate the cave you realize you must be somewhere in the stone age.")
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
       print()
       world1ans2 = input(Colors.MAGENTA + "Run away or face the neanderthals? (run/stay) ")
       time.sleep(1)
       print()
       
       if world1ans2 == "run":
             print_with_delay(Colors.GREEN + "You decide to run away.")
             time.sleep(3)
             print_with_delay("Uh oh. The neanderthals decided to chase after you, and they have clubs!")
             time.sleep(3)
             print_with_delay("You run until you get to a waterfall.")
             time.sleep(3)
             print_with_delay("The neanderthals are still chasing you.")
             time.sleep(3)
             print()
             world1ans2 = input(Colors.MAGENTA + "Jump down the waterfall or face the neanderthals? (jump/stay) ")
             time.sleep(1)
       if world1ans2 == "jump":
              time.sleep(3)
              water_dmg = random.randint(5, 10)
              waterfall = True
       else:
             print_with_delay(Colors.GREEN + "You decide to stay and face the neanderthals.")
             time.sleep(3)
             print_with_delay("They approach you and make it clear they want you to give them something.")
             time.sleep(3)
             world1ans5 = "no"
             world1ans4 = "no"
             world1ans8 = "no"
             if clay_statue >= 1:
                   print_with_delay("You remember you still have the clay statue you took from the cave.")
                   time.sleep(3)
                   print()
                   print_with_delay(Colors.BLUE + "If I give them the statue, it may appease them.")
                   time.sleep(3)
                   print()
                   world1ans4 = input(Colors.MAGENTA + "Give the statue or keep it? (give/keep) ")
                   time.sleep(1)
                   print()
                   if world1ans4 == "keep":
                          print_with_delay(Colors.GREEN + "You decide to keep the statue.")
                          time.sleep(3)
                          print_with_delay("The neanderthals are not pleased, so they throw you off the waterfall.")
                          time.sleep(3)
                          water_dmg = random.randint(15, 20)
                          waterfall = True
                   else:
                         print_with_delay(Colors.GREEN + "You decide to give the neanderthals the clay statue.")
                         time.sleep(3)
                         if clay_statue >= 1:
                                clay_statue -= 1
                         print_with_delay("One of them takes the statue and looks at it, then walks away, satisfied.")
                         time.sleep(3)
                         print_with_delay("The other one doesn't walk away but makes it clear that they want a statue as well.")
                         time.sleep(3)
                         if clay_statue >= 1:
                                print()
                                world1ans4 = input(Colors.MAGENTA + "Give the second statue or keep it? (give/keep) ")
                                time.sleep(1)
                                print()
                                if world1ans4 == "give":
                                       clay_statue = 0
                                       gold += 200
                                       print_with_delay(Colors.GREEN + f"The neanderthal gives you 200 gold in exchange for the statue, then walks off. You now have {gold} gold.")
                                       time.sleep(3)
                                       print_with_delay("As you walk away, you slip and fall down a nearby waterfall")
                                       time.sleep(3)
                                       waterfall = True
                                else:
                                       print_with_delay(Colors.GREEN + "Now that there's only one, you might be able to take them in a fight.")
                                       time.sleep(3)
                                       print()
                                       world1ans5 = input(Colors.MAGENTA + "Fight the neanderthal or shrug apologetically? (fight/shrug) ")
                                       time.sleep(1)
                                       print()
                         else:
                               print_with_delay("You don't have anything to give them, but now that there's only one, you might be able to take them in a fight.")
                               time.sleep(3)
                               print()
                               world1ans5 = input(Colors.MAGENTA + "Fight the neanderthal or shrug apologetically? (fight/shrug) ")
                               time.sleep(1)
                               print()
                         if world1ans5 == "shrug":
                               print_with_delay(Colors.GREEN + "You shrug apologetically.")
                               time.sleep(3)
                               print_with_delay("They aren't going to take it, and you get thrown off the waterfall.")
                               time.sleep(3)
                               waterfall = True
                         if world1ans5 == "fight":
                            neanderthal_health = 100
                            neand_fight = 1
                            waterfall = False
                            while not waterfall:
                                   print_with_delay(Colors.GREEN + "You throw a punch at the neanderthal.")
                                   time.sleep(3)
                                   swing = random.randint(1,10)
                                   if swing == 1 or swing == 4 or swing == 5 or swing == 6 or swing == 8:
                                          print_with_delay(Colors.GREEN + "The blow dazes the neanderthal.")
                                          neanderthal_health = neanderthal_health - 10
                                          neanderthal_health = neanderthal_health - strength
                                          time.sleep(3)
                                          print()
                                          print_with_delay(Colors.WHITE + f"The neanderthal's health is now {neanderthal_health}.")
                                          time.sleep(3)
                                          print()
                                   elif swing == 2 or swing == 3 or swing == 7:
                                          print_with_delay(Colors.GREEN + "The blow knocks the neanderthal over.")
                                          neanderthal_health = neanderthal_health - 20
                                          neanderthal_health = neanderthal_health - strength
                                          time.sleep(3)
                                          print()
                                          print_with_delay(Colors.WHITE + f"The neanderthal's health is now {neanderthal_health}.")
                                          time.sleep(3)
                                          print()
                                          if neanderthal_health > 0:
                                                 continue
                                   else:
                                          print_with_delay(Colors.GREEN + "The neanderthal evades your blow.")
                                          time.sleep(3)
                                   if neanderthal_health <= 0:
                                          print_with_delay(Colors.GREEN + "The neanderthal staggers backwards, and falls over.")
                                          time.sleep(3)
                                          print_with_delay("It appears you have knocked them unconscious.")
                                          time.sleep(3)
                                          print_with_delay("All that fighting has probably attracted some unwanted attention...")
                                          time.sleep(3)
                                          if neand_fight == 1:
                                                 print_with_delay("You could loot the neanderthal but you might get caught.")
                                                 time.sleep(3)
                                                 print()
                                                 world1ans8 = input(Colors.MAGENTA + "Stay a few more minutes to loot the neanderthal or run away? (loot/run) ")
                                                 time.sleep(1)
                                                 print()
                                                 if world1ans8 == "loot":
                                                        rand_fight = random.randint(1,3)
                                                        if rand_fight == 1 or rand_fight == 3:
                                                               print_with_delay(Colors.WHITE + "You take the neanderthal's club and you find a small chunk of gold.")
                                                               club = True
                                                               gold = 5
                                                               strength = strength + 10
                                                               time.sleep(3)
                                                               print_with_delay(Colors.WHITE + f"You gain 10 strength. You now have {strength} strength.")
                                                               time.sleep(3)
                                                               print()
                                                               break
                                                        else:
                                                               print_with_delay(Colors.GREEN + "As you go over to loot the fallen neanderthal, the other one comes back. Seeing his comrade on the ground he becomes enraged, and you have no choice but to fight him.")
                                                               time.sleep(3)
                                                               neand_fight += 1
                                                               neanderthal_health = 100
                                                               continue
                                                 else:
                                                        world1ans7 = "run"
                                                        waterfall = True
                                                        break
                                          else:
                                                 world1ans7 = "run"
                                                 waterfall = True
                                                 break
                                   print_with_delay(Colors.GREEN + "Now it's the neanderthal's turn to take a swing at you.")
                                   time.sleep(3)
                                   print_with_delay("You must predict where the neanderthal is going to swing so you can dodge it.")
                                   time.sleep(3)
                                   swing = random.randint(1,2)
                                   print()
                                   world1ans6 = input(Colors.MAGENTA + "Will the neanderthal swing left or right? (left/right) ")
                                   time.sleep(1)
                                   if world1ans6 != "left" and world1ans6 != "right":
                                          world1ans6 = random.randint(1,2)
                                   print()
                                   if world1ans6 == "right" and swing == 1:
                                          print_with_delay(Colors.GREEN + "You evade the neanderthal's attack.")
                                          time.sleep(3)
                                   elif world1ans6 == "right" and swing == 2:
                                          print_with_delay(Colors.GREEN + "You get hit with the neanderthal's club.")
                                          time.sleep(3)
                                          global health
                                          health = health - 20
                                          print()
                                          print_with_delay(Colors.WHITE + f"Your health is now {health}.")
                                          time.sleep(3)
                                   elif world1ans6 == "left" and swing == 1:
                                          print_with_delay(Colors.GREEN + "You evade the neanderthal's attack.")
                                          time.sleep(3)
                                   elif world1ans6 == "left" and swing == 2:
                                          print_with_delay(Colors.GREEN + "You get hit with the neanderthal's club.")
                                          time.sleep(3)
                                          health = health - 20
                                          print()
                                          print_with_delay(Colors.WHITE + f"Your health is now {health}.")
                                          time.sleep(3)
                                   if health <= 0:
                                          print()
                                          print_with_delay(Colors.WHITE + "You died: you have perished from injuries due to a neanderthal attack.")
                                          print()
                                          time.sleep(3)
                                          the_end()
                                          quit()
                                   else:
                                          print()
                                          world1ans7 = input(Colors.MAGENTA + "Continue fighting or run away? (fight/run) ")
                                          time.sleep(1)
                                          print()
                                          if world1ans7 == "fight":
                                                 continue
                                          else:
                                                 break
                            if world1ans7 == "run":
                                   print_with_delay(Colors.GREEN + "You decide to flee the scene but then you accidentally slip and fall down a nearby waterfall.")
                                   time.sleep(3)
                                   water_dmg = random.randint(5, 10)
                                   waterfall = True
                            else:
                                   time.sleep(3)
                                   waterfall = True
             else:
                     print_with_delay(Colors.GREEN + "You don't have anything to give them so you shrug apologetically.")
                     time.sleep(3)
                     print_with_delay("The neanderthals are not pleased, so they pick you up and fling you down the nearby waterfall.")
                     time.sleep(3)
                     water_dmg = random.randint(5,20)
                     waterfall = True
       if waterfall:
              health -= water_dmg
              print()
              print_with_delay(Colors.WHITE + f"You fall down the waterfall and lose {water_dmg} health. You now have {health} health.")
              time.sleep(3)
              print()
              print_with_delay(Colors.GREEN + "After walking a little ways away from the waterfall, you find the toaster. It still has a piece of toast in it.")
              time.sleep(3)
              print()
              print_with_delay(Colors.BLUE + "Why did you bring me here? I can't even make any money because it hasn't been invented yet?")
              time.sleep(3)
              print()
              print_with_delay(Colors.RED + "There must have been a mistake somewhere in between the present and now. But don't worry, with just a twist of my knob, you can be whisked away back to the present.")
              time.sleep(3)
              print()
              global time1
              print_with_delay(Colors.CYAN + "Zroom!")
              time.sleep(3)
              cards_intro()
              print()
              return

def world2():
       global vip
       global jewelry
       global necklace
       global health
       global strength
       global money
       global world
       global world2_meter
       global time1
       global known_world2
       global won_status
       won_status = False
       known_world2 = "Casino"
       def roulette():
              global money
              global vip
              cont = True
              wins = 0
              while cont:
                     if money <= 0:
                            print()
                            print_with_delay(Colors.GREEN + f"Warning, you have ${money}!")
                            time.sleep(3)
                            print_with_delay("If you gain too much debt, you might get into trouble...")
                            time.sleep(3)
                            print()
                     else:
                            print_with_delay(Colors.GREEN + f"You have ${money}.")
                            time.sleep(3)
                     print()
                     cont = input(Colors.MAGENTA + "Play roulette? (yes/no) ")
                     time.sleep(1)
                     print()
                     if cont == "no":
                            return
                     wheel = random.randint(0,1)
                     rbet = int(input(Colors.MAGENTA + f"How much do you want to bet? "))
                     time.sleep(1)
                     print()
                     if rbet <= 0:
                            money += rbet
                            high_score()
                     else:
                            money -= rbet
                            high_score()
                     choice = random.randint(0,1)
                     if choice == 0:
                            choice = input("Bet on white or black? (white/black) ")
                            time.sleep(1)
                            print()
                     else:
                            choice = input("Bet on odds or evens? (odds/evens) ")
                            time.sleep(1)
                            print()
                     time.sleep(1)
                     if choice == "white" or choice == "odds" and wheel == 0:
                            print()
                            print_with_delay(Colors.WHITE + f"You win and earn ${rbet*2}.")
                            time.sleep(3)
                            print()
                            wins += 1
                            money += rbet*2
                            high_score()
                     elif choice == "black" or choice == "evens" and wheel == 1:
                            if rbet < 0:
                                   rbet -= rbet*2
                            print_with_delay(Colors.GREEN + f"You win and earn ${rbet * 2}.")
                            time.sleep(3)
                            wins += 1
                            money += bet*2
                            high_score()
                     else:
                            print()
                            print_with_delay(Colors.GREEN + "You don't win anything.")
                            time.sleep(3)
                            print()
                            wins -= 1
                     if wins >= 3:
                            vip = True
                            print()
                            print_with_delay(Colors.WHITE + "You gain a VIP pass for winning 3 times in a row.")
                            time.sleep(3)
                            print()
                            continue
                     else:
                            print()
                            print_with_delay(f"You've won {wins} times in a row.")
                            time.sleep(3)
                            print()
                            continue

       def poker():
              plhand = random.randint(1,18)
              if plhand == 1:
                     return "royal flush"
              else:
                     plhand = random.randint(1,16)
                     if plhand == 1:
                            return "straight flush"
                     else:
                            plhand = random.randint(1,14)
                            if plhand == 1:
                                   return "four of a kind"
                            else:
                                   plhand = random.randint(1,12)
                                   if plhand == 1:
                                          return "full house"
                                   else:
                                          plhand = random.randint(1,10)
                                          if plhand == 1:
                                                 return "flush"
                                          else:
                                                 plhand = random.randint(1,8)
                                                 if plhand == 1:
                                                        return "straight"
                                                 else:
                                                        plhand = random.randint(1,6)
                                                        if plhand == 1:
                                                               return "three of a kind"
                                                        else:
                                                               plhand = random.randint(1,4)
                                                               if plhand == 1:
                                                                      return "two pair"
                                                               else:
                                                                      plhand = random.randint(1,2)
                                                                      if plhand == 1:
                                                                             return "pair"
                                                                      else:
                                                                             return "high card"
       def blackjack():
              global won_status
              won_status = False
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
                     print()
                     print_with_delay(Colors.WHITE + f"Round {game_round}")
                     time.sleep(3)
                     print()
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
                            print()
                            hit_stand = input(Colors.MAGENTA + "Hit or stand? (hit/stand) ")
                            time.sleep(1)
                            print()
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
                                                 print()
                                                 print_with_delay("You win the round by holding 5 cards.")
                                                 won += 1
                                                 round_over = True
                                                 time.sleep(3)
                                                 break
                                          else:
                                                 continue
                                   if total > 21:
                                          if total > 21 and ace == 22:
                                                 print_with_delay("Your opponent accuses you of cheating and you get thrown in jail.")
                                                 time.sleep(7)
                                                 print()
                                                 prison("past")
                                                 return
                                          else:
                                                 print()
                                                 print_with_delay(Colors.WHITE + "You busted!")
                                                 time.sleep(3)
                                                 print()
                                                 lost += 1
                                                 round_over = True            
                                                 break
                            else:
                                   print_with_delay(Colors.WHITE + f"You stood with {total}.")
                                   time.sleep(3)
                                   print()
                                   opdone = False
                            if ace > 11:
                                   print()
                                   print_with_delay(Colors.GREEN + "Your opponent becomes suspicious of you holding aces.")
                                   time.sleep(3)
                                   print()
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
                                          print_with_delay(Colors.GREEN + f"Your opponent draws {opname}")
                                          time.sleep(3)
                                   else:
                                          print_with_delay(Colors.GREEN + f"Your opponent draws {opnum}.")
                                          time.sleep(3)
                                   if opace > 0 and optotal > 21:
                                          optotal -= 10
                                          print_with_delay(f"Their ace's value changes to 1 and their total is {optotal}.")
                                          opace -= 1
                                          time.sleep(3)
                                   if optotal > 21:
                                          print()
                                          print_with_delay(Colors.WHITE + "Your opponent has busted!")
                                          time.sleep(3)
                                          won += 1
                                          round_over = True
                                          break
                                   if opcard_num == 5:
                                          print()
                                          print_with_delay(Colors.WHITE + "Yor opponent wins the round by holding 5 cards.")
                                          lost += 1
                                          round_over = True
                                          time.sleep(3)
                                          continue
                            if total <= 21 and optotal <= 21:
                                   if optotal > total:
                                          print()
                                          print_with_delay(Colors.WHITE + "Your opponent has a higher value than you, so your opponent wins the round.")
                                          time.sleep(3)
                                          lost += 1
                                          round_over = True
                                          break
                                   elif total > optotal:
                                          print()
                                          print_with_delay(Colors.WHITE + "You have a higher value than your opponent, so you win the round.")
                                          time.sleep(3)
                                          won += 1
                                          round_over = True
                                          break
                                   else:
                                          print()
                                          print_with_delay(Colors.WHITE + "Your opponent wins due to a tie.")
                                          time.sleep(3)
                                          round_over = True
                                          lost += 1
                                          break
                     if won >= 3:
                            print()
                            print_with_delay(Colors.WHITE + "You beat your opponent.")
                            time.sleep(3)
                            print()
                            won_status = True
                            return
                     elif lost == 3:
                            print()
                            print_with_delay(Colors.WHITE + "You lost and were sent back to the lobby.")
                            time.sleep(3)
                            print()
                            won_status = False
                            return
                     else:
                            continue
       if world2_meter:
              print_with_delay(Colors.GREEN + "You're standing outside of the casino once again. This time the toaster is beside you.")
              time.sleep(3)
              print()
              world2ans0 = input(Colors.MAGENTA + "Go into the casino and earn some money or go back to the present? (casino/present) ")
              time.sleep(1)
              print()
              if world2ans0 == "present":
                     return
              else:
                     print_with_delay(Colors.GREEN + "You decide to go play some games.")
                     time.sleep(3)
                     print_with_delay(Colors.GREEN + "As you go into the building, you get spotted by some of the boss gambler's henchmen. They don't look too happy.")
                     time.sleep(3)
                     print()
                     print_with_delay(Colors.RED + "Hey, you're the guy who cheated the boss out of his shiny new toaster.")
                     time.sleep(3)
                     rand_jail = random.randint(1,2)
                     if rand_jail == 1 and strength < 20 or health <= rand_jail*10:
                            print()
                            print_with_delay(Colors.GREEN + "You get caught.")
                            time.sleep(3)
                            if necklace:
                                   print()
                                   world2ans70 = input(Colors.MAGENTA + f"Bribe the thugs with the {jewelry}? (yes/no) ")
                                   necklace = False
                                   time.sleep(1)
                                   print()
                                   if world2ans70 == "yes":
                                          print_with_delay(Colors.GREEN + f"You bribe the thugs with the {jewelry} and escape with the toaster back to the present.")
                                          time.sleep(3)
                                          print()
                                          print_with_delay(Colors.CYAN + "Zroom!")
                                          time.sleep(3)
                                          cards_intro()
                                          print()
                                          return
                                   else:
                                          print_with_delay(Colors.GREEN + "The thugs drag you away and throw you in jail.")
                                          time.sleep(7)
                                          print()
                                          prison("past")
                                          return
                     elif strength >= 20:
                            print_with_delay(Colors.GREEN + "Because of how strong you are, you beat them up.")
                            time.sleep(3)
                            health -= rand_jail*10
                            print_with_delay(f"You lose {rand_jail*10} health. Your health is now {health}.")
                            time.sleep(3)
                            print_with_delay("The thugs run off and take the golden toaster with them and give it back to the boss.")
                            time.sleep(3)
                            world = 2
                     else:
                            print_with_delay(Colors.GREEN + "You escape the thugs, but they steal the golden toaster and bring it back to the boss.")
                            time.sleep(3)
                            world = 2

       if world == 2:
              bj_won = False
              print_with_delay(Colors.GREEN + "You're standing outside of an old fashioned casino.")
              time.sleep(3)
              print()
              print_with_delay(Colors.BLUE + "I want to find the toaster.")
              time.sleep(3)
              print()
              choice1 = True
       else:
              return
       while choice1:
              world2ans1 = input(Colors.MAGENTA + "Go to the casino restaurant or game rooms? (restaurant/game) ")
              time.sleep(1)
              print()
              while world2ans1 == "game":
                     world2ans2 = input(Colors.MAGENTA + "Go into the blackjack room, or roulette room? (blackjack/roulette) ")
                     time.sleep(1)
                     print()
                     if cheat:
                            necklace = True
                            jewelry = "ring"
                            vip = True
                            world2ans2 = "blackjack"
                            bj_won = input("bj_won? (y/n) ")
                            if bj_won == "y":
                                   bj_won = True
                            else:
                                   bj_won = False
                     if world2ans2 == "blackjack" and bj_won:
                            print_with_delay(Colors.GREEN + "Nobody wants to play blackjack with you.")
                            time.sleep(3)
                            if not vip:
                                   print_with_delay("You need a VIP pass to enter the boss gambler's room.")
                                   time.sleep(3)
                                   print_with_delay("You go off in search of a VIP pass.")
                                   time.sleep(3)
                                   world2ans1 = "restaurant"
                     elif world2ans2 == "blackjack" and not bj_won:
                            print_with_delay(Colors.GREEN + "You go into the blackjack room and confront an important looking gambler")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.BLUE + "Have you by chance seen a golden toaster?")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.RED + "I might have, and I might not have, if you beat me in blackjack, I'll tell you what I know.")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.WHITE + "You must beat the gambler 3 times to win, if you lose 3 times, he won't give you any information.")
                            time.sleep(3)
                            print()
                            blackjack()
                            if not won_status:
                                   print_with_delay(Colors.GREEN + "You lose $50 for losing.")
                                   money -= 50
                                   time.sleep(3)
                                   if money < 0:
                                          print_with_delay(Colors.WHITE + f"You're ${money+money*2} are in debt!")
                                   break
                            else:
                                   print_with_delay(Colors.WHITE + "The gambler gives you $50 for winning.")
                                   money += 50
                                   high_score()
                                   time.sleep(3)
                                   print_with_delay(f"Your total money is now {money}.")
                                   time.sleep(3)
                                   print()
                                   print_with_delay(Colors.GREEN + "The gambler tells you that the boss gambler is going to gamble away the golden toaster, \nand instructs you to the room he'll be in.")
                                   time.sleep(3)
                                   bj_won = True
                                   if not vip:
                                          print_with_delay("You need a VIP pass to enter the boss gambler's room.")
                                          time.sleep(3)
                                          print_with_delay("You go off in search of a VIP pass.")
                                          time.sleep(3)
                                          world2ans1 = "restaurant"
                     if world2ans2 == "blackjack" and vip and bj_won:
                                          print_with_delay(Colors.GREEN + "You use your VIP pass to go onto the boss gambler's room.")
                                          time.sleep(3)
                                          print_with_delay("The boss gambler smirks as you enter and beckons for you to sit down.")
                                          time.sleep(3)
                                          print()
                                          print_with_delay(Colors.RED + "You gotta pay to enter kid.")
                                          time.sleep(3)
                                          print_with_delay(Colors.RED + "If you can beat me a few times, I may consider betting my cool new golden toaster...")
                                          time.sleep(3)
                                          poker_game = True
                                          won = 0
                                          toaster = False
                                          tie = False
                                          pool = 0
                                          rand_rounds = random.randint(3,5)
                                          while poker_game:
                                                 if not tie:
                                                        pool = 0
                                                 else:
                                                        tie = False
                                                 opraise = 0
                                                 raise_pool = 0
                                                 print()
                                                 print_with_delay(Colors.WHITE + f"You have ${money}.")
                                                 time.sleep(3)
                                                 print()
                                                 world2ans6 = input(Colors.MAGENTA + "Pay $5 to start round? (yes/no) ")
                                                 time.sleep(1)
                                                 print()
                                                 if world2ans6 == "yes":
                                                        money -= 5
                                                        print_with_delay(Colors.GREEN + "You bet $5.")
                                                        time.sleep(3)
                                                        pool += 5
                                                        if won >= rand_rounds:
                                                               print_with_delay("The boss puts the toaster in the betting pool.")
                                                               time.sleep(3)
                                                               toaster = True
                                                        else:
                                                               print_with_delay("The boss matches.")
                                                               time.sleep(3)
                                                               pool += 5
                                                        if money < 0:
                                                               print_with_delay("You are in debt!")
                                                               time.sleep(3)
                                                        print_with_delay("The boss starts the game of poker.")
                                                        time.sleep(3)
                                                        hand = poker()
                                                        print_with_delay(f"Your hand type is a {hand}.")
                                                        time.sleep(3)
                                                        print()
                                                        world2ans8 = input(Colors.MAGENTA + "Keep hand or redraw? (keep/draw) ")
                                                        time.sleep(1)
                                                        print()
                                                        if world2ans8 == "draw":
                                                               hand = poker()
                                                               print_with_delay(Colors.GREEN + f"Your hand type is a {hand}.")
                                                               time.sleep(3)
                                                        else:
                                                               print_with_delay(Colors.GREEN + "You keep your hand.")
                                                               time.sleep(3)
                                                        ophand = poker()
                                                        if ophand == "high card" or ophand == "pair" or ophand == "two pair":
                                                               print_with_delay("The boss redraws his hand.")
                                                               time.sleep(3)
                                                               ophand = poker()
                                                        if ophand == "royal flush" or ophand == "straight flush" or ophand == "four of a kind" or ophand == "three of a kind":
                                                               rand_pass = random.randint(1, 8)
                                                               if rand_pass == 1:
                                                                      print_with_delay("The boss checks.")
                                                                      time.sleep(3)
                                                                      print()
                                                                      world2ans7 = input(Colors.MAGENTA + "Match, raise, or fold? (match/raise/fold) ")
                                                                      time.sleep(1)
                                                                      print()
                                                               else:
                                                                      if ophand == "royal flush":
                                                                             opraise = random.randint(20, 50)
                                                                             pool += opraise
                                                                      elif ophand == "straight flush":
                                                                             opraise = random.randint(15, 40)
                                                                             pool += opraise
                                                                      elif ophand == "four of a kind":
                                                                             opraise = random.randint(10, 30)
                                                                             pool += opraise
                                                                      else:
                                                                             opraise = random.randint(5, 20)
                                                                             pool += opraise
                                                                      print_with_delay(Colors.GREEN + f"The boss raises by ${opraise}.")
                                                                      time.sleep(3)
                                                                      print_with_delay(f"The current pool is worth ${pool}.")
                                                                      time.sleep(3)
                                                                      print()
                                                                      world2ans7 = input(Colors.MAGENTA + "Match, raise, or fold? (match/raise/fold) ")
                                                                      time.sleep(1)
                                                                      print()
                                                        else:
                                                               bet = random.randint(1, 5)
                                                               if bet == 1:
                                                                      opraise = random.randint(5, 25)
                                                                      pool += opraise
                                                                      print_with_delay(Colors.GREEN + f"The boss raises by ${opraise}")
                                                                      time.sleep(3)
                                                               else:
                                                                      print_with_delay(Colors.GREEN + "The boss checks.")
                                                                      opraise = 0
                                                                      time.sleep(3)
                                                               print()
                                                               world2ans7 = input(Colors.MAGENTA + "Match, raise, or fold? (match/raise/fold) ")
                                                               time.sleep(1)
                                                               print()
                                                        if world2ans7 == "raise":
                                                               if money > 0 and money >= opraise:
                                                                      raise_func = True
                                                                      while raise_func:
                                                                             print()
                                                                             raise_pool = float(input(Colors.MAGENTA + f"How much do you want to raise by? (up to ${money}) "))
                                                                             time.sleep(1)
                                                                             print()
                                                                             if opraise < raise_pool <= money:
                                                                                    money -= raise_pool
                                                                                    pool += raise_pool
                                                                                    print_with_delay(Colors.GREEN + f"You raise by ${raise_pool}.")
                                                                                    time.sleep(3)
                                                                                    break
                                                                             else:
                                                                                    print_with_delay(Colors.GREEN + f"You can't bet more money than ${money}!")
                                                                                    time.sleep(3)
                                                                                    continue
                                                                      if ophand == "royal flush":
                                                                             raise_cap = 100
                                                                      elif ophand == "straight flush":
                                                                             raise_cap = 80
                                                                      elif ophand == "four of a kind":
                                                                             raise_cap = 70
                                                                      elif ophand == "full house":
                                                                             raise_cap = 60
                                                                      elif ophand == "flush":
                                                                             raise_cap = 50
                                                                      elif ophand == "straight":
                                                                             raise_cap = 40
                                                                      elif ophand == "three of a kind":
                                                                             raise_cap = 30
                                                                      else:
                                                                             raise_cap = 20
                                                                      if raise_pool < raise_cap: #and ophand == "royal flush" or ophand == "straight flush" or ophand == "four of a kind" or ophand == "full house" or ophand == "flush" or ophand == "straight" or ophand == "three of a kind" or ophand == "two pair":
                                                                             print_with_delay(Colors.GREEN + f"The boss matches with ${raise_pool - opraise}.")
                                                                             time.sleep(3)
                                                                             pool += raise_pool
                                                                      else:
                                                                             print_with_delay(Colors.GREEN + "The boss folds.")
                                                                             time.sleep(3)
                                                                             if won >= 5:
                                                                                    print()
                                                                                    print_with_delay(Colors.WHITE + f"You win the golden toaster and also ${pool}!")
                                                                                    time.sleep(3)
                                                                                    money += pool
                                                                                    high_score()
                                                                                    print()
                                                                                    break
                                                                             else:
                                                                                    money += pool
                                                                                    high_score()
                                                                                    pool = 0
                                                                                    won += 1
                                                                                    continue

                                                               else:
                                                                      print_with_delay(Colors.GREEN + "You can't raise, you have to have more than the bet to raise.")
                                                                      time.sleep(3)
                                                                      world2ans7 = input(Colors.MAGENTA + "Match or fold? ")
                                                                      time.sleep(1)
                                                                      if world2ans7 == "match":
                                                                             print_with_delay(Colors.GREEN + f"You match with ${opraise}.")
                                                                             time.sleep(3)
                                                                             pool += opraise
                                                                             money -= opraise
                                                                      else:
                                                                             print_with_delay(Colors.GREEN + "You folded!")
                                                                             time.sleep(3)
                                                                             print_with_delay(f"The boss takes the prize pool, worth ${pool}.")
                                                                             time.sleep(3)
                                                                             print()
                                                                             pool = 0
                                                                             continue
                                                        elif world2ans7 == "match":
                                                               raise_pool = 0
                                                               if pool == 10:
                                                                      print_with_delay(Colors.GREEN + "You check.")
                                                                      time.sleep(3)
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"You match with ${opraise}.")
                                                                      time.sleep(3)
                                                                      money -= opraise
                                                                      pool += opraise
                                                        else:
                                                               raise_pool = 0
                                                               print_with_delay(Colors.GREEN + "You folded!")
                                                               time.sleep(3)
                                                               print_with_delay(f"The boss takes the prize pool, worth ${pool}.")
                                                               time.sleep(3)
                                                               pool = 0
                                                               continue
                                                        if ophand == "royal flush":
                                                               if hand == "royal flush":
                                                                      print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print_with_delay(Colors.GREEN + f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "straight flush" and hand != "royal flush":
                                                               if hand == "straight flush":
                                                                      print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print_with_delay(Colors.GREEN + f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "four of a kind" and hand != "royal flush" and hand != "straight flush":
                                                               if hand == "four of a kind":
                                                                      print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print_with_delay(Colors.GREEN + f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "full house" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind":
                                                               if hand == "full house":
                                                                      print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print_with_delay(Colors.GREEN + f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "flush" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "flush":
                                                               if hand == "flush":
                                                                      print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print_with_delay(Colors.GREEN + f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "straight" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "flush":
                                                               if hand == "straight":
                                                                      print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print_with_delay(Colors.GREEN + f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "three of a kind" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "flush" and hand != "straight":
                                                               if hand == "three of a kind":
                                                                      print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print_with_delay(Colors.GREEN + f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "two pair" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "flush" and hand != "straight" and hand != "three of a kind":
                                                               if hand == "two pair":
                                                                      print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print_with_delay(Colors.GREEN + f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "pair" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "flush" and hand != "straight" and hand != "three of a kind" and hand != "two pair":
                                                               if hand == "pair":
                                                                      print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print_with_delay(Colors.GREEN + f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        elif ophand == "high card" and hand != "royal flush" and hand != "straight flush" and hand != "four of a kind" and hand != "full house" and hand != "flush" and hand != "straight" and hand != "three of a kind" and hand != "two pair" and hand != "pair":
                                                               if hand == "high card":
                                                                      print_with_delay(Colors.GREEN + "No one wins due to a tie, the pool stays for next round")
                                                                      time.sleep(3)
                                                                      tie = True
                                                                      continue
                                                               else:
                                                                      print_with_delay(Colors.GREEN + f"Your opponent wins the round, he had a {ophand}")
                                                                      time.sleep(3)
                                                                      print_with_delay(Colors.GREEN + f"He takes the pool, worth ${pool}.")
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                        else:
                                                               print_with_delay(Colors.GREEN + f"You win the round, your opponent had a {ophand}.")
                                                               won += 1
                                                               time.sleep(3)
                                                               if toaster:
                                                                      print()
                                                                      print_with_delay(Colors.WHITE + "You win the toaster.")
                                                                      time.sleep(3)
                                                                      print()
                                                                      won = True
                                                                      break
                                                               else:
                                                                      print_with_delay(Colors.WHITE + f"You take the pool, worth ${pool}.")
                                                                      money += pool
                                                                      high_score()
                                                                      time.sleep(3)
                                                                      pool = 0
                                                                      continue
                                                 else:
                                                        print_with_delay(Colors.GREEN + "You get up and go back to the lobby.")
                                                        time.sleep(3)
                                                        won = False
                                                        break
                                          if won:
                                                 print_with_delay(Colors.RED + "Hey kid, thanks for winning me.")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.BLUE + "Why did you take me here?")
                                                 time.sleep(3)
                                                 print()
                                                 if money < 0:
                                                        print_with_delay(Colors.RED + f"Well, I assumed you were going to make some money, but instead you somehow are in debt ${money-money*2}!")
                                                        time.sleep(3)
                                                        print()
                                                 else:
                                                        print_with_delay(Colors.RED + f"Well, to make money of course, look: you made ${money}!")
                                                        time.sleep(3)
                                                        print()
                                                 print_with_delay(Colors.BLUE + "Can we leave now?")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.RED + "Sure.")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.CYAN + "Zroom!")
                                                 time.sleep(3)
                                                 cards_intro()
                                                 print()
                                                 time1 = "present"
                                                 world2_meter = True
                                                 return
                                          else:
                                                 continue
                     else:
                            print_with_delay(Colors.GREEN + "You go into the roulette room.")
                            time.sleep(3)
                            print_with_delay("There's no information about the golden toaster.")
                            time.sleep(3)
                            print_with_delay("You notice a VIP pass you could win.")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.BLUE + "Since I'm here anyways, I could play a few rounds of roulette.")
                            time.sleep(3)
                            print()
                            world2ans5 = input(Colors.MAGENTA + "Stay and play roulette or go look for the toaster? (stay/leave) ")
                            time.sleep(1)
                            print()
                            if world2ans5 == "stay":
                                   roulette()
                            else:
                                   continue
              if world2ans1 == "restaurant":
                     print_with_delay(Colors.GREEN + "You decide to go to the restaurant.")
                     time.sleep(3)
                     print()
                     world2ans2 = input(Colors.MAGENTA + "Go into the kitchen or search around the dining area? (kitchen/dining) ")
                     time.sleep(1)
                     print()
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
                                   print()
                                   steal = input(Colors.MAGENTA + "Steal the piece of jewelry? (yes/no) ")
                                   time.sleep(1)
                                   print()
                                   if steal == "yes":
                                          print_with_delay(Colors.GREEN + f"You grab the {jewelry} and stuff it into your pocket.")
                                          necklace = True
                                          time.sleep(3)
                                          print_with_delay("Someone sees you steal the necklace, and comes over to confront you.")
                                          time.sleep(3)
                                          print()
                                          world2ans3 = input(Colors.MAGENTA + "Attempt to start a food fight or wait for them to come to you. (food/wait) ")
                                          time.sleep(1)
                                          print()
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
                                                 print()
                                                 lie = input(Colors.MAGENTA + "Lie about the necklace belonging to your or tell the truth? (lie/truth) ")
                                                 time.sleep(1)
                                                 print()
                                                 if lie == "lie":
                                                        print_with_delay(Colors.GREEN + f"You lie about the {jewelry}.")
                                                        time.sleep(3)
                                                        print_with_delay("The person believes you and goes back to their table.")
                                                        time.sleep(3)
                                                 else:
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
                            print()
                            world2ans4 = input(Colors.MAGENTA + "Go into the kitchen or go back to the lobby? (kitchen/lobby) ")
                            time.sleep(1)
                            print()
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
                            print()
                            world2ans3 = input(Colors.MAGENTA + "Do you want to make bread, spaghetti, or a creme pie? (bread/spaghetti/pie) ")
                            time.sleep(1)
                            print()
                            goodbake = True
                            if world2ans3 == "bread":
                                   print_with_delay(Colors.GREEN + "You decide to make bread.")
                                   time.sleep(3)
                                   print()
                                   flour = input(Colors.MAGENTA + "What is one main ingredient in bread that starts with f? ")
                                   time.sleep(1)
                                   print()
                                   if flour == "flour":
                                          goodbake = True
                                   else:
                                          goodbake = False
                                   if goodbake:
                                          salt = input("What is one main ingredient in bread that starts with s? ")
                                          time.sleep(1)
                                          print()
                                          if salt == "salt" or salt == "sugar":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          yeast = input("What is one main ingredient in bread that starts with y? ")
                                          time.sleep(1)
                                          print()
                                          if yeast == "yeast":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          water = input("What is one main ingredient in bread that starts with w? ")
                                          time.sleep(1)
                                          print()
                                          if water == "water" or water == "wheat":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                            elif world2ans3 == "spaghetti":
                                   print_with_delay(Colors.GREEN + "You decide to make spaghetti.")
                                   time.sleep(3)
                                   print()
                                   noodles = input(Colors.MAGENTA + "What is one main ingredient in spaghetti that starts with n? ")
                                   time.sleep(1)
                                   print()
                                   if noodles == "noodles" or noodles == "noodle":
                                          goodbake = True
                                   else:
                                          goodbake = False
                                   if goodbake:
                                          tomato = input("What is one main ingredient in spaghetti that starts with s? ")
                                          time.sleep(1)
                                          print()
                                          if tomato == "sauce" or tomato == "salt":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          meat = input("What is one main ingredient in spaghetti that starts with m? ")
                                          time.sleep(1)
                                          print()
                                          if meat == "meat" or meat == "meatball" or meat == "meatballs":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          cheese = input("What is one main ingredient in spaghetti that starts with c? ")
                                          time.sleep(1)
                                          print()
                                          if cheese == "cheese":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                            else:
                                   print_with_delay(Colors.GREEN + "You decide to make a creme pie.")
                                   time.sleep(3)
                                   print()
                                   milk = input(Colors.MAGENTA + "What is one main ingredient in creme pie that starts with m? ")
                                   time.sleep(1)
                                   print()
                                   if milk == "milk":
                                          goodbake = True
                                   else:
                                          goodbake = False
                                   if goodbake:
                                          cream = input("What is one main ingredient in creme pie that starts with c? ")
                                          time.sleep(1)
                                          print()
                                          if cream == "creme" or cream == "cream" or cream == "crust" or cream == "custard":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          sugar = input("What is one main ingredient in creme pie that starts with s? ")
                                          time.sleep(1)
                                          print()
                                          if sugar == "sugar":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                                   if goodbake:
                                          eggs = input("What is one main ingredient in creme pie that starts with e? ")
                                          time.sleep(1)
                                          print()
                                          if eggs == "egg" or eggs == "eggs":
                                                 goodbake = True
                                          else:
                                                 goodbake = False
                            
                            if goodbake:
                                   print_with_delay(Colors.GREEN + "The chefs are impressed in your skills. One of them saw a golden shaped toaster object being taken into one of the game rooms by a gambler.")
                                   time.sleep(3)
                                   print()
                                   print_with_delay(Colors.WHITE + "Before you leave, they give you a VIP pass.")
                                   vip = True
                                   time.sleep(3)
                                   print()
                                   world2ans1 = "game"
                                   time.sleep(3)
                                   world = False
                                   world2()
                                   continue
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
              
def world3(idol):
       global clay_statue
       global strength
       global health
       global money
       global open_door
       global gold
       global anvil
       global robot
       global known_world3
       known_world3 = "Ancient Egypt"
       if cheat:
              clay_statue = 1
       if world == 3:
              print_with_delay(Colors.GREEN + "You find yourself out in the desert with some pyramids in front of you.")
              time.sleep(3)
              print_with_delay("The toaster is nowhere to be seen.")
              time.sleep(3)
              inside_pyramid = True
              print_with_delay("You walk inside one of the pyramids.")
              time.sleep(3)
              print_with_delay("There's a split in the passage.")
              while inside_pyramid:
                     print()
                     world3ans1 = input(Colors.MAGENTA + "Go right or left? (left/right) ")
                     time.sleep(1)
                     print()
                     if world3ans1 == "right":
                            print_with_delay(Colors.GREEN + "You decide to go right.")
                            time.sleep(3)
                            if not open_door:
                                   print_with_delay(Colors.GREEN + "There's a big slab of sandstone blocking the path with an indent for a small clay statue.")
                                   time.sleep(3)
                                   if robot == "charged":
                                          print()
                                          world3ans2 = input(Colors.MAGENTA + "Insert the companion robot into the slot? (yes/no) ")
                                          time.sleep(1)
                                          robot = False
                                          if world3ans2 == "yes":
                                                 print()
                                                 print_with_delay(Colors.GREEN + "You insert the robot into the slot.")
                                                 time.sleep(5)
                                                 print_with_delay("The door slides open, revealing a glowing white portal behind it.")
                                                 time.sleep(5)
                                                 print_with_delay("You hear whisperings from the portal, urging you to enter.")
                                                 time.sleep(5)
                                                 print()
                                                 end_game = input(Colors.MAGENTA + "Go into the portal? (yes/no) ")
                                                 time.sleep(2)
                                                 print()
                                                 if end_game == "yes":
                                                        print_with_delay(Colors.GREEN + "You step into the portal.")
                                                        time.sleep(5)
                                                        print_with_delay("And that's where your adventures really begins.")
                                                        time.sleep(5)
                                                        print()
                                                        the_end()
                                                 else:
                                                        print_with_delay(Colors.GREEN + "You step away and try to go back the way you came, except the path now blocked by a slab of sandstone.")
                                                        time.sleep(5)
                                                        print_with_delay("The portal flickers out as the ground starts to rumble.")
                                                        time.sleep(5)
                                                        print_with_delay("Parts of the ceiling start collapsing on top of you.")
                                                        time.sleep(5)
                                                        print_with_delay("Soon you are buried in rubble.")
                                                        time.sleep(5)
                                                        print()
                                                        print_with_delay(Colors.WHITE + "You Died: You have perished from a mysterious cave in.")
                                                        time.sleep(5)
                                                        print()
                                                        print_with_delay(Colors.GREEN + "In 4500 years, your skeleton will be discovered in one of the pyramids and scientists will wonder how you got there...")
                                                        time.sleep(5)
                                                        print()
                                                        the_end()
                                   if clay_statue or idol >= 1:
                                          print()
                                          world3ans2 = input(Colors.MAGENTA + "Insert the clay statue into the slot? (yes/no) ")
                                          time.sleep(1)
                                          if world3ans2 == "yes":
                                                 print()
                                                 open_door = True
                                                 clay_statue -= 1
                                                 print_with_delay(Colors.GREEN + "You insert the statue and the sandstone block slides to the side.")
                                                 time.sleep(3)
                                                 gold += 200
                                                 print()
                                                 print_with_delay(Colors.WHITE + f"Inside the room you find 200 chunks of gold, you now have {gold} gold.")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.GREEN + "You go back to the beginning of the maze.")
                                                 time.sleep(3)
                                                 continue
                                   if strength > 30:
                                          print()
                                          world3ans2 = input(Colors.MAGENTA + "Use brute force to move the slab aside? (yes/no) ")
                                          time.sleep(1)
                                          if world3ans2 == "yes":
                                                 print()
                                                 open_door = True
                                                 print_with_delay(Colors.GREEN + "You drag the rock out of the way and enter the chamber.")
                                                 time.sleep(3)
                                                 gold += 200
                                                 print()
                                                 print_with_delay(Colors.WHITE + f"Inside the room you find 200 chunks of gold, you now have {gold} gold.")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.GREEN + "You go back to the beginning of the maze.")
                                                 time.sleep(3)
                                                 continue
                                   print()
                                   print_with_delay(Colors.GREEN + "You can't figure out how to get past, so you go back to the beginning of the maze.")
                                   time.sleep(3)
                                   continue
                            else:
                                   if robot == "charged":
                                          print_with_delay(Colors.GREEN + "There's a big slab of sandstone blocking the path with an indent for a small clay statue.")
                                          time.sleep(3)
                                          print()
                                          world3ans2 = input(Colors.MAGENTA + "Insert the companion robot into the slot? (yes/no) ")
                                          time.sleep(1)
                                          robot = False
                                          if world3ans2 == "yes":
                                                 print()
                                                 print_with_delay(Colors.GREEN + "You insert the robot into the slot.")
                                                 time.sleep(5)
                                                 print_with_delay("The door slides open, revealing a glowing white portal behind it.")
                                                 time.sleep(5)
                                                 print_with_delay("You hear whisperings from the portal, urging you to enter.")
                                                 time.sleep(5)
                                                 print()
                                                 end_game = input(Colors.MAGENTA + "Go into the portal? (yes/no) ")
                                                 time.sleep(2)
                                                 print()
                                                 if end_game == "yes":
                                                        print_with_delay(Colors.GREEN + "You step into the portal.")
                                                        time.sleep(5)
                                                        print_with_delay("And that's where your adventures really begins.")
                                                        time.sleep(5)
                                                        print()
                                                        the_end()
                                                 else:
                                                        print_with_delay(Colors.GREEN + "You step away and try to go back the way you came, except the path now blocked by a slab of sandstone.")
                                                        time.sleep(5)
                                                        print_with_delay("The portal flickers out as the ground starts to rumble.")
                                                        time.sleep(5)
                                                        print_with_delay("Parts of the ceiling start collapsing on top of you.")
                                                        time.sleep(5)
                                                        print_with_delay("Soon you are buried in rubble.")
                                                        time.sleep(5)
                                                        print()
                                                        print_with_delay(Colors.WHITE + "You Died: You have perished from a mysterious cave in.")
                                                        time.sleep(5)
                                                        print()
                                                        print_with_delay(Colors.GREEN + "In 4500 years, your skeleton will be discovered in one of the pyramids and scientists will wonder how you got there...")
                                                        time.sleep(5)
                                                        print()
                                                        the_end()
                                   else:
                                          print_with_delay(Colors.GREEN + "The chamber is empty.")
                                          time.sleep(3)
                                          continue
                     else:
                            print_with_delay(Colors.GREEN + "You decide to go left.")
                            time.sleep(3)
                            print_with_delay("You come up to another split.")
                            time.sleep(3)
                            print()
                            world3ans3 = input(Colors.MAGENTA + "Go left or right? (left/right) ")
                            time.sleep(1)
                            print()
                            if world3ans3 == "right":
                                   print_with_delay(Colors.GREEN + "You decide to go right.")
                                   time.sleep(3)
                                   print_with_delay("You floor falls out beneath you into a bed of wooden spikes!")
                                   time.sleep(3)
                                   dmg = random.randint(1,30)
                                   if health <= dmg:
                                          print()
                                          print_with_delay(Colors.WHITE + "You Died: You have perished from falling into a pit of spikes.")
                                          time.sleep(3)
                                          print()
                                          the_end()
                                          quit()
                                   health -= dmg
                                   print_with_delay(f"Luckily, the spikes are dull and you only take {dmg} damage, your health is now {health}.")
                                   time.sleep(3)
                                   print_with_delay("You get out of the pit and go back to the beginning of the maze.")
                                   time.sleep(3)
                                   continue
                            else:
                                   print_with_delay(Colors.GREEN + "You decide to go left.")
                                   time.sleep(3)
                                   print_with_delay("You come up to another split.")
                                   time.sleep(3)
                                   print()
                                   world3ans4 = input(Colors.MAGENTA + "Go left or right? (left/right) ")
                                   time.sleep(1)
                                   print()
                                   if world3ans4 == "right":
                                          print_with_delay(Colors.GREEN + "You decide to go right.")
                                          time.sleep(3)
                                          print_with_delay("Part of the ceiling collapses on you!")
                                          time.sleep(3)
                                          dmg = random.randint(1, 30)
                                          if health <= dmg:
                                                 print()
                                                 print_with_delay(Colors.WHITE + "You Died: You have perished from a cave in.")
                                                 time.sleep(3)
                                                 print()
                                                 the_end()
                                                 quit()
                                          health -= dmg
                                          print_with_delay(f"Luckily, only a bit of the ceiling collapsed and you only take {dmg} damage, your health is now {health}.")
                                          time.sleep(3)
                                          print_with_delay("You dig yourself out of the rubble and go back to the beginning of the maze.")
                                          time.sleep(3)
                                          continue
                                   else:
                                          print_with_delay(Colors.GREEN + "You decide to go left.")
                                          time.sleep(3)
                                          print_with_delay("You come up to another split.")
                                          time.sleep(3)
                                          print()
                                          world3ans5 = input(Colors.MAGENTA + "Go left or right? (left/right) ")
                                          time.sleep(1)
                                          print()
                                          if world3ans5 == "left" and not anvil:
                                                 print_with_delay(Colors.GREEN + "You decide to go left.")
                                                 time.sleep(3)
                                                 print_with_delay("An anvil falls from the ceiling and hits you on the head!")
                                                 time.sleep(3)
                                                 dmg = random.randint(1, 30)
                                                 if health <= dmg:
                                                        print()
                                                        print_with_delay(Colors.WHITE + "You Died: You have perished from a falling anvil.")
                                                        time.sleep(3)
                                                        print()
                                                        the_end()
                                                        quit()
                                                 health -= dmg
                                                 print_with_delay(f"Luckily, the anvil was small and you only take {dmg} damage, your health is now {health}.")
                                                 time.sleep(3)
                                                 print()
                                                 strength += 20
                                                 print_with_delay(Colors.WHITE + f"You take the anvil and gain 20 strength. You now have {strength} total strength.")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.GREEN + "You go back to the beginning of the maze.")
                                                 anvil = True
                                                 time.sleep(3)
                                                 continue
                                          elif world3ans5 == "left" and anvil:
                                                 print_with_delay(Colors.GREEN + "It's a dead end. You go back to the beginning of the maze.")
                                                 time.sleep(3)
                                                 continue
                                          else:
                                                 print_with_delay(Colors.GREEN + "You decide to go right.")
                                                 time.sleep(3)
                                                 print_with_delay("You enter the burial chamber.")
                                                 time.sleep(3)
                                                 print_with_delay("A slab of sandstone slides shut behind you, blocking the exit.")
                                                 time.sleep(3)
                                                 print()
                                                 gold += 50
                                                 print_with_delay(Colors.WHITE + f"You find 50 gold. You now have {gold} gold.")
                                                 time.sleep(3)
                                                 world3ans6 = "no"
                                                 while world3ans6 == "no":
                                                        print()
                                                        world3ans6 = input(Colors.MAGENTA + "Open the coffin? (yes/no) ")
                                                        time.sleep(1)
                                                        print()
                                                        if world3ans6 == "no":
                                                               print_with_delay(Colors.GREEN + "There's nothing else besides the coffin.")
                                                               time.sleep(3)
                                                               continue
                                                 print_with_delay(Colors.GREEN + "You decide to open the coffin.")
                                                 time.sleep(3)
                                                 print_with_delay("Inside the coffin is the golden toaster.")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.BLUE + "Quick, lets get out of here, this place gives me the heebie jeebies.")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.RED + "As you wish...")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.CYAN + "Zroom!")
                                                 time.sleep(3)
                                                 cards_intro()
                                                 print()
                                                 return
def world4():
       global money
       global health
       global strength
       global known_bitcoin
       global buy_bitcoin
       global known_world4
       known_world4 = "2010"
       if world == 4:
              print_with_delay(Colors.GREEN + "You yourself seemingly in the present.")
              time.sleep(3)
              print_with_delay("When you go to check the date on your computer, you realise it's 2010.")
              time.sleep(3)
              print_with_delay("You open a drawer on your computer desk and find the toaster.")
              time.sleep(3)
              print()
              print_with_delay(Colors.RED + "Thanks for freeing me, now get to work.")
              time.sleep(3)
              print()
              print_with_delay(Colors.BLUE + "What do you want me to get to work on?")
              time.sleep(3)
              print()
              print_with_delay(Colors.RED + "It's the perfect time to buy Bitcoin!")
              time.sleep(3)
              print()
              world4ans1 = input(Colors.MAGENTA + "Buy Bitcoin or go home? (buy/home) ")
              time.sleep(1)
              if world4ans1 == "home":
                     print()
                     print_with_delay(Colors.BLUE + "Please, take me back to the present. I'm not interesting in Bitcoin right now.")
                     time.sleep(3)
                     print()
                     print_with_delay(Colors.RED + "Fine, but your missing out on a lot of money...")
                     time.sleep(3)
                     print()
                     print_with_delay(Colors.YELLOW + "Zroom!")
                     time.sleep(3)
                     cards_intro()
                     print()
                     return
              else:
                     buying = True
                     while buying:
                            if money > 0:
                                   print()
                                   buy_bitcoin = float(input(Colors.MAGENTA + "How many shares of Bitcoin do you want to buy? (1 share = $0.05) "))
                                   time.sleep(1)
                                   print()
                                   if buy_bitcoin*.05 > money:
                                          print_with_delay(Colors.GREEN + f"You can't buy that much Bitcoin, you don't have enough money. (max shares = {money/.05})")
                                          time.sleep(3)
                                   else:
                                          money -= buy_bitcoin*.05
                                          print_with_delay(Colors.WHITE + f"You bought {buy_bitcoin} shares worth ${buy_bitcoin*.05}.")
                                          time.sleep(3)
                                          print()
                                          print_with_delay(Colors.GREEN + f"You have ${money} left.")
                                          time.sleep(3)
                                   print()
                                   if buy_bitcoin > 0:
                                          known_bitcoin += 1
                                   world4ans2 = input(Colors.MAGENTA + "Continue buying Bitcoin? (yes/no) ")
                                   time.sleep(1)
                                   if world4ans2 == "no":
                                          print()
                                          print_with_delay(Colors.RED + "Alright, lets go back and see how much money your bitcoin made.")
                                          time.sleep(3)
                                          print()
                                          print_with_delay(Colors.CYAN + "Zroom!")
                                          time.sleep(3)
                                          cards_intro()
                                          print()
                                          return
                                   else:
                                          continue
                            else:
                                   print()
                                   print_with_delay(Colors.BLUE + "Wait, I can't buy any Bitcoin, I don't have any money.")
                                   time.sleep(3)
                                   print()
                                   print_with_delay(Colors.RED + "Well, that's a shame, I guess we just have to go back to the present without any more Bitcoin.")
                                   time.sleep(3)
                                   print()
                                   print_with_delay(Colors.CYAN + "Zroom!")
                                   time.sleep(3)
                                   cards_intro()
                                   print()
                                   return
def world5():
       global lottery
       global food
       global money
       global health
       global strength
       global known_lotto
       global sick
       global world5counter
       global known_world5
       global save_food
       global food_type
       food_type = random.randint(1,7)
       if food_type == 1:
              food_type = "a banana"
       elif food_type == 2:
              food_type = "a cucumber"
       elif food_type == 3:
              food_type = " some leftover spaghetti"
       elif food_type == 4:
              food_type = "a twinkie"
       elif food_type == 5:
              food_type = "half a pint of ice cream"
       else:
              food_type = " some tater tots"
       known_world5 = "Tomorrow"
       lottery = random.randint(10000, 99999)
       if world == 5:
              if world5counter > 0 or cheat:
                     if cheat:
                            print(lottery)
                            known_lotto = True
                     print_with_delay(Colors.GREEN + "You find yourself one day in the future.")
                     time.sleep(3)
                     print_with_delay("The toaster is right next to you.")
                     time.sleep(3)
                     world5ans0 = input(Colors.MAGENTA + "Go outside, or go back to the present? (outside/present) ")
                     time.sleep(1)
                     if world5ans0 == "outside":
                            print_with_delay(Colors.GREEN + "You decide to go outside.")
                            time.sleep(3)
                            print_with_delay("Outside, you see a billboard displaying the winning lottery numbers for yesterday.")
                            time.sleep(3)
                            known_lotto = True
                            print_with_delay(f"The winning ticket is {lottery}.")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.BLUE + "This may be handy to remember for later.")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.GREEN + "You decide to go back to the present.")
                            time.sleep(3)
                            print_with_delay("Before you leave, your future self comes into the apartment.")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.CYAN + "Hey, before you leave, I got a warning for you. Don't win the lottery too much or bad things will happen...")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.CYAN + "Zroom!")
                            time.sleep(3)
                            cards_intro()
                            print()
                            return
                     else:
                            print_with_delay(Colors.CYAN + "Zroom!")
                            time.sleep(3)
                            cards_intro()
                            print()
                            return
              else:
                     print()
                     world5counter += 1
                     print_with_delay(Colors.GREEN + "You find yourself seemingly in the present.")
                     time.sleep(3)
                     print_with_delay("The toaster is nowhere to be seen.")
                     time.sleep(3)
                     search_apartment = 0
                     while world == 5:
                            print()
                            world5ans1 = input(Colors.MAGENTA + "Go outside, or search around your apartment? (outside/inside) ")
                            time.sleep(1)
                            print()
                            if world5ans1 == "inside":
                                   search_apartment += 1
                                   if search_apartment == 1:
                                          print_with_delay(Colors.GREEN + "You decide to look around your apartment.")
                                          time.sleep(3)
                                          print_with_delay(Colors.GREEN + "As you look around you find your old computer.")
                                          time.sleep(3)
                                          print()
                                          print_with_delay(Colors.BLUE + "According to the computer, I'm only one day in the future.")
                                          time.sleep(3)
                                          print_with_delay("I wonder why the toaster brought me here?")
                                          time.sleep(3)
                                          print()
                                   elif search_apartment == 2:
                                          money += 20
                                          print_with_delay(Colors.WHITE + f"You find $20 in coins stuffed between your sofa cushions. You now have ${money}.")
                                          time.sleep(3)
                                          high_score()
                                   elif search_apartment == 3:
                                          print_with_delay(Colors.GREEN + "You find the fridge.")
                                          time.sleep(3)
                                          print()
                                          world5ans2 = input(Colors.MAGENTA + "Eat some food? (yes/no) ")
                                          time.sleep(1)
                                          print()
                                          if world5ans2 == "yes":
                                                 food = random.randint(5,20)
                                                 health += food
                                                 high_score()
                                                 print_with_delay(Colors.GREEN + f"The food tasted funky, but your health was restored by {food} and is now {health}.")
                                                 time.sleep(3)
                                                 sick = True
                                                 continue
                                          else:
                                                 if not food > 0:
                                                        save_food = input(Colors.MAGENTA + f"Put {food_type} in your pocket? (yes/no) ")
                                                        time.sleep(1)
                                                        print()
                                                        if save_food == "yes":
                                                               save_food += 1
                                                               print_with_delay(Colors.GREEN + f"You put {food_type} in your pocket.")
                                                               time.sleep(3)
                                                 else:
                                                        print_with_delay(Colors.BLUE + "My fridge is broken, so I'll probably get sick if I eat anything.")
                                                        time.sleep(3)
                                                        continue
                                   else:
                                          print_with_delay(Colors.GREEN + "As you search, you start to realize your home is really dirty.")
                                          time.sleep(3)
                                          print()
                                          world5ans3 = input(Colors.MAGENTA + "Clean up your home? (yes/no) ")
                                          time.sleep(1)
                                          print()
                                          if world5ans3 == "yes":
                                                 print_with_delay(Colors.GREEN + "You decide to take a break and clean.")
                                                 time.sleep(3)
                                                 if strength < 10 < health:
                                                        print()
                                                        print_with_delay(Colors.BLUE + "Whew! I'm sore from all that cleaning!")
                                                        time.sleep(3)
                                                        print()
                                                        health -= 10
                                                        strength += 10
                                                        print_with_delay(Colors.WHITE + f"You lose 10 health and gain 3 strength, you now have {health} health and {strength} strength.")
                                                        time.sleep(3)
                                                        print()
                                                 else:
                                                        print_with_delay(Colors.GREEN + "The apartment looks a lot nicer than it did before.")
                                                        time.sleep(3)
                                                 print_with_delay(Colors.GREEN + "When you open a closet to clean it, the toaster falls out.")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.RED + "Peekaboo!")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.BLUE + "Why did you bring me here?")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.RED + "Well, to teach you a lesson for not keeping your home clean, and also something else and if you know, you know.")
                                                 time.sleep(3)
                                                 print_with_delay("Let's go back now.")
                                                 time.sleep(3)
                                                 print()
                                                 print_with_delay(Colors.CYAN + "Zroom!")
                                                 time.sleep(3)
                                                 cards_intro()
                                                 return
                            else:
                                   if not known_lotto:
                                          print_with_delay(Colors.GREEN + "You decide to go outside.")
                                          time.sleep(3)
                                          print_with_delay("Outside, you see a billboard displaying the winning lottery numbers for yesterday.")
                                          time.sleep(3)
                                          known_lotto = True
                                          print_with_delay(f"The winning ticket is {lottery}.")
                                          time.sleep(3)
                                          print()
                                          print_with_delay(Colors.BLUE + "This may be handy to remember for later.")
                                          time.sleep(3)
                                          print()
                                          print_with_delay(Colors.GREEN + "You decide to go back inside.")
                                          time.sleep(3)
                                   else:
                                          print_with_delay(Colors.GREEN + "There's nothing out of the ordinary outside.")
                                          time.sleep(3)
                                          continue

def world6():
       global health
       global strength
       global money
       global iphone
       global vr
       global robot
       global known_world6
       known_world6 = "Far Future"
       if world == 6:
              taxi = 0
              print_with_delay(Colors.GREEN + "You find yourself in a sci-fi futuristic city. You must have gone far into the future.")
              time.sleep(3)
              print_with_delay("The toaster is nowhere to be seen.")
              time.sleep(3)
              while world == 6:
                     print()
                     world6ans1 = input(Colors.MAGENTA + "Go search in the museum or tech store? (museum/tech) ")
                     time.sleep(1)
                     print()
                     if world6ans1 >= 5:
                            print_with_delay(Colors.GREEN + "The taxi robot's mind short circuits because it can't figure out why your taking the taxi so much. You crash and die.")
                            time.sleep(3)
                            print_with_delay(Colors.WHITE + "You Died: Your taxi crashed because you rode it too much.")
                            time.sleep(3)
                            print()
                            the_end()
                     if world6ans1 == "museum":
                            taxi += 1
                            money -= 2
                            print_with_delay(Colors.GREEN + f"You decide to take a flying taxi for $2 to get to the museum. You now have ${money}.")
                            time.sleep(3)
                            print_with_delay("As you wander through the exhibits, you notice the toaster in one of the displays titled 'ancient kitchen artifacts'.")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.BLUE + "I'll probably get in trouble if I stick around too long after freeing the toaster.")
                            time.sleep(3)
                            print()
                            world6ans2 = input(Colors.MAGENTA + "Steal the toaster or leave the museum? (steal/leave) ")
                            time.sleep(1)
                            print()
                            if world6ans2 == "steal":
                                   print_with_delay(Colors.GREEN + "You decide to steal the toaster.")
                                   time.sleep(3)
                                   print_with_delay("You press the button that turns off the laser display case and grab the toaster.")
                                   time.sleep(3)
                                   print_with_delay("Throughout the museum, alarms start blaring.")
                                   time.sleep(3)
                                   print()
                                   print_with_delay(Colors.RED + "Thanks for rescuing me, now lets skedaddle out of here before we get caught.")
                                   time.sleep(3)
                                   print()
                                   world6ans3 = input(Colors.MAGENTA + "Skedaddle back to the present? (yes/no) ")
                                   time.sleep(1)
                                   print()
                                   if world6ans3 == "yes":
                                          print_with_delay(Colors.CYAN + "Zroom!")
                                          time.sleep(3)
                                          cards_intro()
                                          return
                                   else:
                                          print_with_delay(Colors.GREEN + "You get caught by the guards and sent to future jail.")
                                          time.sleep(7)
                                          print()
                                          prison("future")
                                          return
                            else:
                                   print_with_delay(Colors.GREEN + "You decide to leave the museum.")
                                   time.sleep(3)
                                   continue
                     else:
                            taxi += 1
                            money -= 2
                            print_with_delay(Colors.GREEN + f"You decide to take a flying taxi for $2 to get to the tech shop. You now have ${money}.")
                            time.sleep(3)
                            #iphone80, vr contact lenses, robot companion
                            print_with_delay("You enter the tech shop and inspect some items for sale.")
                            time.sleep(3)
                            if money < 100:
                                   print_with_delay("You can't afford anything in the shop. (minimum purchase = $100)")
                                   time.sleep(3)
                                   print_with_delay("You leave the store.")
                                   time.sleep(3)
                                   continue
                            else:
                                   tech_shop = True
                            print()
                            while tech_shop:
                                   if iphone and vr and robot:
                                          print_with_delay(Colors.GREEN + "You bought everything that's for sale. You leave the store.")
                                          time.sleep(3)
                                          break
                                   world6ans3 = int(input(Colors.MAGENTA + "\n1. iPhone 96 - $5000\n2. VR Contact Lenses - $500,000\n3. Robot Companion - $50,000,000\n4. Nothing\nWhat do you want to buy? (1/2/3/4) "))
                                   time.sleep(1)
                                   print()
                                   if world6ans3 == 1:
                                          if money >= 5000:
                                                 if iphone:
                                                        print_with_delay(Colors.GREEN + "The shop is sold out of this item.")
                                                        time.sleep(3)
                                                        print()
                                                        continue
                                                 else:
                                                        money -= 5000
                                                        print_with_delay(Colors.WHITE + f"You bought the iPhone 96 for $5,000. You now have ${money}.")
                                                        time.sleep(3)
                                                        print()
                                                        iphone = True
                                          else:
                                                 print_with_delay(Colors.GREEN + f"You don't have enough money to buy this item. You only have ${money}.")
                                                 time.sleep(3)
                                                 continue
                                   elif world6ans3 == 2:
                                          if money >= 500000:
                                                 if vr:
                                                        print_with_delay(Colors.GREEN + "The shop is sold out of this item.")
                                                        time.sleep(3)
                                                        print()
                                                        continue
                                                 else:
                                                        money -= 500000
                                                        print_with_delay(Colors.WHITE + f"You bought the VR Contact Lenses for $500,000. You now have ${money}.")
                                                        time.sleep(3)
                                                        print()
                                                        vr = True
                                          else:
                                                 print_with_delay(Colors.GREEN + f"You don't have enough money to buy this item. You only have ${money}.")
                                                 time.sleep(3)
                                                 continue
                                   elif world6ans3 == 3:
                                          if money >= 500000000:
                                                 if robot:
                                                        print_with_delay(Colors.GREEN + "The shop is sold out of this item.")
                                                        time.sleep(3)
                                                        print()
                                                        continue
                                                 else:
                                                        money -= 500000000
                                                        print_with_delay(Colors.WHITE + f"You bought the Robot Companion for $50,000,000. You now have ${money}.")
                                                        time.sleep(3)
                                                        print()
                                                        robot = True
                                          else:
                                                 print_with_delay(Colors.GREEN + f"You don't have enough money to buy this item. You only have ${money}.")
                                                 time.sleep(3)
                                                 continue
                                   elif world6ans3 == 4:
                                          print_with_delay(Colors.GREEN + "You leave the shop.")
                                          time.sleep(3)
                                          break
                                   else:
                                          print_with_delay(Colors.GREEN + "Invalid option.")
                                          time.sleep(3)
                                          continue
                            continue

if start:
       present = True
       if cheat:
              money = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
              strength = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
              robot = "charged"
       elif skip:
              ans1 = input(Colors.MAGENTA + "Accept or decline the toaster's offer? (accept/decline) ")
              time.sleep(1)
              print()
       else:
              print_with_delay(Colors.GREEN + "You live in a run down apartment in the suburbs.")
              time.sleep(5)
              print()
              print_with_delay(Colors.WHITE + f"You have {health} health, {strength} strength, and {money} dollars.")
              time.sleep(5)
              print()
              print_with_delay(Colors.GREEN + "One day while wandering through a thrift store, you see something shining in the kitchen isle.")
              time.sleep(5)
              print_with_delay("You go over and discover that it's a shiny golden toaster.")
              time.sleep(5)
              #print()
              #print_with_delay(Colors.BLUE + "This looks like the perfect white elephant gift.")
              #time.sleep(5)
              #print()
              #print_with_delay(Colors.GREEN + "Later when you get home, you decide to plug in the toaster to try to toast a slice of bread.")
              #time.sleep(5)
              #print_with_delay("When you plug in the toaster and insert a piece of bread, you notice that the dials for the toaster aren't normal.")
              #time.sleep(5)
              #print_with_delay("Instead of bread toasting settings, the knob says 'past' present' and 'future'.")
              #time.sleep(5)
              print_with_delay("You decide to buy it, since your other toaster is broken.")
              time.sleep(5)
              print_with_delay("After you get home, you hear a strange voice talking to you in your head.")
              time.sleep(5)
              print()
              print_with_delay(Colors.RED + "Hey kid, want to earn some sweet dough?")
              time.sleep(5)
              print()
              print_with_delay(Colors.BLUE + "I-I'm not sure, who are you and why are you talking to me?")
              time.sleep(5)
              print()
              print_with_delay(Colors.RED + "Come on kid, you know it's me, your toaster talking to you. And also I'm not a toaster, I'm a time travel machine. \nI can take you anywhere in time and you could become rich!")
              time.sleep(5)
              print()
              ans1 = input(Colors.MAGENTA + "Accept or decline the toaster's offer? (accept/decline) ")
              time.sleep(1)
              print()
       if cheat:
              world = int(input("What world? "))
              time.sleep(1)
       else:
              if ans1 == "decline":
                     print_with_delay(Colors.BLUE + "I must be going crazy, there's no such thing as a talking toaster, or time travel for that matter!")
                     time.sleep(3)
                     print()
                     print_with_delay(Colors.RED + "If you don't believe me, then I guess I'll have to show you.")
                     time.sleep(3)
                     print()
                     print_with_delay(Colors.CYAN + "Zroom!")
                     time.sleep(3)
                     cards_intro()
                     print()
                     world = random.randint(1,6)
                     if cheat:
                            world = int(input("What world? (1-6) "))
              else:
                     print_with_delay(Colors.BLUE + "Sounds fun, I need money.")
                     time.sleep(3)
                     print()
                     print_with_delay(Colors.RED + "Great, would you like to go to the past or the future?")
                     time.sleep(3)
                     print()
                     time1 = input(Colors.MAGENTA + "Go to the past or the future? (past/future) ")
                     time.sleep(1)
                     print()
                     print_with_delay(Colors.CYAN + "Zroom!")
                     time.sleep(3)
                     cards_intro()
                     print()
                     if time1 == "past":
                            world = random.randint(1,4)
                     else:
                            world = random.randint(5,6)
       high_score()
       if cheat:
              die = input("die? (y/n) ")
              if die == "y":
                     health = random.randint(1,1000)
                     strength = random.randint(1,1000)
                     money = random.randint(1,1000)
                     high_score()
                     health = random.randint(1, 1000)
                     strength = random.randint(1, 1000)
                     money = random.randint(1, 1000)
                     the_end()
       if world == 1:
              world1()
       elif world == 2:
              world2()
       elif world == 3:
              world3("False")
       elif world == 4:
              world4()
       elif world == 5:
              world5()
       elif world == 6:
              world6()
       while present:
              rand_bill = random.randint(1,5)
              amount_bill = random.randint(10,100)
              rand_sus_lotto = random.randint(2, 5)
              rand_coin = random.randint(2,5)
              high_score()
              print_with_delay(Colors.GREEN + "You're back in your apartment. The toaster is sitting on your kitchen counter.")
              time.sleep(3)
              print_with_delay(f"You have ${money}.")
              time.sleep(3)
              if save_food > 0:
                     print()
                     eat_food = input(Colors.MAGENTA + f"Eat {food_type} from your pocket? (yes/no) ")
                     time.sleep(1)
                     print()
                     if eat_food == "yes":
                            save_food -= 1
                            rand_food = random.randint(5,30)
                            print_with_delay(Colors.GREEN + f"You eat {food_type} from your pocket.")
                            time.sleep(3)
                            if food_type == "some tater tots":
                                   rand_food *= 10
                                   health += rand_food
                            else:
                                   health += rand_food
                            print_with_delay(Colors.WHITE + f"You gain {rand_food} health. Your health is now {health}.")
                            time.sleep(3)
                            sick = True
              if robot:
                     print_with_delay("The companion robot didn't come with batteries.")
                     time.sleep(3)
                     print_with_delay("Luckily, you can go out and buy a pack of batteries for the robot.")
                     time.sleep(3)
                     print()
                     buy_batteries = input(Colors.MAGENTA + "Buy batteries for $5? (yes/no) ")
                     time.sleep(1)
                     print()
                     if buy_batteries == "yes":
                            money -= 5
                            print_with_delay(Colors.GREEN + "You buy a pack of batteries for $5. You now have ${money}.")
                            time.sleep(3)
                            print_with_delay("You insert the batteries into the back of the robot.")
                            time.sleep(3)
                            print_with_delay("Nothing happens.")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.BLUE + "Dang it! These batteries must not be compatible with this future robot.")
                            time.sleep(3)
                            print()
                            print_with_delay(Colors.GREEN + "You tuck the robot away for later.")
                            time.sleep(3)
                            robot = "charged"
                     else:
                            print_with_delay(Colors.GREEN + "You decide to wait to buy batteries.")
                            time.sleep(3)
              if health < 50:
                     print()
                     health += health/2
                     print_with_delay(Colors.WHITE + f"You gain {health/2} health. You now have {health} health.")
                     time.sleep(3)
              if known_bitcoin > 0:
                     buy_bitcoin = buy_bitcoin * 96000
                     print()
                     if known_bitcoin > rand_coin:
                            rand_coin = random.randint(1,3)
                            if rand_coin == 1:
                                   money -= buy_bitcoin/10
                                   print_with_delay(Colors.GREEN + f"Over the last 15 years, someone hacked into your crypto account and stole all your Bitcoin and an extra ${buy_bitcoin/10}. You now have ${money}.")
                                   time.sleep(3)
                            elif rand_coin == 2:
                                   rand_coin = random.randint(1,10)
                                   print_with_delay(Colors.GREEN + f"Somehow, meddling with time caused the stock market to crash! You lost ${rand_coin*buy_bitcoin}. You now have ${money}.")
                                   time.sleep(3)
                            else:
                                   money += buy_bitcoin
                                   print_with_delay(Colors.WHITE + f"Your Bitcoin has matured and you earn {buy_bitcoin}. You now have ${money}.")
                                   time.sleep(3)
                            known_bitcoin = 1
                     else:
                            money += buy_bitcoin
                            print_with_delay(Colors.WHITE + f"Your Bitcoin has matured and you earn {buy_bitcoin}. You now have ${money}.")
                            time.sleep(3)
                            known_bitcoin = 0
              if sick:
                     rand_sick = random.randint(1,3)
                     if rand_sick == 1:
                            print()
                            print_with_delay(Colors.BLUE + "Ugh, I feel sick. I think it was something I ate.")
                            time.sleep(3)
                            print()
                            if health <= food:
                                   food = health-1
                                   health -= food
                            print_with_delay(Colors.WHITE + f"You lose {food*2} health for being sick, your health is now {health}.")
                            time.sleep(3)
              if rand_bill == 1:
                     print()
                     print_with_delay(Colors.GREEN + f"You have ${amount_bill} in miscellaneous bills to pay.")
                     time.sleep(3)
                     print()
                     pay_bill = input(Colors.MAGENTA + "Pay the bills? (yes/no) ")
                     time.sleep(1)
                     print()
                     if pay_bill == "no":
                            print_with_delay(Colors.GREEN + "You get sent to jail for not paying your bills.")
                            time.sleep(3)
                            print_with_delay(Colors.WHITE + f"You lose ${amount_bill/2}.")
                            money -= amount_bill/2
                            if money < 0:
                                   time.sleep(3)
                                   print_with_delay(f"You are now ${money+money*2} in debt!")
                                   time.sleep(7)
                            else:
                                   time.sleep(7)
                            prison("present")
                            continue
                     else:
                            money -= amount_bill
                            print_with_delay(Colors.GREEN + f"You pay ${amount_bill} to cover the bills. You now have ${money}.")
                            time.sleep(3)
                            if money < 0:
                                   print_with_delay(f"You are now ${money+money*2} in debt!")
                                   time.sleep(3)
              if known_lotto:
                     print()
                     get_lotto = input(Colors.MAGENTA + "Go play the lottery? (yes/no) ")
                     time.sleep(1)
                     print()
                     if get_lotto == "yes":
                            print_with_delay(Colors.GREEN + "You walk over to a nearby gas station to buy a ticket.")
                            time.sleep(3)
                            money -= 5
                            print_with_delay(f"You spend $5 on a ticket, you now have ${money}.")
                            time.sleep(3)
                            print()
                            guess_lotto = int(input(Colors.MAGENTA + "What lottery number do you want? (5-digits) "))
                            time.sleep(1)
                            print()
                            if lottery == guess_lotto:
                                   rand_lotto = random.randint(100,10000)
                                   money += rand_lotto
                                   print_with_delay(Colors.WHITE + f"You won the lottery and gained ${rand_lotto}! You now have ${money}.")
                                   sus_lotto += 1
                                   time.sleep(3)
                                   if sus_lotto >= rand_sus_lotto:
                                          print()
                                          print_with_delay(Colors.GREEN + "You've won the lottery so many times, some people become suspicious you're cheating, and you get thrown in jail.")
                                          time.sleep(7)
                                          prison("present")
                                          print()
                                          continue
                            else:
                                   print_with_delay(Colors.GREEN + "You didn't guess correctly. :(")
                                   time.sleep(3)
                     else:
                            print_with_delay(Colors.GREEN + "You decide to save the lottery for another day.")
                            time.sleep(3)
              known_lotto = False
              print()
              cash = input(Colors.MAGENTA + "Cash out in some of your items or move on to your next adventure? (cash/adventure) ")
              time.sleep(1)
              buy = 0
              if cash == "cash":
                     if gold > 0:
                            print()
                            cash = input(Colors.MAGENTA + f"Cash in {gold} gold, worth ${gold*2}? (yes/no) ")
                            time.sleep(1)
                            print()
                            if cash == "yes":
                                   print_with_delay(Colors.WHITE + f"You gain ${gold*2}.")
                                   money += gold*2
                                   time.sleep(3)
                                   gold = 0
                                   print()
                     else:
                            buy += 1
                     if clay_statue >= 1:
                            cash = input(Colors.MAGENTA + "Sell the clay statue? (yes/no) ")
                            time.sleep(1)
                            print()
                            if cash == "yes":
                                   money += 300
                                   print_with_delay(Colors.WHITE + "You gain $300.")
                                   time.sleep(3)
                                   clay_statue -= 1
                                   print()
                     else:
                            buy +=1
                     if iphone:
                            cash = input(Colors.MAGENTA + "Sell the iPhone 96? (yes/no) ")
                            time.sleep(1)
                            print()
                            if cash == "yes":
                                   money += 10000
                                   print_with_delay(Colors.WHITE + "You gain $10,000.")
                                   time.sleep(3)
                                   iphone = False
                                   print()
                     else:
                            buy +=1
                     if vr:
                            cash = input(Colors.MAGENTA + "Sell the VR Contact Lenses? (yes/no) ")
                            time.sleep(1)
                            print()
                            if cash == "yes":
                                   money +=  1000000
                                   print_with_delay(Colors.WHITE + "You gain $1,000,000.")
                                   time.sleep(3)
                                   vr = False
                                   print()
                     else:
                            buy +=1
                     if club:
                            cash = input(Colors.MAGENTA + "Sell club? (yes/no) ")
                            time.sleep(1)
                            print()
                            if cash == "yes":
                                   money += 10
                                   print_with_delay(Colors.WHITE + "You gain $10.")
                                   time.sleep(3)
                                   strength = strength - 10
                                   print_with_delay("You lose 10 strength.")
                                   time.sleep(3)
                                   club = False
                                   print()
                     else:
                            buy += 1
                     if necklace:
                            cash = input(Colors.MAGENTA + f"Sell antique {jewelry}? (yes/no) ")
                            time.sleep(1)
                            print()
                            if cash == "yes":
                                   money += 200
                                   print_with_delay(Colors.WHITE + "You gain $200.")
                                   time.sleep(3)
                                   necklace = False
                                   print()
                     else:
                            buy += 1
                     if anvil:
                            cash = input(Colors.MAGENTA + f"Sell ancient egyptian anvil? (yes/no) ")
                            time.sleep(1)
                            print()
                            if cash == "yes":
                                   money += 20
                                   print_with_delay(Colors.WHITE + "You gain $20 and lose 20 strength.")
                                   time.sleep(3)
                                   strength -= 20
                                   anvil = False
                                   print()
                     else:
                            buy +=1
                     if buy == 7:
                            print_with_delay(Colors.GREEN + "Nothing to sell.")
                            time.sleep(3)
                     else:
                            print_with_delay(Colors.GREEN + f"Your total money is ${money}.")
                            time.sleep(3)
              print()
              high_score()
              print_with_delay(Colors.RED + "Alrighty kid, if your done dawdling, it's time for your next adventure. Turn my knob and go to the past or the future, there's not a minute to spare!")
              time.sleep(3)
              print()
              world = int(input(Colors.MAGENTA + f"1. {known_world1}\n2. {known_world2}\n3. {known_world3}\n4. {known_world4}\n5. {known_world5}\n6. {known_world6}\nWhere do you want to go? (1/2/3/4/5/6) "))
              time.sleep(1)
              if world != 1 and world != 2 and world != 3 and world != 4 and world != 5 and world != 6:
                     world = random.randint(1, 6)
              print()
              print_with_delay(Colors.CYAN + "Zroom!")
              time.sleep(3)
              cards_intro()
              print()
              if world == 1:
                     world1()
                     continue
              if world == 2:
                     world2()
                     continue
              if world == 3:
                     if clay_statue:
                            idol = True
                     else:
                            idol = False
                     world3(idol)
                     continue
              if world == 4:
                     world4()
                     continue
              if world == 5:
                     world5()
                     continue
              if world == 6:
                     world6()
                     continue