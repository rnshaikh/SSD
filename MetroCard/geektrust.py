import sys

import conf

from src.program_driver import ProgramDriver

def main():
	input_file = sys.argv[conf.INIT_ONE]
	driver_obj = ProgramDriver()
	driver_obj.add_station()
	driver_obj.parse_commands(input_file)


if __name__ == "__main__":
	main()