
import sys

from src.program_driver import program_driver


def main():

	file_path = sys.argv[1]
	program_driver(file_path)
	
if __name__ == "__main__":

	main()