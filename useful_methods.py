import random


def HexToInt(hexa):
    hexa = hexa.replace(" ", "").replace("\n", "")
    integer = int(hexa, 16)
    return integer


def generateRandomInteger(max):
    n = len(str(max)) + 8
    random_number = random.randint(10 ** n, 10 ** (n + 1) - 1)
    return random_number % max


def power(a, b):
    product = 1
    for i, j in zip(a, b):
        product *= a ** b
    return product
