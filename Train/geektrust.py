import sys

from src.program_driver import ProgramDriver


def main(file_path):

	p_obj = ProgramDriver()
	p_obj.parse_commands(file_path)



if __name__ == "__main__":

	file_path = sys.argv[1]
	main(file_path)
