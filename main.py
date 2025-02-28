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
        numbers = sorted(self.numbers)
        middle = len(numbers) // 2
        if len(numbers) == 0:
            raise RuntimeError('No values added')
        if self._is_even(len(numbers)):
            return self._mean_of_pair(numbers, middle - 1, middle)
        return numbers[middle]
