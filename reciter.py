from pi_memorize.compute_pi import ComputePi

class Reciter:
    def __init__(self):
        self.computer = ComputePi()
        self.current_calculated = 0
        self.pi = ''
        self.pos = 0
        self.compute_pi(100)

    def reset(self):
        self.pos = 0

    def check_next_digit(self, digit):
        if digit == self.pi[self.pos]:
            self.pos += 1
            if self.pos == self.current_calculated:
                self.compute_pi(self.current_calculated + 100)
            return True

        return False

    def compute_pi(self, count):
        self.pi = self.computer.BBP(count)[2:]
        self.current_calculated = count
