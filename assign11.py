atomic_weight = float(input("input atomic_weight: "))
amount_of_elements = float(input("input amount_of_elements: "))12
avogadro_number = 6.022*(pow(10,23))
def num_atom(amount_of_elements,atomic_weight = 196.67):
    num_atom = (atomic_weight/amount_of_elements)*avogadro_number
    return num_atom
print("num_atom: ",num_atom(amount_of_elements,atomic_weight))

