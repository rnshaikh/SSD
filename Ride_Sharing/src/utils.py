import math
import conf


def my_round(val, n):
    part = val * conf.TENTH ** n
    delta = part - int(part)
    # always round "away from 0"
    if delta >= conf.HALF_PART or conf.NEGATIVE_HALF_PART < delta <= conf.ZERO_INIT:
        part = math.ceil(part)
    else:
        part = math.floor(part)
    return part / (conf.TENTH ** n) if n >= conf.ZERO_INIT else part * conf.TENTH ** abs(n)


def calculate_ecd(start_x_co, start_y_co, end_x_co, end_y_co):
    
    ans = (end_x_co - start_x_co) ** conf.TWO + (end_y_co - start_y_co) ** conf.TWO
    ans = math.sqrt(ans)
    ans = my_round(ans, conf.TWO)
    ans = (ans*conf.PERC_DIVISOR)/conf.PERC_DIVISOR
    return ans


def format_params(sp_str, param_count):

    params = []
    for i in range(1, param_count+1):
        param = sp_str[i].strip()
        try:
            param = int(param)
        except ValueError:
            pass
        params.append(param)
    return params