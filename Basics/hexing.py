def hexing(x: int )

    quo = num

    rem = 0

    val = ""


    while quo != 0:

        rem = str(quo % 16)

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

        val = rem + val

        quo = int(quo / 16)

    return val

