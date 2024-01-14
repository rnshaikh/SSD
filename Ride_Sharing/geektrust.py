
import sys
import conf
from src.program_driver import program_driver


def main():

	file_path = sys.argv[conf.ONE_INIT]
	program_driver(file_path)
	
if __name__ == "__main__":

	main()