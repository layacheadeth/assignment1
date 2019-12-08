word = str(input("english word: "))
print(word.isalpha())
new = " "
for i in word:
    new = i + new
new = new + "ay"
print(new)