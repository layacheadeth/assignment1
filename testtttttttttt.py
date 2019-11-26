mdict = {'1':'bagus','2':'ngak','3':'tanpa','4':'tapi'}
bab = {'1':'tidak','2':10,'color':'yellow'}
for i in mdict:
    print(mdict[i])
for a,b in mdict.items():
    print(a)
    print(b)
for b in mdict.values():
    print(b)
all = [mdict,bab]
print(all[0]['3'])
var_string="andreas"
print(var_string[::-1])
print(var_string[1:-1:2])
print(var_string[2:-1])
def f(*a):
    print(a)
f("asd","dst","qwe")