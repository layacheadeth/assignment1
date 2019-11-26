def convert_to_day():
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))
    round(get_days(hours, minutes, seconds),4)
    print("number of days:  ",get_days(hours,minutes,seconds))
def get_days(hours,minutes,seconds):
    days = float(hours+minutes/60+seconds/3600)/24
    return days
convert_to_day()

