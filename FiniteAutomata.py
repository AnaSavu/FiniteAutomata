#E - epsilon
#S - sigma
import itertools


class FA:
    def __init__(self, Q, E, S, q0, F):
        self.Q = Q
        self.E = E
        self.S = S
        self.q0 = q0
        self.F = F

    # return the set of states
    def getQ(self):
        return self.Q

    # return the alphabet
    def getE(self):
        return self.E

    # return all the transitions
    def getS(self):
        return self.S

    # return the set of final states
    def getF(self):
        return self.F

    def isDFA(self):
        for a, b in itertools.combinations(self.S, 2):
            if a[0] == b[0]:
                raise Exception("It is not DFA!")
            # print(a[0], end="")
            # print(b[0])
            # compare(a[0], b[0])

    def isSequenceAcceptedByFA(self, sequence):
        currentState = self.q0

        for i in range(len(sequence)):
            posi = sequence[i]
            ok = 0
            for transition in self.S:
                if transition[0][1] == posi and transition[0][0] == currentState:
                    currentState = transition[1]
                    ok = 1
                    break
            if ok == 0:
                raise Exception("Sequence is not accepted by the FA!")

    def toString(self):
        return "Q: " + str(self.Q) + "\n" + "E: " + str(self.E) + "\n" + "S: " + str(self.S) + "\n" + "q0: " + str(self.q0) + "\n" + "F: " + str(self.F)


