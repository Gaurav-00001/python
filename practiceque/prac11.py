#WAP to check if a list contains a palindrome of elements.
list=[1,2,2,1]
copy_list= list.copy()
copy_list.reverse()
if (list==copy_list):
    print("list is a palindrome")
else:
    print("list is not a palindrome")