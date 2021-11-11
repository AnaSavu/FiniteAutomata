from FiniteAutomata import *

def printMenu():
    print("Menu:")
    print("1. the set of states")
    print("2. the alphabet")
    print("3. all the transitions")
    print("4. the set of final states")

if __name__ == "__main__":
    try:
        FA = FA('fa.in')
        print("It is a valid FA!")
    except Exception as e:
        FA = None
        print(e)

    if FA is None:
        exit()

    try:
        FA.isDFA()
        print("It is DFA!")
    except Exception as e:
        print(e)

    print('sequence: ', end="")
    sequence = input()

    try:
        FA.isSequenceAcceptedByFA(sequence)
        print("Sequence is accepted by the FA!")
    except Exception as e:
        print(e)

    while(True):
        print()
        printMenu()
        print('>>> ', end="")
        try:
            command = int(input())
            print()
            if command == 1:
                print(FA.getQ())
            elif command == 2:
                print(FA.getE())
            elif command == 3:
                print(FA.getS())
            elif command == 4:
                print(FA.getF())
            else:
                print("Wrong command! Try again")
        except ValueError as e:
            print(e)

    # print(FA.toString())
