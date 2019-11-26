n = int(input("n: "))
string= str(input("string: "))
def generate_n_chars(n,string):
    result = ""
    for i in range(n):
        result +=string
    print(result)
generate_n_chars(n,string)