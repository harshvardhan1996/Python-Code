# =============================================================================
# Python : Unique pairs in list
# 
# Sometimes, while working with python list, we can have a binary matrix(Nested list having  elements).
# And we can have a problem in which we need to find the uniqueness of a pair. A pair is unique irrespective of order, it doesn't appear again in list.
# Lets discuss certain way in which this task can be performed.
# 
# Method : Using frozenset() + Counter() + list comprehension
# =============================================================================
 

from collections import Counter

test_list = [[5,6,1],[9,8,2],[8,9,2],[1,4],[1,6,5],[10,1]]

print("The Original list is : " + str(test_list))

# frozenset() is used for ignoring the ordering,
# Counter() is used to perform the task of checking the uniqueness and iteration is done using list comprehension.
# printing original list 
print("The original list is : " + str(test_list)) 
  
# Unique pairs in list 
# using frozenset() + Counter() + list comprehension 
temp = Counter(frozenset(ele) for ele in test_list) 
res = [temp[frozenset(ele)] == 1 for ele in test_list] 
  
# printing result 
print("The Unique status of elements is " + str(res))