from FiniteAutomata import *

def parseTransitions(parts):
    result = []
    transitions = []
    index = 0

    while index < len(parts):
        transitions.append(parts[index] + ',' + parts[index + 1])
        index += 2

    for transition in transitions:
        lhs, rhs = transition.split('->')
        state2 = rhs.strip()
        state1, route = [value.strip() for value in lhs.strip()[1:-1].split(',')]

        result.append(((state1, route), state2))

    return result

def parseLine(line):
    return [value.strip() for value in line.split('=')[1].strip()[1:-1].strip().split(',')]

def readFromFile(fileName):
    with open(fileName) as file:
        Q = parseLine(file.readline())
        E = parseLine(file.readline())
        print(''.join([line for line in file]))
        #S = parseTransitions(FA.parseLine(''.join([line for line in file])))
        q0 = file.readline().split('=')[1].strip()
        F = parseLine(file.readline())

        return FA(Q, E, S, q0, F)

if __name__ == "__main__":
    FA = readFromFile("fa.in")
    print(FA.toString())
