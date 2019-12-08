words=str(input("word: "))
word= words.split()
n = int(input("n: "))
def find_longest_word(a=[]):
    list_of_len_words = []
    for i in a:
        list_of_len_words.append(len(i))
        if len(i) > n:
            print(i)
find_longest_word(word)