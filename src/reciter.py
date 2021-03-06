from pi_memorize.compute_pi import ComputePi


class Reciter:
    """Calculates pi and validates inputted digits."""

    def __init__(self):
        """Setups all variables and starts computing pi."""
        self.computer = ComputePi()
        self.current_calculated = 0
        self.pi = ''
        self.pos = 0
        self.errors = 0
        self.compute_pi(150)

    def reset(self):
        """Sets the number of correct digit and of the errors back to zero."""
        self.pos = 0
        self.errors = 0

    def check_next_digit(self, digit):
        """Checks, if the next inputted digit is correct."""
        if digit == self.pi[self.pos]:
            self.pos += 1
            if self.pos == self.current_calculated:
                self.compute_pi(self.current_calculated + 150)
            return True
        else:
            self.errors += 1
            return False

    def compute_pi(self, precision):
        """Computes the digits of pi."""
        self.pi = self.computer.machin_euler(precision)[2:]
        self.current_calculated = precision
