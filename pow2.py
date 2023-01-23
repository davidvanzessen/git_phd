import sys

def main(input_path):
    with open(input_path) as numbers_file:
        for number in numbers_file:
            try:
                print(pow(number))
            except ValueError:
                print("Could not parse:", number.strip())
                sys.exit(1)

def pow(number):
    return int(number) * int(number)

if __name__ == "__main__":
    args = sys.argv
    
    main(args[1])