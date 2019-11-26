one_charactor = str(input("one_charactor: "))
def takes_a_charactor(one_charactor):
    if (one_charactor == 'a' or one_charactor == 'e' or one_charactor == 'i' or one_charactor == 'o' or one_charactor == 'u'
   or one_charactor == 'A' or one_charactor == 'E' or one_charactor == 'I' or one_charactor == 'O' or one_charactor == 'U'):
        z = "true"
    else:
        z = "false"
    return z
print(takes_a_charactor(one_charactor))