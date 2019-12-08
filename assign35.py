words=str(input("word: "))
word= words.split()
def find_longest_word(a=[]):
    list_of_len_words = []
    for i in a:
        list_of_len_words.append(len(i))
    print(max(list_of_len_words))
find_longest_word(word)