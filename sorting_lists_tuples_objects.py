# In this one we will look into how to sort a few different types in python

li = [9,1,4,8,5,6,7,2,3]

s_li = sorted(li)

print('Sorted variable:\t', s_li)


# if we want the original variable to be sorted we will have to use the sort method
li.sort()
# difference between sorted list and sort() is that sort returns none after sorting the list whereas
# sorted returns sorted list that is why we are able to set it to a new variable
print('Original variable:\t', li) 

# How we can sort in descending order
s_li = sorted(li, reverse=True)

print('Sorted variable:\t', s_li)

li.sort(reverse=True)
print('Original variable:\t', li) 


# sort() works only on list, we can use sorted() for tuples, dicts, etc,.

# Tuple

tup = (9,1,4,8,5,6,7,2,3)
# tup.sort(); tuple doesn't have sort method
# what we can do is we can use sorted function
s_tup = sorted(tup)
print('Sorted tuple:', s_tup)

# Dictionary

di = {'name' : 'vickee', 'job': 'programming', 'age': None, 'os': 'ubuntu'}
s_di = sorted(di)
# what sorted will do is just sort the keys
print('Dict', s_di)

