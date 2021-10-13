import math

# Input numerator and denominator, calculates gcd
numer = int(input("Enter a numerator (value must be greater than 0): "))
while numer <= 0:
    numer = int(input("Please re-enter the numerator (value must be greater than 0): "))
denom = int(input("Enter a denominator (value must be greater than 0): "))
while denom <= 0:
    denom = int(input("Please re-enter the denominator (value must be greater than 0): "))

# Determines if a fraction is proper or improper
improperty = ""
if numer > denom:
    print(f"{numer}/{denom} is an improper fraction")
    improperty = "improper"
else:
    print(f"{numer}/{denom} is a proper fraction.")
    improperty = "proper"

# Simplifies a fraction, leaves it be if the fraction is irreducible
divisor = math.gcd(numer, denom)
if divisor != 1:
    print(f"This {improperty} fraction can be reduced to: {numer // divisor}/{denom //divisor}")
else:
    print(f"This {improperty} fraction can not be reduced any further.")

# Calculates either the mixed number or the whole number of an improper fraction
whole_num = numer // denom
leftover = numer % denom
if leftover == 0:
    print(f"The whole number is {whole_num}")
elif whole_num == 0:
    pass
else:
    print(f"The mixed number is {whole_num} and {leftover // divisor}/{denom // divisor}")
