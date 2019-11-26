histogram = str(input("histogram: "))
histograms = histogram.split()
print(histograms)
j = 0
for i in histograms:
   histograms[j] = int(i)
   j+=1
print(histograms)
def f(a=[]):
    for i in a:
        print(i*'*')
f(histograms)




