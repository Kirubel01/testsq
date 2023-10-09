def main():
    total = 0
    num = int(input("Enter a positive integer (enter 0 to end): "))
    while num != 0:
        total += num
        num = int(input("Enter a positive integer (enter 0 to end): "))
    print("The sum of the positive integers is:", total)

if __name__ == "__main__":
    main()