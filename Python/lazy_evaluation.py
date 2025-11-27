# LAzy evaluation

# It is a technique used to save memory and make the program 
# more efficient and fast. For example

# 1:
# range(1000000) function does not return a list of 1 million 
# numbers, instead it returns a range object which is iterable.

# We see "lazy evaluation" used in many of Python’s libraries. 
# For example, the dictionary class supports methods keys( ),
# values( ), and items( ), which respectively produce a “view” 
# of all keys, values, or (key,value) pairs within a dictionary. 
# None of these methods produces an explicit list of results. 
# Instead, the views that are produced are iterable objects 
# based upon the actual contents of the dictionary   
