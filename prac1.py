number= int(input("n: "))
def fac(number):
    if number == 1:
        return number
    elif number<1:
        return "-"
    else:
        return number*fac(number-1)
print("result: ",fac(number))
def find_the_prime_numbers_with_index():
    number= int(input("Enter the index of the prime number: "))
    prime_number=[2,3,5,7]
    for i in range(8,100):
        if number<1:
            print("there's no prime number with that index")
            exit()
        elif i%2 !=0 and i%3 !=0 and i%5 !=0 and i%7 !=0:
            prime_number.append(i)
    return (prime_number[number-1])
print(find_the_prime_numbers_with_index())
for x in "Mississippi".split("i"):
    print(x, end="")
