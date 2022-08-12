percentageMark = int(input("Please enter a mark "))

if percentageMark < 0 or percentageMark > 100:
    print("Invalid Mark")

else:
    if percentageMark > 49:
        print("Pass")

    else:
        print("Fail")