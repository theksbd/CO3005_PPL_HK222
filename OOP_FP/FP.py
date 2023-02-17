# # Recursive
# def lstSquare(n):
#     if n == 1:
#         return [1]
#     else:
#         lst = lstSquare(n-1)
#         lst.append(n*n)
#         return lst

# # List Comprehension
# def lstSquare(n):
#     lst = range(1, n+1)
#     return [x*x for x in lst]

# # Functional Programming
# def lstSquare(n):
#     return list(map(lambda x: x*x, range(1, n+1)))

# Let lst be a list of integer and n be any value, use list comprehension approach to write function dist(lst,n) that returns the list of pairs of an element

# def dist(lst, n):
#     return [(x, n) for x in lst]

# # Functional Programming
# def dist(lst, n):
#     return list(map(lambda x: (x, n), lst))

# # Recursive
# def dist(lst, n):
#     if len(lst) == 0:
#         return []
#     if len(lst) == 1:
#         return [(lst[0], n)]
#     else:
#         lst1 = dist(lst[:-1], n)
#         lst1.append((lst[-1], n))
#         return lst1

# print(dist([1, 2, 3, 4, 5], 10))

# Let lst be a list of integer and n be an integer, use recursive approach to write function lessThan(lst,n) that returns the list of all numbers in lst less than n.
# # Recursive
# def lessThan(lst, n):
#     if len(lst) == 0:
#         return []
#     if len(lst) == 1:
#         if lst[0] < n:
#             return [lst[0]]
#         return []
#     else:
#         lst1 = lessThan(lst[:-1], n)
#         if lst[-1] < n:
#             lst1.append(lst[-1])
#         return lst1


# # List Comprehension
# def lessThan(lst, n):
#     return [x for x in lst if x < n]

# # Functional Programming
# def lessThan(lst, n):
#     return list(filter(lambda x: x < n, lst))

# print(lessThan([1, 2, 3, 4, 5], 3))

# Let lst be a list of a list of element, use recursive approach to write function flatten(lst) that returns the list of all elements

# def flatten(lst):
#     if len(lst) == 0:
#         return []
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         lst1 = flatten(lst[:-1])
#         lst1.extend(lst[-1])
#         return lst1

# # List Comprehension
# def flatten(lst):
#     return [x for y in lst for x in y]

# # Functional Programming
# from functools import reduce


# def flatten(lst):
#     return list(reduce(lambda total, curr: total + curr, lst, []))


# print(flatten([[1, 2, 3], [4, 5], [6, 7]]))
