import time
import random


def print_pause(sentence):
    print(sentence)
    time.sleep(2)


def tutorial():
    print_pause("Once upon a time...")
    print_pause("The ogre came in a village.")
    print_pause("It's too much to handle him because he are very strong.")
    print_pause("You heard the rumor those thing,"
                " so you decided to fight him to save people.")


def firstStage(party):
    response = input("Which way do you want to go?\n1.The mountain"
                     "that wolves lived in.\n2.The village\n")
    if response == "1":
        print_pause("You arrived at the mountain that wolves lived in.")
        print_pause("You met the person such as wolf."
                    " He called himself 'dog'.")
        print_pause("He joined your party.")
        party.append("dog")
        secondStage(party)
    elif response == "2":
        print_pause("You challenge the ogre to fight.")
        print_pause("However, his power was beyond your imagination.")
        print_pause("You lost...")
        playagain()
    else:
        print("Please answer '1' or '2'")
        firstStage(party)
# fix invalid option like above fubctiob


def guessingGame(party):
    quiz = ['apple', 'orange']
    answer = random.choice(quiz)
    print(answer)
    response2 = input("Which food does he like? 'apple' or 'orange'\n")
    if response2.lower() == 'apple' or response2.lower() == 'orange':
        if response2.lower() == answer:
            print_pause("He said it\'s correct to you.")
            print_pause("He joined your party.")
            party.append("phesant")
        else:
            print_pause("He said to you, 'No'.")
            print_pause("He said he cannot be on your side to you.")
    else:
        print("Please answer 'apple' or 'orange'")
        guessingGame(party)


def secondStage(party):
    response = (input("Which way do you want to go?\n1.The kingdom"
                      " of bird\n2.The ghetto\n3.The village\n"))
    if response == "1":
        if "phesant" in party:
            print_pause("You arrived at the kingdom of bird,"
                        "but you don't need to do here anymore.")
            secondStage(party)
        else:
            print_pause("You arrived at the kingdom of bird.")
            print_pause("You met the warrior, his name is phesant.")
            print_pause("He told you to guess the food that he likes.")
            guessingGame(party)
            secondStage(party)
    elif response == "2":
        if "monkey" in party:
            print_pause("You arrived at the ghetto,"
                        " but you don't need to do here anymore.")
            secondStage(party)
        else:
            print_pause("You arrived at the ghetto,"
                        " but the gate is blocked by a heap of rubble.")
            if "phesant" in party:
                print_pause("The ghetto blew the heap of rubble away.")
                print_pause("You met the guy, his name is monkey.")
                print_pause("He joined your party..")
                party.append("monkey")
                secondStage(party)
            else:
                print_pause("It seems like that you can\'t go over there. ")
                secondStage(party)
    elif response == "3":
        if "phesant" in party and "monkey" in party:
            print_pause("You challenge the ogre to fight.")
            print_pause("The dog and phesant and monkey work together well!")
            print_pause("You won the ogre!")
            print_pause("Congratulations!!!!!")
            playagain()
        else:
            print_pause("You challenge the ogre to fight.")
            print_pause("However, his power was beyond "
                        "your imagination.")
            print_pause("You lost...")
            playagain()
    else:
        print("Please answer '1' or '2' or '3'.")
        secondStage(party)


def playagain():
    response3 = input("Would you like to play again? (y/n)\n")
    if response3.lower() in "y":
        print_pause("Excellent! Restarting the game...")
        playinggame()
    elif response3.lower() in "n":
        print_pause("Thanks for playing!")
    else:
        print("Please answer 'yes' or 'no'.")
        playagain()


def playinggame():
    party = []
    tutorial()
    firstStage(party)


playinggame()
