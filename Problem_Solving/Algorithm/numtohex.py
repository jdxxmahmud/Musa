def hexing(x):

    n = ""

    rem = str(x % 16)

    x = int(x / 16 )

    x = str(x)

    if x == "10":
        x = "A"
    elif x == "11":
        x = "B"
    elif x == "12":
        x = "C"
    elif x == "13":
        x = "D"
    elif x == "14":
        x = "E"
    elif x == "15":
        x = "F"
    
    if rem == "10":
        rem = "A"
    elif rem == "11":
        rem = "B"
    elif rem == "12":
        rem = "C"
    elif rem == "13":
        rem = "D"
    elif rem == "14":
        rem = "E"
    elif rem == "15":
        rem = "F"

    n = n + x + rem
    return print(n)


hexing(0)
