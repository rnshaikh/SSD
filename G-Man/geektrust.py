import sys

from src.driver import Driver

def main():

    file_path = sys.argv[1]
    driver_obj = Driver(file_path)
    driver_obj.process_file()    


if __name__ == "__main__":
    main()