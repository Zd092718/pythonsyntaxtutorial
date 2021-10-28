s = 'abcdef'

print(s[0])
print(s[0:3])
# 2 is a skip
print(s[0:4:2])

# find returns index
print(s.find('c'))
# replaces first item with second
print(s.replace('d', 'z'))
# count counts number of instances of passed value
print(s.count('a'))
