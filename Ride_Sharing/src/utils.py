import math


def my_round(val, n):
    part = val * 10 ** n
    delta = part - int(part)
    # always round "away from 0"
    if delta >= 0.5 or -0.5 < delta <= 0:
        part = math.ceil(part)
    else:
        part = math.floor(part)
    return part / (10 ** n) if n >= 0 else part * 10 ** abs(n)