class Password:
    def __init__(self, lower, higher, char, passphrase):
        self.lower = lower
        self.higher = higher
        self.char = char
        self.passphrase = passphrase

    def is_correct_task1(self):
        return self.higher >= self.passphrase.count(self.char) >= self.lower

    def is_correct_task2(self):
        return self.passphrase[self.lower - 1] == self.char != self.passphrase[self.higher - 1] or self.passphrase[
            self.lower - 1] != self.char == self.passphrase[self.higher - 1]
