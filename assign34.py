word = str(input("words: "))
words = word.split()
new_words = []
for i in words:
    new_words.append(len(i))
j = 0
for x in new_words:
    print(words[j] + ": " + str(new_words[j]) + ", " , end = "")
    j+=1