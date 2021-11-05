#E - epsilon
#S - sigma

class FA:
    def __init__(self, Q, E, S, q0, F):
        self.Q = Q
        self.E = E
        self.S = S
        self.q0 = q0
        self.F = F

    def parseLine(self):
        pass

    def getQ(self):
        return self.Q

    def toString(self):
        return "Q: " + str(self.Q) + "\n" + "E: " + str(self.E) + "\n" + "S: " + self.S + "\n" + "q0: " + self.q0 + "\n" + "F: " + str(self.F)


