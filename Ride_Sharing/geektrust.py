
import sys

from src.driver import Driver
from src.rider import Rider
import conf
from src.ride_sharing  import RideSharing


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


def main():

	file_path = sys.argv[1]
	fs = open(file_path, 'r')
	ride_sharing = RideSharing()

	for query in fs:

		sp_str = query.split(" ")
		action_info = conf.COMMANDS.get(sp_str[0], None)

		if action_info and action_info.get('obj', None):
			param_count = action_info.get('param_count')
			params = format_params(sp_str, param_count)
			obj = action_info.get('obj')(*params)
			action = action_info['action']
			getattr(ride_sharing, action)(obj)

		if action_info and not action_info.get('obj', None):
			param_count = action_info.get('param_count')
			params = format_params(sp_str, param_count)
			action = action_info['action']
			getattr(ride_sharing, action)(*params)


if __name__ == "__main__":

	main()