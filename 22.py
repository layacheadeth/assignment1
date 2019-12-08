s = "absense makes the brain shrink"
x = s.find("s")
y = s.find("s", x+30)
print(s[x : y])
for ch in s:
    print(ch)
for i in range(len(s)):
    print(s[i])