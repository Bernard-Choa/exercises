def ramp_angle():
    m = int(input("Enter the mass of the cart (in kg): "))
    F = int(input("Enter the force to push the cart (in N): "))
    result = F / (m * 9.8)
    trunc_num = "{:.1f}"
    print("Angle of the ramp is {:.1f} degrees".format(math.degrees(math.asin(result))))


def if_triangle():
    edge1 = float(input("Enter length of edge1: "))
    edge2 = float(input("Enter length of edge2: "))
    edge3 = float(input("Enter length of edge3: "))
    if edge1 + edge2 > edge3 and edge1 + edge3 > edge2 and edge2 + edge3 > edge1:
        print("The perimeter is {}".format(edge1 + edge2 + edge3))
    else:
        print("Perimeter cannot be calculated: input is invalid")


def wind_chill_temp():
    ta = int(input("Enter the temperature in Fahrenheit: "))
    while not -58 < ta < 41:
        print("Temperature must be between -58F and 41F")
        ta = int(input("Please re-enter the temperature in Fahrenheit: "))

    v = int(input("Enter the wind speed in miles per hour: "))
    while v < 2:
        print("Speed must be greater than or equal to 2")
        v = int(input("Please re-enter the wind speed in miles per hour: "))

    twc = 35.74 + 0.6215 * ta - 35.75 * v ** 0.16 + 0.4275 * ta * v ** 0.16
    print("The wind chill index is {:.3f}".format(twc))


def software_sales():
    quantity = int(input("Enter the number of packages purchased: "))
    if 0 < quantity < 10:
        print("Discount Amount @ 0% : $ {:.2f}".format(0))
        print("Total Amount: $ {:.2f}".format(99 * quantity))
    elif 9 < quantity < 20:
        print("Discount Amount @ 10% : $ {:.2f}".format(99 * quantity * 10 / 100))
        print("Total Amount: $ {:.2f}".format(99 * quantity * 90 / 100))
    elif 19 < quantity < 50:
        print("Discount Amount @ 20% : $ {:.2f}".format(99 * quantity * 20 / 100))
        print("Total Amount: $ {:.2f}".format(99 * quantity * 80 / 100))
    elif 49 < quantity < 100:
        print("Discount Amount @ 30% : $ {:.2f}".format(99 * quantity * 30 / 100))
        print("Total Amount: $ {:.2f}".format(99 * quantity * 70 / 100))
    elif quantity > 99:
        print("Discount Amount @ 40% : $ {:.2f}".format(99 * quantity * 40 / 100))
        print("Total Amount: $ {:.2f}".format(99 * quantity * 60 / 100))





