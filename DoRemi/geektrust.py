import sys

from src.program_driver import ProgramDriver


def main(file_path):

    handler_obj = ProgramDriver()
    handler_obj.parse_file(file_path)


if __name__ == "__main__":

    file_path = sys.argv[1]
    main(file_path)