class LinkableSignature:
    def __init__(self, Y0, S, C) -> None:
        self.Y0 = Y0
        self.S = S
        self.C = C

    def isLinked(self, S1) -> bool:
        return S1.Y0 == self.Y0
