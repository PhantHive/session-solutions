"""
Exercise: Multiplication Table
Goal: Create a multiplication table for a given number n
where each element is a string in the form "n x i = result" going from i = 10 to i = 1.
"""


def multiplication_table(n):
    return [f"{n} x {i} = {n * i}" for i in range(10, 0, -1)]


print(multiplication_table(2))
