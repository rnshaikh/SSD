from src.rider import Rider
import conf
from src.ride_sharing  import RideSharing
from src.utils import format_params


def execute_action_with_obj(action_info, sp_str, ride_sharing):

	if action_info and action_info.get('obj', None):
		param_count = action_info.get('param_count')
		params = format_params(sp_str, param_count)
		obj = action_info.get('obj')(*params)
		action = action_info['action']
		getattr(ride_sharing, action)(obj)


def execute_action_without_obj(action_info, sp_str, ride_sharing):

	if action_info and not action_info.get('obj', None):
		param_count = action_info.get('param_count')
		params = format_params(sp_str, param_count)
		action = action_info['action']
		getattr(ride_sharing, action)(*params)



def program_driver(file_path):

	fs = open(file_path, 'r')
	ride_sharing = RideSharing()

	for query in fs:

		sp_str = query.split(" ")
		action_info = conf.COMMANDS.get(sp_str[conf.ZERO_INIT], None)

		execute_action_with_obj(action_info, sp_str, ride_sharing)
		execute_action_without_obj(action_info, sp_str, ride_sharing)

		# if action_info and action_info.get('obj', None):
		# 	param_count = action_info.get('param_count')
		# 	params = format_params(sp_str, param_count)
		# 	obj = action_info.get('obj')(*params)
		# 	action = action_info['action']
		# 	getattr(ride_sharing, action)(obj)

		# if action_info and not action_info.get('obj', None):
		# 	param_count = action_info.get('param_count')
		# 	params = format_params(sp_str, param_count)
		# 	action = action_info['action']
		# 	getattr(ride_sharing, action)(*params)

