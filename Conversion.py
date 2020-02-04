def dtb(x):  # Convert decimal to binary
    out = ""  # An output string
    while x > 0:  # While the input is greater than zero
        hold = x % 2  # Store the modulo (Remainder) of x by 2
        out += str(hold)  # Concatenates the string form of hold to the out variable
        x = int(x/2)  # Half the value of x
    out = out[::-1]  # Reverse out
    return out


def btd(x):  # Convert binary to decimal
    max_power = len(x) - 1   # The maximum possible power which is the number of items in string
    out = 0  # Creates output variable
    for i in x:  # For each item in x
        out += (int(i) * (2 ** max_power))  # Adds the value to out
        max_power -= 1  # Decrements max_power
    return out


print(dtb(10))
print(btd("1010"))
