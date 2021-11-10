from FiniteAutomata import *

def determineTransitions(parts, Q, E):
    result = []
    transitions = []
    index = 0

    while index < len(parts):
        transitions.append(parts[index])
        index += 1

    for transition in transitions:
        lhs, rhs = transition.split('->')
        state2 = rhs.strip()

        if state2 not in Q:
            raise Exception(state2 + " is not in the set of states!")

        state1, route = [value.strip() for value in lhs.strip()[1:-1].split(',')]

        if state1 not in Q:
            raise Exception(state1 + " is not in the set of states!")
        if route == "epsilon":
            raise Exception("Transition of " + state1 + " and epsilon is not allowed!")
        if route not in E:
            raise Exception(route + " is not defined in the alphabet!")

        result.append(((state1, route), state2))

    return result

def transformLine(line):
    return [value.strip() for value in line.split('=')[1].strip()[1:-1].strip().split(';')]

def readFromFileAndVerify(fileName):
    with open(fileName) as file:
        Q = transformLine(file.readline())
        E = transformLine(file.readline())

        for element in Q:
            if element in E:
                raise Exception("The set of states cannot have elements of the alphabet!")

        try:
            S = determineTransitions(transformLine(file.readline()), Q, E)
        except Exception as e:
            print(e)
            exit()
        # S = parseTransitions(prseLine(''.join([line for line in file])))
        q0 = file.readline().split('=')[1].strip()

        if len(q0) != 1:
            raise Exception("There are more the one initial state!")
        if q0 not in Q:
            raise Exception("The initial state is not in the set of states!")

        F = transformLine(file.readline())

        for state in F:
            if state not in Q:
                raise Exception("State " + state + " is not in the set of states!")



        return FA(Q, E, S, q0, F)

def printMenu():
    print("Menu:")
    print("1. the set of states")
    print("2. the alphabet")
    print("3. all the transitions")
    print("4. the set of final states")

if __name__ == "__main__":
    try:
        FA = readFromFileAndVerify('fa.in')
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
