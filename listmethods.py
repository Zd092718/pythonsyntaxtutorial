a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)

s = "a b c d e f"
# split adds individual characters to a list
z = s.split()
print(z)

if 'a' in z:
    print("A is in z")
else:
    print("A is not in z")

for i in z:
    print(i)

#  sort sorts by ascending order
g = [4, 5, 3, 2, 7]
g.sort()
print(g)
g.reverse()
print(g)
