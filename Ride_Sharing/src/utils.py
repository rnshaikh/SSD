import math
import conf

from heapq import heappush, heappop


def my_round(val, n):
    part = val * conf.TENTH ** n
    delta = part - int(part)
    
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
    for i in range(conf.ONE_INIT, param_count+conf.ONE_INIT):
        param = sp_str[i].strip()
        try:
            param = int(param)
        except ValueError:
            pass
        params.append(param)
    return params



def push_driver(match_drivers, temp):
    for temp_driver in temp:
        heappush(match_drivers, temp_driver)


def push_match_driver(match_drivers, driver, ans):

    if ans <= conf.MAX_DRIVER_SHOW:
        heappush(match_drivers, (ans, driver))


def check_driver_within_range(rider, drivers, driver, match_drivers):

    if drivers[driver].is_available():
        rider_location = rider.get_location()
        driver_location = drivers[driver].get_location()
        ans = calculate_ecd(rider_location[0],rider_location[1], driver_location[0], driver_location[1])
        push_match_driver(match_drivers, driver, ans)


def match_driver(rider, drivers):

    match_drivers = []
    for driver in drivers:
        check_driver_within_range(rider, drivers, driver, match_drivers)

    return match_drivers

