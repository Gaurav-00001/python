tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


search_num = int(input("Enter a number you want to search: "))

for num in tup:
    if search_num == num:
        print("Gotcha! The number is found in the tuple at index:", tup.index(num))
        break
else:
    print("Not found!")