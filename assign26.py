text = str(input("text: "))
def translate(text):
    new = " "
    for i in text:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            new = new + i
        else:
            new = new + i + "o" + i
    return new
print(translate(text))