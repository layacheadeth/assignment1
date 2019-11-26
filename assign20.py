word= str(input("input word:"))
def _palindrome(word):
    string = ""
    for i in word:
        string = i + string
    if string == word:
        a = "true"
    elif string != word:
        a = "false"
    punc = ["!","?","."]
    if word.contain(punc)
        remove.punc()
    print(a)
_palindrome(word)
