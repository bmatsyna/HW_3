# 1. Define the id of next variables
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(list(map(id, (int_a, str_b, set_c, lst_d, set_c, dict_e))))
# 2. Append 4 and 5 to the lst_d and define the id one more time
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
# 3. Define the type of each object from step 1
print(list(map(type, (int_a, str_b, set_c, lst_d, set_c, dict_e))))
# 4. Check the type of the objects by using isinstance
print(isinstance(int_a, float))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))
# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(10, 20))
# 6. By passing index numbers into the curly braces.
apples = 10
peaches = 20
print("Anna has {0} apples and {1} peaches.".format(apples, peaches))
# 7. By using keyword arguments into the curly braces
print("Anna has {ap} apples and {pe} peaches.".format(ap=apples, pe=peaches))
# 8*. With indicators of field size (5 chars for the first and 3 for the second)

# 9. With f-strings and variables
print(f"Anna has {apples} apples and {peaches} peaches.")
# 10. With % operator
print("Anna has %s apples and %s peaches." % (apples, peaches))
# 11*. With variable substitutions by name (hint: by using dict)
fruits = {"apples": 10,
          "peaches": 20}
print("Anna has {apples} apples and {peaches} peaches.".format(**fruits))
# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
# 12. Convert (1) to list comprehension
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
# 13. Convert (2) to regular for with if-else
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# 14. Convert (3) to dict comprehension
dict_comprehension = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comprehension)
# 15*. Convert (4) to dict comprehension
d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)
# 16. Convert (5) to regular for with if
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x**3
print(d)
# 17*. Convert (6) to regular for with if-else
d = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d[x] = x ** 3
    else:
        d[x] = x
print(d)

# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
#
# 18. Convert (7) to lambda function
lmb_1 = lambda x, y: x if x < y else y
print(lmb_1(2, 3))
# 19*. Convert (8) to regular function
def foo_2(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

print(foo_2(10, 8, 7))

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 20. Sort lst_to_sort from min to max
print(sorted(lst_to_sort))
# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst_to_sort)))
# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
lst_2 = list(map(lambda x: x + 3, list_A))
# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda elem: elem % 2 == 1, lst_to_sort)))
# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print(list(filter(lambda elem: elem < 0, range(-10, 10))))
# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print(list(filter(lambda x: x in list_1, list_2)))
