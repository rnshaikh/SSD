import math
import conf


def my_round(val, n):
    part = val * 10 ** n
    delta = part - int(part)
    # always round "away from 0"
    if delta >= 0.5 or -0.5 < delta <= 0:
        part = math.ceil(part)
    else:
        part = math.floor(part)
    return part / (10 ** n) if n >= 0 else part * 10 ** abs(n)


def calculate_ecd(start_x_co, start_y_co, end_x_co, end_y_co):
    
    ans = (end_x_co - start_x_co) ** conf.TWO + (end_y_co - start_y_co) ** conf.TWO
    ans = math.sqrt(ans)
    ans = my_round(ans, conf.TWO)
    ans = (ans*conf.PERC_DIVISOR)/conf.PERC_DIVISOR
    return ans