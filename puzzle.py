from colorama import Fore, Style

# THIS IS THE PUZZLE CLASS: HERE THE RIDDLES ARE STORED, AS WELL AS THEIR ANSWERS
class Puzzle:
    def __init__(self, difficulty):
        self.difficulty = difficulty # THIS IS THE DIFFICULTY THE USER CHOSE: EASY, MEDIUM, HARD
        self.tries = 3 # THEY ONLY HAVE THREE TRIES TO SOLVE IT CORRECTLY

    # HERE WHENEVER A TRY HAS BEEN USED UP WE REDUCE AND KEEP TRACK OF IT
    def set_tries(self):
        self.tries -= 1
        if self.tries != 0:
            print(f"You have {self.tries} tries left.")

    # IN THIS METHOD WE DISPLAY TO THE USER THE QUESTION THEY PICKED, AND WE CHECK FOR THE ANSWER
    def ask_question(self, question, options, correct_answer):
        print(question)
        for option in options:
            print(option)

        answer = input("Choose your answer: ").upper()

        invalid_answer = True
        while invalid_answer:
            if answer == correct_answer:
                invalid_answer = False
                print()
                print("\033[1m Correct!\033[0m")
            else:
                print()
                print("\033[1m Incorrect!\033[0m")
                self.set_tries()
                if self.tries == 0: # WHEN THERE ARE NO MORE ATTEMPTS LEFT, END THE GAME
                    print("No tries left.")
                    print()
                    print()
                    print("As the last attempt failed, the temple rumbles and crumbles to rubble on top of you!!")
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
                answer = input("Choose your answer: ").upper()

    # THIS METHOD SENDS THE USER TO THE CORRECT CODE DEPENDING ON WHICH CHOICE THEY PICKED
    def play(self):
        if self.difficulty == "a":
            self.ask_question(Fore.LIGHTGREEN_EX+"\033[1m Question\033[0m: A pirate has 6 gold coins, and he finds 4 more. How many gold coins does he have now?"+Style.RESET_ALL,
                              ["A: 4", "B: 6", "C: 10"], "C")
        elif self.difficulty == "b":
            self.ask_question(Fore.LIGHTYELLOW_EX+"\033[1m Question\033[0m: A group of pirates have 12 bottles of rum, and they want to share them equally among themselves.\nHow many bottles of rum will each pirate get if there are 4 pirates in the group?"+Style.RESET_ALL,
                              ["A: 2", "B: 3", "C: 4"], "B")
        elif self.difficulty == "c":
            self.ask_question(Fore.LIGHTRED_EX+"\033[1m Question\033[0m: A group of 8 pirates have found a treasure chest with 100 gold coins. They want to divide the treasure among themselves, but they need to come up with a fair way to split the coins.\nThe captain proposes a plan where each pirate gets a certain number of coins, and the captain gets twice as many coins as the next highest-ranked pirate.\nHow many gold coins will the captain get under this plan?"+Style.RESET_ALL,
                              ["A: 20", "B: 30", "C: 40"], "B")
        else:
            print("Invalid difficulty level.")