# list are mutable
f = ['orange', 'melon', 'banana', 'mango']
f.append('Pineapple')

f.insert(1,"Kiwi")
print(f)

# remove item by description
f.remove("melon")
# remove item based index provided
f.pop(2)