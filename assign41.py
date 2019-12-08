prices= {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}
j=0
for i in prices:
    print(i)
    print("price: ",prices[i])
    j+=1
    print("stock: ",j)
total = 0
j = 0
for i in prices:
    j += 1
    x = prices[i]* j
    print(x)
    total = total + x
print(total)