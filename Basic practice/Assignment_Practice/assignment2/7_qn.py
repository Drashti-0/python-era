while True:
    n = input("Enter your number: ")

    if n == "Quit":
        print("Thank you for using our systeam")
        break

    n = int(n)

    if n > 0:
        print("Positive number")
    elif n < 0:
        print("Negative number")
    else:
        print("Zero")