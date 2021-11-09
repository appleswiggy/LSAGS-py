import random
import math
import hmac
import hashlib


def HexToInt(hexa):
    hexa = hexa.replace(" ", "").replace("\n", "")
    integer = int(hexa, 16)
    return integer


def generateRandomInteger(max):
    n = len(str(max)) + 8
    # random_number = random.randint(10 ** n, 10 ** (n + 1) - 1)
    random_number = random.randint(1, 10 ** (n + 1) - 1)
    return random_number % max


def power(a, b, prime):
    product = 1
    for i, j in zip(a, b):
        # product mod prime ??
        product = (product * pow(i, j, prime)) % prime
    return product


def concatPublicKeys(publicKeys):
    st = ""
    for i in publicKeys:
        st += str(i)
    return st


def hash1(message, subgroupSize):
    keys = ["01", "02", "03", "04", "05"]
    st = ""
    for i in keys:
        digest = hmac.new(i.encode(), message.encode(), hashlib.sha512).hexdigest()
        st += str(HexToInt(digest))
    return int(st) % subgroupSize


def hash2(message, prime):
    keys = ["11", "12", "13", "14", "15"]
    st = ""
    for i in keys:
        digest = hmac.new(i.encode(), message.encode(), hashlib.sha512).hexdigest()
        st += str(HexToInt(digest))
    return ((int(st) % (prime - 1)) + 1) % prime


def generateKeyPairs(groupParameters, n):
    p = groupParameters.prime
    q = groupParameters.subgroupSize
    g = groupParameters.generator

    publicKeys = []
    privateKeys = []
    for i in range(n):
        temp = generateRandomInteger(q)
        privateKeys.append(temp)
        temp = pow(g, temp, p)
        publicKeys.append(temp)

    return [publicKeys, privateKeys]
