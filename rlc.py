import math

class RLC:
    def __init__(self, R, L, C, frequency):
        if R < 0 or L <= 0 or C <= 0 or frequency <= 0:
            raise ValueError("Invalid input values")

        self.R = R
        self.L = L
        self.C = C
        self.f = frequency

    def reactance_L(self):
        return 2 * math.pi * self.f * self.L

    def reactance_C(self):
        return 1 / (2 * math.pi * self.f * self.C)

    def impedance(self):
        XL = self.reactance_L()
        XC = self.reactance_C()
        return math.sqrt(self.R**2 + (XL - XC)**2)

    def phase_angle(self):
        XL = self.reactance_L()
        XC = self.reactance_C()
        return math.atan((XL - XC) / self.R)

    def resonant_frequency(self):
        return 1 / (2 * math.pi * math.sqrt(self.L * self.C))
