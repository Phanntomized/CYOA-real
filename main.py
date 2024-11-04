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

def world1():
       fall = False
       health = 100
       strength = 100
       clay_statue = False 
       gold = 0
       club = False  
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
                                          print_with_delay(Colors.WHITE + f"The neadnerthal's health is now {neanderthal_health}.")
                                          time.sleep(3)
                                   elif swing == 2:
                                          print_with_delay(Colors.GREEN + "The blow knocks the neanderthal over.")
                                          neanderthal_health = neanderthal_health - 20
                                          neanderthal_health = neanderthal_health - strength
                                          time.sleep(3)
                                          print_with_delay(Colors.WHITE + f"The neadnerthal's health is now {neanderthal_health}.")
                                          time.sleep(3)
                                          continue
                                   else:
                                          print_with_delay(Colors.GREEN + "The neanderthal evades your blow.")
                                          time.sleep(3)
                                   if neanderthal_health <= 0:
                                          print_with_delay("The neanderthal staggers backwards, and falls over.")
                                          time.sleep(3)
                                          print_with_delay("It appears you have knocked them unconsious.")
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
       print_with_delay(Colors.GREEN + "You hit the water a little hard and lose 5 health.")
       health -= 5
       time.sleep(3)
       print_with_delay("After walking a little ways away from the waterfall, you find the toaster. It still has a piece of toast in it.")
       time.sleep(3)
       print_with_delay(Colors.BLUE + "Why did you bring me here? I can't even make any money because it hasn't been invented yet?")
       time.sleep(3)
       print_with_delay(Colors.RED + "There must have been a mistake somewhere in between the present and now. But don't worry, with just a twist of my knob, you can be whisked away to a different time period.")
       time.sleep(3)
       time1 = input(Colors.MAGENTA + "Go to the present or the future? (present/future) ")
       time.sleep(1)

def world2():
       if world == 2:
              pass

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
       



       money = 10
       health = 100
       strength = 0

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
              world = random.randint(1,6)
       else:
              print_with_delay(Colors.BLUE + "Sounds fun, I need money.")
              time.sleep(3)
              print_with_delay(Colors.RED + "Great, would you like to go to the past or the future?")
              time.sleep(3)
              time1 = input(Colors.MAGENTA + "Go to the past or the future? (past/future) ")
              time.sleep(1)
              print_with_delay(Colors.YELLOW + "Zroom!")
              time.sleep(3)
              if time1 == "past":
                     world = random.randint(2,4)
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

       if time1 == "present":
              print_with_delay(Colors.GREEN + "You find yourself back in your apartment. The toaster is plugged in next to you.")
              time.sleep(3)
              while cash != "adventure":
                     cash = input(Colors.MAGENTA + "Cash out in some of your items or move on to your next adventure? (cash/adventure) ")
                     if cash == "cash":
                            if gold > 0:
                                   cash = input(Colors.MAGENTA + "Cash in gold? (yes/no) ")
                                   time.sleep(1)
                                   if cash == "yes":
                                          gold = gold * 2
                                          print_with_delay(Colors.WHITE + f"You gain {gold} dollars.")
                                          money = money + gold
                                          gold = 0
                            try:
                                   if clay_statue:
                                          cash = input(Colors.MAGENTA + "Sell the clay statue? (yes/no) ")
                                          time.sleep(1)
                                          if cash == "yes":
                                                 money = money + 50
                                                 print_with_delay(Colors.WHITE + "You gain 50 dollars.")
                                                 clay_statue = False
                            except:
                                   pass
                            try:       
                                   if club:
                                          cash = input(Colors.MAGENTA + "Sell club? (yes/no) ")
                                          time.sleep(1)
                                          if cash == "yes":
                                                 money = money + 10
                                                 print_with_delay(Colors.WHITE + "You gain 10 dollars.")
                                                 time.sleep(3)
                                                 strength = strength - 10
                                                 print_with_delay("You lose 10 strength.")
                                                 time.sleep(3)
                            except:
                                   pass
              else:
                     print_with_delay(Colors.RED + "Alrighty kid, if your done selling all that stuff, it's time for your next adventure. Turn my knob and go to the past or the future, there's not a minute to spare!")
                     time.sleep(3)
                     time1 = input("Go to the past or the future? (past/future) ")
              if time1 == "past":
                     world = random.randint(2,4)
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

