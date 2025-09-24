import math
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
print(calculate_circle_area(5))

students = [
    {"id": 1,"name": "Alice", "major": "Computer Science"},
    {"id": 2,"name": "Bob", "major": "Mathematics"},
    {"id": 3,"name": "Charlie", "major": "Physics"},
]

#寫一個涵式，接受一個數字列表，回傳列表中的最大值
def find_maximum(numbers):
    """Return the maximum value from a list of numbers.

    numbers: 必須為非空的數字列表，否則會丟出 ValueError 或 TypeError。
    """
    if not numbers:
        raise ValueError("The list cannot be empty")
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
print(find_maximum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

# 寫一個程式，從1列印到100
# 如果數字是3的倍數，印出"Fizz"
# 如果數字是5的倍數，印出 "Buzz"
# 如果數字是3和5倍數，印出 "FizzBuzz"
# 其他情況則印出數字本身
def fizz_buzz(n):
    """Return 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, and 'FizzBuzz' for multiples of both."""
    result = ''
    if n % 3 == 0:
        result += 'Fizz'
    if n % 5 == 0:
        result += 'Buzz'
    return result or str(n)
