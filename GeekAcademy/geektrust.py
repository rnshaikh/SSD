import sys

from src.driver import Driver


def main():
    file_path = sys.argv[1]
    obj = Driver(file_path)
    obj.process_command()


if __name__ == "__main__":
    main()

