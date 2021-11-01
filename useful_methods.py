def HexToInt(hexa):
    hexa = hexa.replace(" ", "").replace("\n", "")
    integer = int(hexa, 16)
    return integer
