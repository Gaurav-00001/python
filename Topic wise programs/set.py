collection = set()
collection.add(1)
collection.add(3)
collection.add(5)
collection.add(7)
collection.add(8)
print(collection)
collection.remove(8)
collection.pop()
print(collection)

set2= {"Gaurav", 2,3, 46}

print(collection.intersection(set2))
print(collection.union(set2))
collection.clear()
print(collection)