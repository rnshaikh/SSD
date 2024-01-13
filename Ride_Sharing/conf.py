from src.driver import Driver
from src.rider import Rider

COMMANDS = {
	
	"ADD_DRIVER": {
		"obj": Driver,
		"param_count": 3,
		"action": "add_driver"
	},
	"ADD_RIDER":{
		"obj": Rider,
		"param_count": 3,
		"action": "add_rider"
	},
	"MATCH": {
		"obj": None,
		"param_count": 1,
		"action": "match_driver"
	},
	"START_RIDE":{
		"obj": None,
		"param_count": 3,
		"action": "start_ride"
	},
	"STOP_RIDE": {
		"obj": None,
		"param_count": 4,
		"action": "stop_ride"
	},
	"BILL": {
		"obj": None,
		"param_count": 1,
		"action": "get_fair"
	}

}

BASE_PRICE = 50
PER_KM = 6.5
PER_MINUTE = 2
SERVICE_TAX = 0.2
PERC_DIVISOR = 100
TWO = 2
MAX_DRIVER_SHOW = 5
ZERO_INIT = 0
NEGATIVE_INIT = -1
TENTH = 10
HALF_PART = 0.5
NEGATIVE_HALF_PART = -0.5
