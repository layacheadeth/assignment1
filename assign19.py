word= str(input("input word:"))
def _palindrome(word):
    string = ""
    for i in word:
        string = i + string
    if string == word:
        a = "true"
    elif string != word:
        a = "false"
    print(a)
_palindrome(word)


