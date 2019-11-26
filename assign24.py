hours = int(input("Enter the hours: "))
rate = int(input("Rate: "))
def pay(hours,rate):
    return (hours*rate*1.5)
print("Pay: ",pay(hours,rate))