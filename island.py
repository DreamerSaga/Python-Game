from colorama import Fore, Style
from puzzle import Puzzle
import time
# THIS IS THE ISLAND CLASS. WHEN THE USER SUCCESSFULY SAILS TO THE ISLAND, THEY WILL HAVE THREE OPTIONS OF WHERE TO GO.
class Island:
    def __init__(self, lives, choice, key):
        self.choice = choice # WHAT OPTION THEY CHOSE
        self.health = lives # HOW MANY LIVES THEY HAVE LEFT
        self.key = key # WHETHER THEY OBTAINED THE KEY FROM SOLVING THE RIDDLE

    # THIS IS CHOICE 1: ENTERING A DARK CAVE
    def island_choice1(self):
        print()
        print("""
        You set off towards the dark cave....
        If treasure is hidden, surely its here, who wouldn't think of entering a dark and spooky cave?!""")
        print()
        time.sleep(3)
        print("""
        As you walk around the cave, you can't see a thing, it seems to dangerous, you turn around to leave,
        but you realise that you can no longer see the entrance and you start to panic, losing your footing you fall into a deep pit,
        with no way out and no one able to hear you from this far down, it seems that your journey ends. """)
        print()
        print(Fore.RED+"""
        
                        ████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
                        ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
                        ░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
                        ░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
                        ░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
                        ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
                                    
        """+Style.RESET_ALL)
        quit()

    # THIS IS CHOICE 2: THE WINNING CHOICE
    def island_choice2(self):
        print()
        print("You set off for the Temple.")
        print()
        time.sleep(2)
        print("You enjoy a surprsingly joyful hike.")
        print()
        time.sleep(1)
        print("Finally at the temple, you look around to see if there's any treasure.")
        print()
        time.sleep(2)
        print("You find a weird alter that has some weird puzzle on it and a keyhole on the side.")
        print()
        if self.key: # IF KEY IS TRUE, AKA THEY HAVE IT, THEY DON'T NEED TO SOLVE THE PUZZLE
            print("You take out the key that the Mysterious figure from the tavern gave you and put it in the keyhole and turn.")
            print()
            time.sleep(3)
            print("The alter opens up and inside is a mountain of gold and gems! YOU HAVE FOUND THE TREASURE!")
        else:
            print("With no key to use, you have to solve the puzzle, you only have three attemps, luckily there's a difficulty slider, you can't help but thank whoever made this.")
            print()
            time.sleep(2)
            print("Which difficulty do you choose?:")

            # THEY HAVE THREE OPTIONS TO CHOOSE FROM: EASY, MEDIUM AND HARD
            choices = [
                Fore.LIGHTGREEN_EX+"A: Easy"+Style.RESET_ALL,
                Fore.LIGHTYELLOW_EX+"B: Medium"+Style.RESET_ALL,
                Fore.LIGHTRED_EX+"C: Hard"+Style.RESET_ALL
            ]
            for i in choices:
                print(i)
            
            selection = input("Please select your choice: ").lower()

            error_checking = True
            while error_checking:
                if selection == "a" or selection == "b" or selection == "c":
                    error_checking = False
                    puzzle = Puzzle(selection) # AFTER ALL THE ERROR HANDLING HAS BEEN DONE, WE USE THE
                                               # PUZZLE CLASS TO DISPLAY AND CHECK THE RIDDLE
                    puzzle.play()
                else:
                    print("Not a valid option!")
                    selection = input("Please select your choice: ").lower()        

    # THIS IS CHOICE 3: THE JUNGLE
    def island_choice3(self):
        print()
        print("You set off to the jungle, everyone knows thats where treasure is hidden!")
        print()
        time.sleep(2)
        print("You wonder through the jungle with no luck finding any treasure, this seems like a waste of time.")
        print("You decide to head to the temple since its closer than the cave...")
        print()
        time.sleep(4)
        print("OH NO, on your way out of the jungle, you heard a hiss and by the time you noticed, it was too late, a snake lashed out and bit you!")
        print()
        print(Fore.MAGENTA+""" 
                                ⠀⠀ ⠀⣀⣀⣄⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡖⣻⠉⢿⣿⠆⠈⠙⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡚⠒⠊⠙⠂⠀⠀⢆⣱⡘⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡟⠛⠳⣖⠒⠒⢙⡤⣿⣷⠃⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢻⠆⠤⠤⡗⣿⢻⣼⢀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠸⣼⣏⡒⢲⠟⡟⣾⡾⣎⢾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⢸⡴⢻⠃⠀⡜⢸⣻⠴⠛⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣰⣰⣷⠏⠀⢰⠃⣿⣷⢳⣰⣤⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠹⣯⣿⣟⠢⢤⣇⣸⣿⡽⣧⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⣭⠓⠌⠉⡛⠉⣿⣼⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⣰⠁⣼⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠐⠁⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⣼⠏⢰⢦⡀⠀⠀⠀⠀⠀⣀⡠⠤⠤⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⡀⠀⠀⣸⡟⠀⠈⢯⡓⠦⢤⡤⠴⠚⠁⠀⠀⠀⠀⠀⢘⠍⠳⡄⠀⠀⠀⠀
                    ⠀⠀⢀⣠⠤⠖⠒⡒⠒⠢⢤⡗⢤⡉⢺⠒⣿⡃⣀⣀⣠⠽⠷⠒⠛⠉⠉⣉⣉⣛⣛⣛⣛⡉⠀⠀⣸⠀⠀⠀⠀
                    ⢀⡴⠋⠀⠀⢠⠊⠀⠀⠀⢸⡇⢄⡈⠛⣏⣿⠉⠁⠀⢀⣠⠤⠖⠚⠉⠉⠀⠀⠀⠓⠦⣄⠉⠙⠚⠯⣄⡀⠀⠀
                    ⡜⠀⠀⠀⠀⢸⣤⡶⠦⢤⣼⣇⠀⠈⢉⣧⢿⣧⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠉⢦⠀
                    ⣇⠀⠀⠀⠀⠈⠳⣄⣀⣀⣈⣿⠑⠢⠤⠼⡞⣿⡄⠀⠀⠀⠀⠀⢀⣀⣠⡤⠴⠶⠶⠒⠒⢿⡇⠀⠀⠀⠀⠸⡆
                    ⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠈⠐⠂⠙⣖⠻⣤⣠⣤⡶⠞⠋⠉⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⢸⠇
                    ⠀⠈⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠈⠢⠀⠉⠓⠦⠤⢤⣀⣠⠤⠤⠤⠒⠚⠉⠀⠀⠀⠀⠀⣠⡟⠁
                    ⠀⠀⠀⠀⠈⠙⠓⠲⠶⠶⠶⠶⠞⠛⠓⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⠴⠞⠋⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
        
        """+ Style.RESET_ALL)
        print()
        print("OUCH!")
        print()
        time.sleep(1)
        print("You have lost a LIFE!")
        self.health -= 1
        if self.health == 0:
            print("Your journey ends, you lost all your lives, honestly for a novice pirate you made it far, try again!")
            print(f"""{Fore.RED}
                  
                    ████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
                    ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
                    ░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
                    ░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
                    ░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
                    ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
                                    
                  {Style.RESET_ALL}""")
            quit()
        print(f"You now have {self.health} health!")
        self.island_choice2()

    # THIS SENDS THE USER TO THE RIGHT PLACE DEPENDING ON THEIR CHOICE
    def enter_island(self):
        if self.choice == "A":
            self.island_choice1()
        elif self.choice == "B":
            self.island_choice2()
        else:
            self.island_choice3()
