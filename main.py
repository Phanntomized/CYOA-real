import time


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
       
       time.sleep(1)
       #print("center".center(20,"-"))
       x = input(Colors.BLUE + "                                Press x to start: " + Colors.RESET)
       if x == "x":
              start = True
       else:
              intro()
       if start:
              print("it works")
       else:
              print("it doesnt work :C")
intro()