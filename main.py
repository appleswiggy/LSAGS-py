import useful_methods
from parameters import KnownParameters

groupParameters = KnownParameters.RFC5114_2_3_256


class LinkableSignature:
    def __init__(self, Y0, S, C) -> None:
        self.Y0 = Y0
        self.S = S
        self.C = C

    def isLinked(self, S1) -> bool:
        return S1.Y0 == self.Y0


def generateSignature(message, publicKeys, privateKey, identity):
    # this way of generating random int might be wrong
    r = useful_methods.generateRandomInteger(groupParameters.subgroupSize)
    c = [-1] * len(publicKeys)
    b = 0

    for i in range(len(publicKeys)):
        if i != identity:
            # this way of generating random int might be wrong
            c[i] = useful_methods.generateRandomInteger(groupParameters.subgroupSize)
            b = (b + c[i]) % groupParameters.subgroupSize

    x = publicKeys.copy()
    x[identity] = groupParameters.generator
    c[identity] = r

    a = useful_methods.power(x, c)  # this is wrong. Fix it later when you figure out
