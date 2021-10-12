def slope():
    x1 = float(input("Enter the x-coordinate of point1: "))
    y1 = float(input("Enter the y-coordinate of point1: "))
    x2 = float(input("Enter the x-coordinate of point2: "))
    y2 = float(input("Enter the y-coordinate of point2: "))
    result = (y2 - y1)/(x2 - x1)
    trunc_numba = ""
    if result > 0:
        for i in range(7):
            trunc_numba += str(result)[i]
        print(f"The slope for the line that connects two points ({x1}, {y1}) and ({x2}, {y2}) is {trunc_numba}")
    else:
        for i in range(8):
            trunc_numba += str(result)[i]
        print(f"The slope for the line that connects two points ({x1}, {y1}) and ({x2}, {y2}) is {trunc_numba}")


def runway_len():
    v = float(input("Enter the plane's takeoff speed in m/s: "))
    a = float(input("Enter the plane's acceleration in m/s**2: "))
    length = v ** 2 / (2 * a)
    print("The minimum runway length needed for this airplane is {:.4f} meters".format(length))


def tip_calc():
    subtotal = int(input("Enter the subtotal: "))
    tip_amnt = int(input("Enter the tip amount as percentage: "))
    print("Subtotal: ${:,.2f}".format(subtotal))
    print("Tip: ${:,.2f}".format(subtotal * tip_amnt / 100))
    print("Total: ${:,.2f}".format(subtotal + subtotal * tip_amnt / 100))


def hex_area():
    side = int(input("Enter the side of the length of the hexagon: "))
    area = (3 / 2) * math.sqrt(3) * math.pow(side, 2)
    print("The area of a hexagon with side {:.3f} is {:.3f}".format(side, area))


