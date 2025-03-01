class MedianFinder:

    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)

    def _is_even(self, num):
        return num % 2 == 0

    def _mean_of_pair(self, numbers, i, j):
        return (numbers[i] + numbers[j]) / 2

    def get(self):
        if len(self.numbers) == 0:
            raise RuntimeError('No values added')
        self.numbers.sort()
        middle = len(self.numbers) // 2
        if self._is_even(len(self.numbers)):
            return self._mean_of_pair(self.numbers, middle - 1, middle)
        return self.numbers[middle]
