import itertools


class ISBN:
    def __init__(self, isbn):
        self.clean = isbn.replace('-', '')
        self.parsed = self.parse()

    def parse(self):
        return [int(digit) for digit in self.clean]

    def validate(self):
        if len(self.parsed) == 10:
            return self._validate10()

        if len(self.parsed) == 13:
            return self._validate13()

    def _validate10(self):
        check = sum([
            digit * weight
            for digit, weight in enumerate(self.parsed)
        ])

        return check % 11 == 0

    def _validate13(self):
        check = sum([
            digit * weight
            for digit, weight in zip(self.parsed, itertools.cycle((1, 3,)))
        ])

        return check % 10 == 0
