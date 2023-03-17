# THIS IS THE SHIPMATE CLASS: WHEN THE USER DECIDES WHICH CREW MEMBER THEY WANT TO TAKE, WE CREATE AN OBJECT OF THAT PERSON
import time
from colorama import Fore, Style
class Shipmate:
    def __init__(self, shipmate_name, shipmate_age, shipmate_sex):
        self.name = shipmate_name
        self.age = shipmate_age
        self.sex = shipmate_sex # SEX IS TRUE FOR FEMALE, FALSE FOR MALE

    # IF THE USER CHOSE THE PIRATE, THERE WILL BE SPECIAL CONSEQUENCES DEPENDING ON WHETHER THEY CHOSE TO SPLIT OR KEEP THE TREASURE
    def lady_consequence(self, answer):
        if answer == "A":
            print("")
            print("""
You've decided to keep the treasure for yourself, which seems like the right choice since you catch your so called shipmate trying to sneak up on you,
you manage to move passed her and run to your ship, setting sail without her and leaving her stranded, its what she deserves for trying to double cross you,
even though you where going to double cross her..... a pirates life sure is complicated!""")
            print()
            time.sleep(4)
            print("You return to the Tavern and buy a round for everyone, and tell your tale on how you made your fortune!")
            print()
            print(Fore.GREEN+""" 
            
                                ████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
                                ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
                                ░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
                                ░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
                                ░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
                                ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
            
            """+Style.RESET_ALL)
            quit()
        else: # SINCE WE ALREADY DID ERROR HANDLING IN OUR MAIN CODE, WE DON'T NEED TO SPECIFY THAT THIS IS OPTION B
            print("")
            print("You decide to split the treasure with the lady, but she knocks you out and takes the treasure for herself, leaving you stranded on the island")
            print("")
            print("You really should choose who you trust better, they're pirates after all")
            print()
            print(Fore.GREEN+"""
            
                                ████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
                                ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
                                ░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
                                ░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
                                ░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
                                ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
                                           
            """+Style.RESET_ALL)
            quit()
    
    # IF THE USER CHOSE THE SAILOR, THERE WILL BE SPECIAL CONSEQUENCES DEPENDING ON WHETHER THEY CHOSE TO SPLIT OR KEEP THE TREASURE
    def oldman_consequence(self, answer):
        if answer == "A":
            print()
            print("""
You decide to keep the treasure for yourself, whats that old man gonna do anyway.
You sneak upon your ship and go to set sail with the treasure alone, but the old man was waiting, and he doesn't seem pleased.
            
Your plan to keep the treasure to yourself has backfired, the old man being displeased with you trying to steal the treasure has tied you up and left you stranded,
now he sails with all the treasure while you have to sit and think about what you've done.""")
            print()
            print(Fore.GREEN+"""
                                            
                                ████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
                                ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
                                ░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
                                ░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
                                ░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
                                ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
                                            
            """+Style.RESET_ALL)
            quit()
        else: # SINCE WE ALREADY DID ERROR HANDLING IN OUR MAIN CODE, WE DON'T NEED TO SPECIFY THAT THIS IS OPTION B
            print("")
            print("""
You decide to be honest and share your treasure with the old man.
Both your eyes sparkle and glitter from the reflection of the gold and gems, with delight you both load up the ship and sail back to Windrun.
               
You sit now with your new partner in crime in the tavern, sharing stories and drinking ale, your pirate dream has come true. """)
            print()
            print(Fore.GREEN+"""
            
                                ████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
                                ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
                                ░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
                                ░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
                                ░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
                                ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
            
            """+Style.RESET_ALL)
            quit()      