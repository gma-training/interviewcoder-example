class MedianFinder:

    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)

    def get(self):
        numbers = sorted(self.numbers)
        middle = len(numbers) // 2
        try:
            if len(numbers) > 0 and len(numbers) % 2 == 0:
                upper_middle = middle
                lower_middle = upper_middle - 1
                return (numbers[lower_middle] + numbers[upper_middle]) / 2
            else:
                return numbers[middle]
        except IndexError:
            raise RuntimeError('No values added')
