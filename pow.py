import sys

def main():
    args = sys.argv

    with open(args[1]) as numbers_file:
        for number in numbers_file:
            print(pow(number))

def pow(number):
    return int(number) * int(number)

if __name__ == "__main__":
    main()
