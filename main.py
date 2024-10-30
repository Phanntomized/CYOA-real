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
       text_delay = .1
       print_with_delay('''
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                      
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                      
       ''')
else:
       intro()
if start:
       clay_statue = False

       time.sleep(2)
       print_with_delay(Colors.GREEN + "You live in a run down apartment in one of the worst parts of town.")
       time.sleep(2)
       print_with_delay("You need money.")
       time.sleep(2)
       print_with_delay("One day while wandering through a junk shop in search of cheap furniture, you see something shining between two pieces of junk.")
       time.sleep(2)
       print_with_delay("You pull it out and you discover that it's' a golden toaster.")
       time.sleep(2)
       print_with_delay("It looks a little strange though, because instead of toasting settings on the knob, all it says is 'Past', 'Present', and 'Future'.")
       time.sleep(2)
       print_with_delay(Colors.BLUE + "Interesting, I think I'll buy this as a gag gift.")
       time.sleep(2)
       print_with_delay(Colors.GREEN + "Later when you get home, you decide to plug in the toaster to try to toast a slice of bread.")
       time.sleep(2)
       print_with_delay("When you plug in the toaster and insert a pice fo bread, you hear a strange voice start talking to you inside of you head.")
       time.sleep(2)
       print_with_delay(Colors.RED + "Hey kid, want to earn some sweet dough?")
       time.sleep(2)
       print_with_delay(Colors.BLUE + "I-I'm not sure, who are you and why are you talking to me?")
       time.sleep(2)
       print_with_delay(Colors.RED + "Come on kid, you know it's me, your toaster talking to you. And also I'm not a toaster, I'm a time travel machine. I can take you anywhere in time and you could become rich!")
       time.sleep(2)
       ans1 = input(Colors.MAGENTA + "Accept or decline the toaster's offer? (yes/no) ")
       time.sleep(2)

       if ans1 == "Decline":
              print_with_delay(Colors.BLUE + "I don't believe you.")
              time.sleep(2)
              print_with_delay(Colors.RED + "Well then let me show you...")
              time.sleep(2)
              print_with_delay(Colors.YELLOW + "Zroom!")
              time.sleep(2)
              world = random.randint(1,6)
            
       if world == 1:
              print_with_delay(Colors.GREEN + "You find yourself in a cave with some fresh cave paintings.")
              time.sleep(2)
              print_with_delay(Colors.BLUE + "Uh oh. That toaster must have been telling the truth.")
              time.sleep(2)
              print_with_delay(Colors.GREEN + "Speaking of the toaster, it's nowhere to be seen.")
              time.sleep(2)
              print_with_delay(Colors.BLUE + "I should probably look for that toaster, so it can take me back.")
              time.sleep(2)
              world1ans1 = (Colors.MAGENTA + "Explore inside or explore outside? (inside/outside) ")
              time.sleep(2)

       if world1ans1 == "inside":
              print_with_delay(Colors.GREEN + "You decide to explore the cave.")
              time.sleep(2)
              print_with_delay(Colors.WHITE + "You find a small, clay statue.")
              clay_statue = True
              time.sleep(2)
              print_with_delay("As you investigate the caves you realize you must be somewhere in the stone age.")
              time.sleep(2)
       elif world1ans1 == "outside":
              print_with_delay(Colors.GREEN + "You decide to explore outside the cave.")
              time.sleep(2)
              print_with_delay("It's hard to tell what time period you got warped into, because there's no sign of civilization apart from the cave.")
              time.sleep(2)
       
       print_with_delay("You notice two people that kind of look like neanderthals coming towards you.")
       time.sleep(2)
       print_with_delay("They are wearing crude sheepskins.")
       time.sleep(2)
       if world1ans1 == "outside":
             print_with_delay("You realize that they are neanderthals and you must be somewhere in the stone age.")
             time.sleep(2)
       print_with_delay("The as they get closer, you notice they don't look happy that your in their territory.")
       time.sleep(2)
       world1ans2 = input(Colors.MAGENTA + "Run away or face the neanderthals? (run/stay) ")
       time.sleep(2)
       
       if world1ans2 == "run":
             print_with_delay(Colors.GREEN + "You decide to run away.")
             time.sleep(2)
             print_with_delay("Uh oh. The neanderthals decided to chase after you, and they have clubs!")
             time.sleep(2)
             print_with_delay("You run until you get to a waterfall.")
             time.sleep(2)
             print_with_delay("The neanderthals are still chasing you.")
             time.sleep(2)
             world1ans3 = input(Colors.MAGENTA + "Jump down the waterfall or face he neanderthals? (jump/stay)")
             time.sleep(2)
       if world1ans2 or world1ans3 == "stay":
             print_with_delay(Colors.GREEN + "You decide to stay and face the neanderthals.")
             time.sleep(2)
             print_with_delay("They approach you and make it clear they want you to give them something.")
             time.sleep(2)
             if clay_statue:
                   print_with_delay("You remember you still have the clay statue you took from the cave.")
                   time.sleep(2)
                   print_with_delay(Colors.BLUE + "If I give them the statue, it may appease them...")
                   time.sleep(2)
                   print_with_delay("...But if I ever do get back to my time, I could probably sell it for a lot of money.")
                   time.sleep(2)
                   world1ans4 = input(Colors.MAGENTA + "Give the statue or keep it? (give/keep) ")
                   time.sleep(2)
                   if world1ans4 == "give":
                         print_with_delay(Colors.GREEN + "You decide to give the neanderthals the clay statue.")
                         time.sleep(2)
                         print_with_delay("...One of them takes the statue and lokks at it, then the one holding the statue walks away.")
                         time.sleep(2)
                         print_with_delay("The other one doesn't walk away but makes it clear that they want a statue as well.")
                         time.sleep(2)
                         print_with_delay("Now that there's only one, you might be able to take them in a fight.")
                         time.sleep(2)
                         world1ans5 = input(Colors.MAGENTA + "Fight the neanderthal or shrug apologetically? (fight/shrug) ")
                         time.sleep(2)
                         if world1ans5 == "fight":
                               print_with_delay(Colors.GREEN + "You decide to try to fight the neanderthal.")
                               time.sleep(2)
                               neanderthal_health = 100
                               print_with_delay("You throw a punch at the neanderthal.")
                               time.sleep(2)
                               swing = random.randint(1,3)
                               if swing == 2:
                                   print_with_delay("The blow dazes the neanderthal, but only for a second.")
                                   neanderthal_health -= 10
                               elif swing == 3:
                                   print_with_delay("The blow catches the neanderthal off guard and knocks them down...")
                                   neanderthal_health -= 20
                               time.sleep(2)
                               print_with_delay("Now its the neanderthal's turn to take a swing at you.")
                               time.sleep(2)
                               print_with_delay("You must predict where the neanderthal is going to swing so you can dodge it.")
                               time.sleep(2)
                               swing = random.randint(1,2)
                               world1ans6 = input("Will the neanderthal swing left or right? (left/right) ")