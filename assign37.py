sentence = str(input("sentence: "))
pan=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Pan=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def pangram(sentence):
    for i in sentence:
        if i in pan or i in Pan:
            a = "it is a pangram"
        else:
            a = "it is not a pangram"
    return a
print(" ",pangram(sentence))
