if __name__ == '__main__':
    def calc(*numbers):
        sum = 0
        for n in numbers:
            sum = sum +n * n
        return sum
print(calc(1,2,3))
