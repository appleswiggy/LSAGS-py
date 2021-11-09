import useful_methods
import math
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
    r = useful_methods.generateRandomInteger(groupParameters.subgroupSize)

    c = [-1] * len(publicKeys)
    b = 0
    b1 = 0
    for i in range(len(publicKeys)):
        if i != identity:
            c[i] = useful_methods.generateRandomInteger(groupParameters.subgroupSize)
            b = (b + c[i]) % groupParameters.subgroupSize
            b1 += c[i]

    x = publicKeys.copy()
    x[identity] = groupParameters.generator
    c[identity] = r

    a = useful_methods.power(x, c, groupParameters.prime)

    L = useful_methods.concatPublicKeys(publicKeys)
    h = useful_methods.hash2(L, groupParameters.prime)
    y0 = pow(h, privateKey, groupParameters.prime)

    prefix = L + str(y0) + message
    suffix = str(a) + str(useful_methods.power([h, y0], [r, b], groupParameters.prime))
    h1 = useful_methods.hash1(prefix + suffix, groupParameters.subgroupSize)

    c[identity] = (h1 - b) % groupParameters.subgroupSize
    s = r - c[identity] * privateKey

    return LinkableSignature(y0, s, c)


def verifySignature(message, sig, publicKeys):
    b = 0
    b1 = 0
    for i in range(len(publicKeys)):
        b = (b + sig.C[i]) % groupParameters.subgroupSize
        b1 += sig.C[i]

    L = useful_methods.concatPublicKeys(publicKeys)
    h = useful_methods.hash2(L, groupParameters.prime)
    y0 = sig.Y0

    a = pow(groupParameters.generator, sig.S, groupParameters.prime)
    a = (
        a * useful_methods.power(publicKeys, sig.C, groupParameters.prime)
    ) % groupParameters.prime

    prefix = L + str(y0) + message
    suffix = str(a) + str(
        useful_methods.power([h, y0], [sig.S, b], groupParameters.prime)
    )
    h1 = useful_methods.hash1(prefix + suffix, groupParameters.subgroupSize)

    return b == h1


def test():
    g = groupParameters.generator
    p = groupParameters.prime
    privateKeys = [
        755502699064178066303604234204392021073346147087,
        519432354035141830177690877642097162593516130216,
        290475175773941749519530234778479608230513273407,
    ]
    publicKeys = [
        6501161587842935598173203223206798434410066855562629717014724716669861063485993246885025707709502534785567484676450632216034757391215406232246434475275603,
        3391414727079913550676768974026123772125481856462652607319441728044289478444704568994491683548690113308374975074717855951439265339661433762794520207397001,
        3771092845943974129452137126949984703838881841183871798128175149141161844544046738091938692556454103778625175440309073434685123515608556375817367316642745,
    ]

    sig = generateSignature("hello", publicKeys, privateKeys[1], 1)

    # print("Y0 is: ", sig.Y0)
    # print()
    # print("S is: ", sig.S)
    # print()
    # print("C is: ", sig.C)

    print(verifySignature("hello", sig, publicKeys))
    # print(groupParameters.subgroupSize)


# test()
