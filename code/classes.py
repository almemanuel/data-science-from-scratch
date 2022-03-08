class CountingClicker:
    def __init__(self, count = 0):
        self.count = count


    def __repr__(self):
        return f'{self.count}'


    def click(self, num_times = 1):
        self.count += num_times


    def read(self):
        return self.count


    def reset(self):
        self.count = 0


class NoResetClicker(CountingClicker):
    def reset(self):
        pass


clicker = CountingClicker()

assert clicker.read() == 0, 'clicker should start with count 0'
clicker.click()

clicker.click()

assert clicker.read() == 2, 'after two clicks, clicker should have count 2'
clicker.reset()

assert clicker.read() == 0, 'after reset, clicker should be back 0'

