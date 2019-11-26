def calc_weight_on_planet(weight_on_earth,surfacegravityonplanet = 23.1):
    mass = weight_on_earth / 9.8
    weightonplanet = float(mass * surfacegravityonplanet)
    return weightonplanet
weight_on_earth = float(input("weightonearth: "))
surfacegravityonplanet = float(input("surfacegravityonplanet: "))
print(("weight on other planet: "),calc_weight_on_planet(weight_on_earth,surfacegravityonplanet))

