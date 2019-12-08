number = float(input("number: "))
def distance_from_zero(number):
    if isinstance(number, float):
        return float(abs(number))
print("exact value: ",distance_from_zero(number))
