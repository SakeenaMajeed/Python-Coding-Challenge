# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position
          # of where it was found


x = ( 1, 2, 3, 4, 5, 3, 6, 7, 8, 3, 9, 10, 3)
y = x.count(3) 
print(y)


s = ("Apple", "Banana", "Cherry")
h = s.index("Banana")
print(h)

#  Useful functions that work with tuples:

# Function	Description
# len()	Returns the length of the tuple
# max()	Returns the largest value in the tuple
# min()	Returns the smallest value in the tuple
# tuple()	Converts a list into a tuple
# sum()	Returns the sum of all elements in the tuple
# sorted()	Returns a sorted list of the specified iterable object


my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
print(sum(my_tuple))
print(tuple(my_tuple))

tuple1 = (1, 88, 90, 4, 5)
print(sorted(tuple1))


# tuple in concetination

tuple_one = (1, 2, 3, 4, 5)
tuple_two = (6, 7, 8, 9, 10)
tuple_three = tuple_one + tuple_two 
print(tuple_three)


# tuple in membership

tuple_four = (1, 2, 3, 4, 5)
print(3 in tuple_four)
print(6 in tuple_four)

#tuple in iteration

tuple_five = (1, 2, 3, 4, 5)
for x in tuple_five:
   print(x)


# tuple in slicing

tuple_six = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_six[2:5])
print(tuple_six[:5])
print(tuple_six[5:])
print(tuple_six[:])
print(tuple_six[::2])
print(tuple_six[1::2])
print(tuple_six[::-1])