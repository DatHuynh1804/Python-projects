def convert(value,unit,table):
    return value * table.get(unit.lower(),None)
mass_units = {"kg":1,"g": 1e-3,"ton": 1000,"mg": 1e-6}
acceleration_units = {"m/s^2":1,"dm/s^2": 1e-1,"cm/s^2":1e-2}
distance_units = {"km": 1e+3,"m":1,"dm":1e-1,"cm":1e-2,"mm":1e-3}
G = 6.67*1e-11
while True:
    print("---Physics calculator---")
    print("1. Net force (F = m.a)")
    print("2. Gravitational force (Fg=G(M1/M2)/r^2")
    print("3. Exit")
    x = int(input("What do you want to do?: "))
    if x == 1:
        mass_unit = input("Enter your unit of mass (ton, kg, g, mg): ").lower()
        m = convert(float(input("Enter your mass: ")),mass_unit , mass_units)
        acceleration_unit = input("Enter your acceleration unit (m/s^2, dm/s^2, cm/s^2): ").lower()
        a = convert(float(input("Enter your acceleration value: ")),acceleration_unit , acceleration_units)
        if m > 0 and a is not None:
            print("The net force F is {:.2f} N".format(m*a))
        else:
            print("Your unit choice is invalid, please try again!")
    elif x == 2:
        mass_unit = input("Enter your unit of mass (ton, kg, g, mg): ").lower()
        M1 = convert(float(input("Enter your first mass: ")),mass_unit , mass_units)
        M2 = convert(float(input("Enter your second mass: ")),mass_unit , mass_units)
        distance_unit = input("Enter your unit of distace (km, m, dm, cm, mm): ")
        r = convert(float(input("Enter your distance: ")),distance_unit , distance_units).lower()
        if r == 0:
            print("Distance must be larger than 0!")
        elif (M1 and M2 and r) > 0:
            print("The gravitational force Fg = {:.2e} N".format(G*(M1*M2)/r**2))
    elif x == 3:
       print("Goodbye!")
       break
    else:
        print("Your choice is invalid, please try again!")
        