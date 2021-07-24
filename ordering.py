
def order(numbers):
    n = len(numbers)
    for x in range(n - 1):
       for y in range(0, n-x-1):
           if numbers[y] > numbers[y + 1]:
               numbers[y], numbers[y + 1] = numbers[y + 1], numbers[y]
    return numbers


