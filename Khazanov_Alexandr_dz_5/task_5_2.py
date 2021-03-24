"""*Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""


def odd_nums(n):
    if n % 2 == 0:
        generator = [i for i in range(n) if i % 2 != 0]
    else:
        generator = [i for i in range(n+2) if i % 2 != 0]
    return generator


for gen in odd_nums(14):
    print(gen)
