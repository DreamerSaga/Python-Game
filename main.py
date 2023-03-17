from colorama import Back, Fore, Style
from island import Island
from shipmate import Shipmate
import time
import os

# ========================================= METHODS ========================================= #

# EVERY INITIAL CHOICE IS MADE INTO A METHOD SO THAT IT COULD BE EASIER TO CALL 
# THE METHOD WHEN NECESSARY IN THE CODE(ALSO MAKES IT NEATER)

health=3 # HEALTH IS MADE GLOBAL HERE SO IT CAN BE USED WHEN HEALTH IS MINUSED
key = False # KEY IS MADE GLOBAL SO THAT WE KNOW WHICH COURSE OF ACTION TO TAKE IF THE USER GOT THE KEY

# THIS IS THE METHOD SECTION WHERE ALL THE METHODS ARE CALLED TO THE CODE DOWN BELOW

# THIS METHOD DISPLAYS THE CHARACTERS THE USER CAN CHOOSE

def npc_selection():

        print("Who do you choose to approach?:")
        selection_options=[
        Fore.RED+"A: The tough pirate covered in scars?"+Style.RESET_ALL,
        Fore.CYAN+"B: The mysterious figure hiding away?"+Style.RESET_ALL,
        Fore.MAGENTA+"C: The Burly Bartender?"+Style.RESET_ALL
        ]
        return selection_options # THIS IS RETURNED SO THAT BELOW IN THE CODE IT COULD BE CALLED 
# NPC SELECTION IS A LIST OF THE NPC'S WHERE THE USER CAN CHOOSE FROM


# THIS METHOD RUNS IF THE USER PICKS THE ROUGH LOOKING GUY
def choice1():
        print()
        print("You decide to approach the tough looking pirate and ask him for rumours of treasure")
        print()
        time.sleep(2)
        print()
        print(f"\033[1m {mc_name}\033[0m: Hello there sir, do you by chance happen to know of any leads for treasure and adventure?")
        print()
        time.sleep(2)
        print()
        print("\033[1m Pirate\033[0m: Who dares be askin a pirate about treasure, yargh, ye be seekin an early end me thinks.")
        print()
        time.sleep(2)
        print(f"""

The tough pirate picks \033[1m {mc_name}\033[0m up and throws them through a table.

OUCH!!

Thats not the best start to an adventure, and it seems \033[1m {mc_name}\033[0m has lost a LIFE, be careful
if you end up with 0, then its game over.

Well, what's done is done, time for \033[1m {mc_name}\033[0m to pick themselves up and try again!
        
        """)

        global health # FROM ABOVE THE HEALTH WAS GLOBALISED THEREFORE 'GLOBAL HEALTH' WAS USED TO LOCALISE THE GLOBAL HEALTH
                      #AND SUBTRACTED IT BY 1 TO GET THE NEW HEALTH
        health-=1 
        if health == 0: # THIS IS A IF STATEMENT THAT IS USED WHENEVER THE HEALTH IS DEDUCTED FROM THE USER'S HEALTH, 
                        # IF THE HEALTH AT ANY POINT EQUALS TO 0 THEN THE GAME WILL END IMMEDIATELY AS THE MC HAS DIED IN THE GAME
                print("Your adventure comes to an early end, you've ran out of lives, perhaps you should have made better choices")
                print()
                print(f"""{Fore.RED}
                          
                            ████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
                            ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
                            ░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
                            ░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
                            ░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
                            ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
                          
                          {Style.RESET_ALL}""")
                quit()
        
        print()
        print(f"Remaining Life: {health}.")
        print()
        print("\nSo, time to try again!")
        new_selection = npc_selection() # A NEW VARIABLE WAS USED, SO THAT CHOICE 1 COULD BE REMOVED FROM THE SELECTION LIST
        new_selection.remove(Fore.RED+"A: The tough pirate covered in scars?"+Style.RESET_ALL) # .REMOVE WAS USED AS THE METHOD 
        for i in new_selection:
                print(i)
        print("") # THIS PRINTS THE NEW SELECTION WITHOUT CHOICE 1 AS THE NEW VARIABLE
                  # CHOICE 1 IS THE FUNCTION TO BE CALLED IF THE USER WISHES TO PICK CHOICE 1 ONE FROM THE SELECTION LIST


# THIS METHOD RUNS IF THE USER PICKS THE BARTENDER
def choice3():
        print()
        print()
        print("You take a seat at the counter and wait for the Bartender to finish serving a patron.")
        time.sleep(2)
        print()
        print("\033[1m Bartender\033[0m: Welcome, what can I get yer?")
        time.sleep(2)
        print()
        print(f"\033[1m {mc_name}\033[0m: Actually, I'm not here to drink, I was hoping you'd have a lead on an adventure!")
        time.sleep(2)
        print()
        print("The Bartender strokes her strangely well defined chin and seems lost in thought.")
        time.sleep(2)
        print()
        print("\033[1m Bartender\033[0m: Normally I'd have you buy something to get information, but I do have a lead on an island that no one has yet to plunder.")
        time.sleep(2)
        print()
        print(f"\033[1m {mc_name}\033[0m: Well look no further, with my thirst for adventure I'll be sure to plunder every corner of this island!")
        print()
        time.sleep(2)
        print("\033[1m Bartender\033[0m: AHA HA HA, yargh got spirit kid, but its your funeral, but what do I care, HA HA HA, here, take this map and recruit a crew, or don't HAHA!")
        print()
        time.sleep(2)
        print("\033[1m Bartender\033[0m: NOW GET OUT!")
        print()
        print()
        print(Fore.GREEN+"You obtained a map from the Bartender."+Style.RESET_ALL) # LINK TO NEXT CODE
      
# THIS IS THE CHOICE THAT NEEDS TO BE LINKED TO THE NEXT PART OF THE GAME


# THIS METHOD RUNS IF THE USER PICKS THE MYSTERIOUD ROBED GUY
def choice2():
        print()
        print("You approach the Mysterious Figure.")
        print()
        time.sleep(1)
        print("\033[1m Mysterious Figure\033[0m: WhO DaRes aPProAcH mEEEEE!")
        print()
        time.sleep(2)
        print("Umm, maybe this wasn't a good idea, you go to turn away....")
        print()
        time.sleep(2)
        print()
        print("\033[1m Mysterious Figure\033[0m: WAIT! I know what ye seek, a lead to adventure and fortunes untold, well it so happens I be having what ya need.")
        time.sleep(2)
        print()
        print(f"\033[1m {mc_name}\033[0m: You're clearly crazy but its not like I've had any luck yet, so why not, tell me, what do you have?")
        time.sleep(2)
        print()
        print("""\033[1m Mysterious Figure\033[0m: Not so fast!, I shall give you the location of an island with a hidden treassure most precious, 
        and I even have a key that will open your way...""")
        print(" And all you have to do is answer... my riddle heh heh heeeeh...")
        time.sleep(2)
        print()
        print(f"\033[1m {mc_name}\033[0m: I'll solve your riddle no problem, so go ahead and ask!")
        print()
        time.sleep(2)
        print("\033[1m Mysterious Figure\033[0m: The KEY is on the line so listen closely!") # THE ROBED FIGURE GIVES A RIDDLE ETC 
        print()
        time.sleep(2)
        print(Fore.GREEN+"""
        This pirate's phrase you should know:
        When you take a two by four
        then place it on a shelf
        Put it in a freezer box
        """+Style.RESET_ALL) # THIS IS THE PIRATE RIDDLE FOR THE USER TO ANSWER
        print("")
        print()
        print("Pick from A, B, or C")
        riddle_answers=[
        Fore.CYAN+"A: Shlver m3 Tlmbers"+Style.RESET_ALL,
        Fore.YELLOW+"B: Timber me Shivers"+Style.RESET_ALL,
        Fore.MAGENTA+"C: Shiver me Timbers"+Style.RESET_ALL
        ]
        for i in riddle_answers:
                print(i) # THE ANSWERS TO THE RIDDLE AND A MULTI-CHOICE
        print("")
        answer_of_riddle=input("What is the Riddles answer? ").upper()
        print("")
        error_checking = True
        while error_checking: # IF ERROR_CHECKING EQUALS TO TRUE AND 'WHILE' IT IS TRUE, WE ARE CARRYING OUT ERROR HANDLING
                
                if answer_of_riddle=="A" or answer_of_riddle=="B": # THESE ARE THE INCORRECT ANSWERS TO THE RIDDLE 
                        print("\033[1m Mysterious Figure\033[0m: REEEEEEEEEEEEEEEEE, WRONG WRONG WRONG, YOU NO GOOD OAF, GO TALK TO THE BARTENDER AND LEAVE ME BE!")
                        print()
                        print("Well.... that was weird, oh well who needs a stupid key anyway, but he was right, I should go talk to the Bartender.")

                        error_checking = False # BECAUSE THE CONDITION HAS BEEN MET, THE WHILE LOOP OF THE CODE WILL NOT INFINITELY RUN 
                        choice3()

                elif answer_of_riddle=="C": # IF THE USER PICKS THE RIDDLE ANSWER OF C THEN THE CORRECT ANSWER WILL BE DISPLAYED
                        print("\033[1m Mysterious Figure\033[0m: YES YES YES!, CORRECT, GOOD JOB, TAKE THIS KEY AND SAIL SOUTH EAST.") # LINK TO NEXT CODE, IF CORRECT THEN LINK TO NEXT CODE OF THE GAME
                        global key
                        key = True
                        print("")
                        error_checking = False # BECAUSE THE CONDITION HAS BEEN MET, THE WHILE LOOP OF THE CODE WILL NOT INFINITELY RUN 
               
                else:
                        print("Please pick from the options A, B or C! ") # THIS IS ONLY TO MAKE SURE THAT IF THE USER PICKS ANYTHING OTHER THAN A,
                                                                        #B OR C IT WILL RE-QUESTION
                        print("")
                        answer_of_riddle=input("What is your answer? ").upper()


os.system('cls')
filenames=["art.txt","art1.txt"]
filenames2=["art2.txt", "art3.txt"]

# THIS METHOD RUNS IF THE USER DECIDES TO TAKE A CREWMATE WITH THEM
crew_mate = Shipmate(None, 0, None)
def trav_crew():
    print()
    print("Going alone seems dangerous, it would be better to recruit a shipmate for the journey...")
    print()
    time.sleep(2)
    print("You set up help wanted posters all over town and wait till morning.")
    print()
    time.sleep(5)
    print("You return to the tavern and see if anyone has responded, and what a luck, there seems to be two applicants, who do you choose?")
    print()
    options=[
        Fore.GREEN+"A: Beautiful young woman, she seems keen for adventure and an eye for treasure"+Style.RESET_ALL, 
        Fore.BLUE+"B: An old scruffy man, perhaps his experience will be useful"+Style.RESET_ALL]
    for i in options:
           print(i)
    time.sleep(2)
    print()
    crew=input("Who will it be? ").upper()

    global crew_mate

    error_checking = True
    while error_checking:
           if crew=="A":
                  error_checking = False
                  crew_mate = Shipmate("Sarah", 22, True) # IF THEY CHOOSE THE BEAUTIFUL GIRL, CREATE HER OBJECT
                  print(Fore.GREEN+f"You have chosen to voyage with {crew_mate.name}. She is {crew_mate.age} years old."+Style.RESET_ALL)
           elif crew=="B":
                  error_checking = False
                  crew_mate = Shipmate("Gin", 52, False) # IF THEY CHOOSE THE OLD MAN, CREATE HIS OBJECT
                  print(Fore.BLUE+f"You have chosen the voyage with {crew_mate.name}. He is {crew_mate.age} years old."+Style.RESET_ALL)
           else:
                  print("Please choose A or B!")
                  crew=input("Who will it be? ").upper()

# ========================================== CODE ============================================= #

print(Fore.CYAN+"""  

        
                ████████╗░█████╗░██████╗░░█████╗░██╗░░░██░   ░██╗   ░█████╗░███╗░░░███╗  
                ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝   ░██║   ██╔══██╗████╗░████║  
                ░░░██║░░░██║░░██║██║░░██║███████║░╚████╔╝    ░██║   ███████║██╔████╔██║  
                ░░░██║░░░██║░░██║██║░░██║██╔══██║░░╚██╔╝░░   ░██║   ██╔══██║██║╚██╔╝██║  
                ░░░██║░░░╚█████╔╝██████╔╝██║░░██║░░░██║░░░   ░██║   ██║░░██║██║░╚═╝░██║  
                ░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░   ░╚═╝   ╚═╝░░╚═╝╚═╝░░░░░╚═╝  

                        ░█████╗░    ██████╗░██╗██████╗░░█████╗░████████╗███████    ██╗
                        ██╔══██╗    ██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝   ██║
                        ███████║    ██████╔╝██║██████╔╝███████║░░░██║░░░█████╗░░   ██║
                        ██╔══██║    ██╔═══╝░██║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░   ╚═╝
                        ██║░░██║    ██║░░░░░██║██║░░██║██║░░██║░░░██║░░░███████╗   ██╗
                        ╚═╝░░╚═╝    ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝   ╚═╝


"""+Style.RESET_ALL)
time.sleep(0.2)
print() 
print()
print("""
Today, you are a pirate, you have a thirst for treasure and adventure, will you be able to reach the goal 
and lay claim to fame and fortune?
Or shall your adventure fall through and wind up at the bottom of the ocean?""")
print()
mc_name = input("Please choose a name for your pirate: ").capitalize()
print()
time.sleep(0.5)
print(f"""

Welcome \033[1m {mc_name}\033[0m, to Windrun Island, a place full of outlaws and pirates but also known for great rumours 
that can lead to boundless treasures untold, but be warned, you only have 3 LIVES to see yourself through your journey,
lose them all? Well its game over.""")
print()
time.sleep(3.5)
print(f"""

As you look around the island you see ruggish men and women, veterans of the sea, this truly is the place to be for a pirate,
stumbling from place to place with no luck, you find yourself in a shadey part of town, you see a tavern named The Golden Whistle,
surely this place will hold the key to starting your first adventure, \033[1m {mc_name}\033[0m, take a deep breath, and go inside.""")
print()
time.sleep(6)
print("""

As you enter the tavern a thick smog of smoke hits your face, coughing a little you bat your hand around to blow the smoke away,
as the smoke clears you make out a lively tavern scene, people drinking and making merry, you notice three distinct people.
The Bartender, a beautiful burly woman who's clearly seen her fair share, surely she hears a lot of rumours?
A mysterious figure, sitting in the back wearing hooded robes, perhaps they are hiding away?
A tough, scar riddled man, a pirate without equal, clearly he has been on many a voyage, perhaps he would be willing to share some information?""")
time.sleep(8)
# THIS IS THE INTRODUCTION TO THE BEGINNING STAGE OF THE GAME
# THIS GIVES YOU THE BRIEF INFORMATION TO START THE GAME

# A="Rough looking guy": you lose 1 health and talk to mysterious figure or bartender
# B="Mysterious robed figure": will give a riddle and if correct then a key if incorrect, talk to bartender
# C="Bartender": gives information

print()


for i in npc_selection():
        print(i) # THIS IS THE SELECTION OF NPC'S FROM THE METHOD ABOVE WHERE THE RETURN STATEMENT WAS USED
print("")

answer=input("Enter A, B or C: ").upper() # INITIALLY ASKING THE USER WHAT CHOICE THEY WOULD LIKE TO PICK
print("")

error_checking = True
while error_checking: # IF ERROR_CHECKING EQUALS TO TRUE AND 'WHILE' IT IS TRUE, ERROR HANDLING WILL OCCUR
        if answer == "A": # IF A THEN CHOICE 1 IS CARRIED OUT
                choice1()
                answer=input("Who do you wish to talk to? ").upper()
                while answer == "A":
                        print("Pick a valid option!")
                        answer=input("Who do you wish to talk to? ").upper()

        elif answer == "B": # IF B THEN CHOICE 2 IS CARRIED OUT
                error_checking = False # BECAUSE THE CONDITION HAS BEEN MET, THE WHILE LOOP OF THE CODE WILL NOT INFINITELY RUN
                choice2()

        elif answer == "C": # IF C THEN CHOICE 3 IS CARRIED OUT
                error_checking = False # BECAUSE THE CONDITION HAS BEEN MET, THE WHILE LOOP OF THE CODE WILL NOT INFINITELY RUN
                choice3()

        else:
                print("Pick a option between A,B or C!")
                answer=input("Who do you wish to talk to? ").upper() # THIS IS TO ENSURE THAT IF THE INITIAL QUESTION IS ANSWERED WITHOUT A,B OR C THEN IT WOULD RE-QUESTION



# NOW THE USER DECIDES WHETHER THEY WANT TO GO ALONE OR TAKE A CREWMATE WITH THEM
print()
time.sleep(2)
print("Now that you have what you need, you must decide if you shall venture alone, or with a crew?! ")
print()
print("Choose how you'll set sail: ")
selection=[
       Fore.CYAN+"A: Alone"+Style.RESET_ALL, 
       Fore.GREEN+"B: With a crew"+Style.RESET_ALL]

for i in selection:
        print (i)
print("")

answer=input("So what will you decide to pick? ").upper()
print("")

sail_choice = True # THIS IS OUR ERROR HANDLING VARIABLE
while sail_choice:
        if answer=="A": # IF THEY CHOOSE A, THEY SAIL ALONE
                sail_choice = False # BECAUSE THEY ENTERED A VALID ANSWER, WE EXIT THE LOOP
                print("You decided to set sail alone, I mean why would you want to share your loot?")
                print()
                time.sleep(5)
                print("You're sailing the seas towards the island that holds treasure and adventure.")
                print()
                time.sleep(2)
                print()
                print("As you journey, the clouds start to darken and the waves batter against your ship, this isn't looking good.")
                time.sleep(4)
                print()
                print("ITS A STORM!")
                print("You quickly hurry back and forth on your ship, trying to adjust the sails and keep the ship steady, but its to much to handle alone.")
                print()
                time.sleep(2)
                print("A MASSIVE WAVE HAS CRASHED INTO YOUR SHIP AND WRECKED IT!")
                print()
                print(Fore.CYAN+"""
                
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣷⣄⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠿⣤⣾⣿⣽⡿⠛⣆⣬⣿⣅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⡟⣟⠁⠀⠀⠀⠉⠁⡀⠀⡚⠉⠀⠈⠹⡶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢀⣀⣤⠶⠶⠒⢛⣉⡭⠞⠁⠈⠙⢷⡤⠴⠶⢤⡴⠞⠋⢻⣧⡤⣦⡀⠀⠀⠈⣇⡈⠛⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⣠⡴⠛⣡⠤⠖⠚⠛⠉⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⡏⠁⠀⠀⠙⢦⡀⠀⠨⣧⠀⠀⣿⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⢀⣤⠴⠛⠁⣠⠞⠁⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⣡⠏⠀⠀⠀⠀⣀⡠⢿⡀⢰⠿⣤⠀⢘⠋⠉⠻⣆⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
               .⠋⠁⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣰⠋⠀⠀⠀⣰⠞⠁⠀⠀⠉⠁⠀⠹⠗⠻⡆⠀⠀⠻⣯⡉⢣⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⢠⣾ :⠀⢠⣾⠀⠀⠀⠀⣰⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠰⡏⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⢀⣀⡀⠀⠈⣽⡄⠀⠀⣼⡿⣾⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠘⢻⣤  ⠀⠘⢻⣤⠀⠀⠀⠹⡆⠀⠠⡄⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⣶⣧⠀⠀⠀⡇⠀⠀⠀⠀⣠⠞⠉⣸⡿⠿⠿⡶⣽⣦⣶⠿⢦⠈⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
              ⠘⢹⡀⠀⠀⠘⢹⡀⠀⠀⠀⠹⣆⠀⠙⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠋⣿⠀⠀⣇⡇⠀⢀⠀⣼⠁⡤⠟⠁⣀⣀⣰⣖⣚⠋⠀⠀⢸⠀⠀⢘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                :⡄⠀⠀⠈⢧⡀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⢳⠀⠀⢸⣇⠀⡿⠇⣿⡾⢁⡴⣋⣉⣀⣉⠃⠉⢢⡀⠀⢸⠀⠀⠀⢿⣤⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠙⢦⣀⣀⠀⠙⠢⣄⠀⠀⠀⠈⠳⢦⡀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠉⢀⡇⡇⣷⢃⣏⡾⠉⠀⠀⠉⠙⢶⣶⣿⣄⣿⡄⠀⠀⠘⢿⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠈⠙⠲⢤⣀⡉⠳⠦⣄⡀⠀⠙⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⡇⡟⣺⡿⠀⠀⠀⠀⠀⠀⠀⠻⢿⠁⠙⣷⡀⠀⠀⠀⣇⠘⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⢢⣶⢄⡀⠀⠀⠀⠀⠉⠓⠦⠤⣉⣓⠦⣄⡀⠙⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠿⣧⡀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣄⢹⣿⡄⠀⠀⣿⠤⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠈⠓⢭⣓⠒⠒⠒⠒⠲⠤⣄⡀⠀⠉⠛⠛⠿⠦⣄⣙⠳⢤⡀⠀⠀⠀⠀⠀⠸⡄⠈⢧⢷⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢯⢏⣿⣶⡄⢹⡇⢈⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠉⠓⠲⢤⣤⣀⣀⠀⠉⠓⠲⠤⠔⠶⢴⣤⣭⣉⠀⠈⠓⠦⣄⠀⠀⠀⢻⡄⠈⣞⣆⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠻⣞⢿⣼⣧⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠘⣶⣤⣀⠀⠀⠀⠀⠉⠙⠦⣤⣤⣀⣤⣤⣤⣀⣀⡀⠉⠳⢦⣀⠀⠀⠀⠀⠀⠙⣄⡈⢯⢪⡻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢾⣽⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⢹⣦⡍⠓⠶⠤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠲⠤⣍⣙⣳⣦⡀⠀⠀⠀⠙⠶⣷⣹⣟⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠘⠿⣇⡀⠀⠀⠀⠀⠉⠛⠛⠒⠒⠦⠤⢤⣤⣀⡀⠀⠀⠀⠀⠈⠙⠀⠀⢤⠀⠀⠀⠀⠀⠻⢧⡉⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠈⠙⠲⠤⣄⡀⠀⠀⠀⣦⣄⣀⣀⡐⠺⠯⣤⣀⣀⣀⣀⣀⡀⠀⠀⠈⠓⢄⡀⠀⠀⠀⠀⠉⠲⢬⡙⠳⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠲⢤⣌⣓⠮⣭⣉⠙⠓⠒⠒⠦⠬⠭⢭⣽⣷⠶⣦⣀⠀⠙⠲⣤⡀⠀⠀⠀⠀⠉⠳⢤⣉⠛⠲⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠷⣄⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠑⠚⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠳⣄⠀⠀⠉⠉⠒⠲⠶⣄⠀⠀⠈⠙⠲⠶⠮⢝⣲⡦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⢹⣦⡍ ⠀⠈⠙⠶⢾⠏⠉⠋⠙⠲⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⡿⢕⡲⠶⢤⣀⠀⠀⠙⣄⠈⠳⢄⡀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠉⠑⠚⠿⠷⠦⣄⣀⡀⠀⠀⠀⠀
             ⢠⣾  ⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣄⡀⠀⠰⠴⣤⡤⠤⠤⠾⠋⠙⠃⢀⣀⣨⠿⠦⠀⠈⠑⢄⡀⠙⠲⢤⣄⡀⠀⠀⠈⠙⠲⠤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠒⠤⢄
                ⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣀⣀⠙⢦⡀⠀⠈⠉⠓⠢⢤⣀⠀⠘⠿⢤⣄⡀⠀⠀⠀⠀⠀⠉⠒⢦⣄⣈⡉⠒⠦⣤⣀⠀⠀⠀⠉⠙⠒⠲⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠁
                ⠀⠀⠉⠓⠚⠓⠦⣄⡀⠀⠀⠀⠉⠑⠺⣭⡑⠛⠂⠀⠀⠀⠀⠀⠈⠙⠲⢦⣀⣈⣙⠓⠦⣄⡀⠀⠀⠀⠀⠀⠉⠉⠙⠒⠒⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠓⠒⠲⠦⠤⣤⣤
                ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢦⡀⠀⠀⠀⠀⠉⠓⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠈⠉⠑⠾⢍⣦⣄⠀⠀⠀⠀⠀⠀⠀⠤⠤⠤⠤⠤⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣚⣇⡀⠀⠀⠀⠀⠀⠈⠙⠲⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣛⣷⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠓⠲⠤⠤⣄⣀⠀⠀⠈⠙⠲⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣇⣉⣡⣛⣁⣹⣛⣉⣿
                
"""+Style.RESET_ALL)

                time.sleep(2)
                print()
                print("You slowly sink to the ocean floor, if you only had a shipmate to help, but your greed caused your downfall!")
                print()
                print(Fore.RED+"""
                
                                ████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
                                ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
                                ░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
                                ░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
                                ░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
                                ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
                
                """+Style.RESET_ALL)
                print("")
                quit()
        elif answer=="B": # IF THEY CHOOSE B, THEY DECIDE WHO THEY WANT TO TAKE
                sail_choice = False # BECAUSE THEY ENTERED A VALID ANSWER, WE EXIT THE LOOP
                trav_crew()

        else:
               print()
               print("Please choose A or B: ")
               answer=input("So who will you decide to pick? ").upper()


# THEIR JOURNEY HAS STARTED, THE FIRST OBSTACLE IS SAILING TO AN ISLAND
print()
time.sleep(4)
print("With your crew choosen, you spend the day planning your adventure, before you know it evening has approached, you decide to sleep for the night before setting off.")
time.sleep(5)
print()
print("\nYou awaken and join your crew aboard your ship, you have your map, you have your shipmate, now you need to decide on a route, shall ye take the Calm seas or the Stormy Seas?")
print("\nHere are your options: ")

sail = [
Fore.GREEN+"A: Calm seas"+Style.RESET_ALL,
Fore.CYAN+"B: Stormy seas"+Style.RESET_ALL
]
for i in sail:
        print(i)

choice = input("\nPick your course: ").upper()

incorrect_sea_condition = True
while incorrect_sea_condition:
        if choice == "A": # IF THEY CHOOSE THE CALM SEA, THEY GET TO THE ISLAND SAFELY
                incorrect_sea_condition = False
                print()
                print("You decide to take the safe route, the calm seas, sure it'll take longer but sure it's safer.")
                print()
                time.sleep(3)
                print("You and your shipmates seem eager to get to the island.")
                time.sleep(3)
                print()
                print("The calming seas treat you well, but there's nothing to be done.")
                print()
                                
                time.sleep(2)
                print("With the journey taking longer than expected, you decide to take a nap, and enjoy the voyage!...")
                print()
                time.sleep(6)
                print()
                print()
                print()
                def animator(filenames, delay=2, repeat=10):
                        frames= []

                        for name in filenames:
                                 with open(name,"r", encoding="utf8") as f:
                                        frames.append(f.readlines())

                        for i in range(repeat):
                                for frame in frames:
                                   print("".join(frame))
                                   time.sleep(delay)
                                   os.system('cls')

                animator(filenames, delay=0.5, repeat=6)
                time.sleep(3)
                print()
                print()
                print("FINALLY, you reach the island safely, but that sure did take a while.")

                print(""" 
                
                                ⠀⠀⠀⠈⠉⠛⢷⣦⡀⠀⣀⣠⣤⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⣀⣻⣿⣿⣿⣋⣀⡀⠀⠀⢀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⣠⠾⠛⠛⢻⣿⣿⣿⠟⠛⠛⠓⠢⠀⠀⠉⢿⣿⣆⣀⣠⣤⣀⣀⠀⠀⠀
                                ⠀⠀⠘⠁⠀⠀⣰⡿⠛⠿⠿⣧⡀⠀⠀⢀⣤⣤⣤⣼⣿⣿⣿⡿⠟⠋⠉⠉⠀⠀
                                ⠀⠀⠀⠀⠀⠠⠋⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠹⣿⣿⣿⠟⠻⢶⣄⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠈⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⣤⣤⣤⣤⣤⣤⡤⠄⠀⠀⣀⡀⢸⡇⢠⣤⣁⣀⠀⠀⠠⢤⣤⣤⣤⣤⣤⣤⠀
                                ⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣷⣤⣤⣾⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀
                                ⠀⠀⠼⠿⣿⣿⠿⠛⠉⠉⠉⠙⠛⠿⣿⣿⠿⠛⠛⠛⠛⠿⢿⣿⣿⠿⠿⠇⠀⠀
                                ⠀⢶⣤⣀⣀⣠⣴⠶⠛⠋⠙⠻⣦⣄⣀⣀⣠⣤⣴⠶⠶⣦⣄⣀⣀⣠⣤⣤⡶⠀
                                ⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀              
                """)
                
        elif choice == "B": # IF THEY CHOOSE THE STORMY SHORTCUT, THEY GET SCURVY AND LOSE A LIFE
                incorrect_sea_condition = False
                print()
                print("You decide to take the dangerous route, the stormy seas, it'll be faster but risky!")
                print()
                time.sleep(10)
                print()
                print()
                def animator2(filenames2, delay=1, repeat=8):
                        frames= []

                        for name in filenames2:
                                 with open(name,"r", encoding="utf8") as f:
                                        frames.append(f.readlines())

                        for i in range(repeat):
                                for frame in frames:
                                   print("".join(frame))
                                   time.sleep(delay)
                                   os.system('cls')

                animator2(filenames2, delay=0.5, repeat=4)
                print()
                print("You and your shipmates focus on keeping the ships steady as the oceans waves batter against it.")
                time.sleep(2)
                print()
                print("You arrive at the island, a little worse for wear, you stumbled during the journey and hit your head, it seems you've lost a LIFE.")
                health -= 1
                if health == 0:
                        print("You ran out of lives")
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
                print(f"You have {health} lives left.")
        else:
                print("Please pick a choice:")
                choice = input("Pick a choice: ").upper()


# ARRIVE AT THE ISLAND. THEY NOW HAVE THREE OPTIONS OF WHERE TO GO NEXT
print()
time.sleep(2)
print(f"Congratulations \033[1m {mc_name}\033[0m, you've made it to the island!")
print("Now that you're here, you realise you have no idea where to go, the map doesn't show exactly where on the island this treasure is.")
print()
time.sleep(2)
print("After surveying around your landing site, you see three possible paths...")
print("Which path do you take? ")


islands = [Fore.GREEN+
    Fore.RED+"A: The Dark Cave"+Style.RESET_ALL,
    Fore.YELLOW+"B: The Temple"+Style.RESET_ALL,
    Fore.GREEN+"C: The Jungle"+Style.RESET_ALL
]
for i in islands:
    print(i)

answer = input("Choose from A, B, or C: ").upper()


incorrect_location_choice = True
while incorrect_location_choice:
    if answer == "A" or answer == "B" or answer == "C":
        incorrect_location_choice = False
        island = Island(health, answer, key) # IF THEY ENTER A VALID ANSWER, CREATE AN ISLAND OBJECT AND ALLOW THEM TO CONTINUE
        island.enter_island()
    else:
        print("Please pick from options A, B, or C!")
        answer = input("Choose from A, B, or C: ").upper()


# THEY HAVE NOW REACHED THE ANCIENT TEMPLE, SOLVED THE RIDDLE (IF APPLICABLE) AND FOUND THE TREASURE
print()
time.sleep(3)
print("Now that you've finally found the treasure, it glitters in yer eyes, but now you feel the greed taking over you, surely you can just take it for yerself?")
print()
print(Fore.YELLOW+""" 
⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠿⠿⠿⢿⣿⣷⣶⣶⣶⣦⣤⣤⣤⣤⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣶⣦⠀⣶⣤⣤⣤⣤⣍⣉⣉⣉⡙⠛⠛⠛⠛⠏⣰⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⡿⢠⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣆⠸⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⢸⣿⣿⣿⣿⣿⣿⣿⡏⠀⠹⠟⠙⣿⣿⣿⠄⢻⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠊⣉⡉⢋⣩⡉⠻⠛⠁⣾⣀⣴⡀⢛⡉⢠⣷⠈⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⣿⣿⣿⣿⣷⣿⠀⢿⣿⣿⣿⡿⢁⠚⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠤⠾⠿⣿⡿⠛⣿⣿⣿⣿⣿⣷⣦⣌⣉⣉⣠⣾⡷⠂⣠⠀⠀⠀⠀
⠀⠀⠀⣿⢰⣶⣶⣶⣦⠀⠀⣤⣌⣉⠉⣉⡙⠛⠛⠛⠻⠟⢁⣴⣾⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣆⠻⣿⣿⢇⣸⠀⣯⢉⣿⠀⣿⣿⣿⣿⣿⣷⠀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣷⡔⠐⣾⣿⠀⠛⠚⠿⠀⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⠿⠋⠀⠀⠀⠀
⠀⠀⠰⣦⡄⠀⠀⠈⠉⠉⠉⠉⠛⠛⠛⠛⠻⠿⠿⠿⠿⠀⠛⢁⣀⡀⠲⠖⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀                          
"""+Style.RESET_ALL)

time.sleep(2)
print("So young pirate, make yer choice, keep it fer yerself or share with yer shipmate?")

ending=[Fore.MAGENTA+
       Fore.CYAN+"A. Keep it fer yerself"+Style.RESET_ALL,
       Fore.GREEN+"B. Share the treasure"+Style.RESET_ALL]
for i in ending:
       print(i)
answer = input("type A or B to make yer choice: ").upper()


invalid_decision = True
while invalid_decision:
    if answer != "A" and answer != "B":
        print("Please type a valid choice!")
        answer = input("type A or B to make yer choice: ").upper()
    else:
        invalid_decision = False       
        if crew_mate.sex: # IF THEY CHOSE THE FEMALE PIRATE AT THE START OF THE GAME, WE ASSIGN THE APPROPRIATE CONSEQUENCE
            crew_mate.lady_consequence(answer)
        else: # IF THEY CHOSE THE MAKE SAILOR, WE ASSIGN THE APPROPRIATE CONSEQUENCE
            crew_mate.oldman_consequence(answer)