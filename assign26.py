text = str(input("text: "))
def translate(text):
    new = ""
    for i in text:
        if i in ['a','e','i','o','u',' ']:
            new = new + i
        else:
            new = new + i + "o" + i
    return new
print(translate(text))
