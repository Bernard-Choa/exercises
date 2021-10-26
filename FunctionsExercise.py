def convert_to_days():
    hr = int(input("Enter number of hours: "))
    mnt = int(input("Enter number of minutes: "))
    sec = int(input("Enter number of seconds: "))
    def get_days(h, m, s):
        return (h / 24) + (m / 1440) + (s / 86400)
    print(" ")
    print(f"The number of days is: {round(get_days(hr, mnt, sec), 4)}")


def calc_weight_on_planet(m, g=23.1):
    if g == 9.8:
        print(m / 1)
    else:
        print(round(m * g / 9.8, 14))


def num_atoms(gr, aw=196.97):
    n = gr / aw
    m = n * (6.022 * 10 ** 23)
    print(m)


def calc_new_height():
    w = int(input("Enter the current width: "))
    h = int(input("Enter the current height: "))
    n_w = int(input("Enter the desired width: "))
    print(f"The corresponding height is: {n_w * h / w}")


def convert_temp():
    f = int(input("Enter the temperature in Fahrenheit: "))
    print(f"The temperature in Fahrenheit is: {f}")
    print(f"The temperature in Celcius is: {(f-32) * 5 / 9}")
    print(f"The temperature in Kelvin is: {(f-32) * 5 / 9 + 273.15}")
