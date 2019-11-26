def calc_new_height():
    current_width = float(input("current width: "))
    current_height = float(input("current height: "))
    desired_width= float(input("desired width: "))
    corresponding_height= (desired_width*current_height)/current_width
    return corresponding_height
print("corresponding height: ",calc_new_height())