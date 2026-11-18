# Roman to integer
def roman_to_int(x):

    roman_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    x = x.replace("IV", "IIII")
    x = x.replace("IX", "VIIII")
    x = x.replace("XL", "XXXX")
    x = x.replace("XC", "LXXXX")
    x = x.replace("CD", "CCCC")
    x = x.replace("CM", "DCCCC")
    for num in x:
        total += roman_val[num]
    return total


s = "XIVM"
roman_to_int(s)
