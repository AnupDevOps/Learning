# Data Hiding.py


class JustCounter:
    secretCount = 0
    def count(self):
        self.secretCount += 1
        print(self.secretCount)


counter = JustCounter()
counter.count()
counter.count()

print(counter.secretCount)


class JustCounter:
    __secretCount = 0
    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()

print(counter.__secretCount)
