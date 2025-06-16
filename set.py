print("======================== Sets ========================")
# do not maintain order and output can change on each run of program
imran = {1, 2, 4, 1, 9, 8, 5}
print(imran)


# syntax of dist and set is same
# form making empty set

syntax = set()
print(type(syntax))

sets = {"imran", 121, "ashraf", 10, 12.34}
print(sets)

for value in sets:
    print(value, end=" ")


print("\n======================== Sets Methods ========================")
s1 = {1, 2, 3, 4}
s2 = {7, 8, 9, 6, 5}
s3 = {3, 4}
print(s1.union(s2))
s1.intersection(s2)
print(s1)
# update set1 by common elements in both sets
# s1.intersection_update(s3)
# print(s1)

print(s1.issuperset(s3))
print(s3.issubset(s1))
# return that elements which are not common
print(s1.symmetric_difference(s3))
# uncommon elements which are present in first set only
print(s1.difference(s3))
print(s3.clear())
# delete permanently the set
del s3
# pop a element from the set and element will randomly pop
ele = s2.pop()
print(ele)
set1 = {1, 2, 3, 4, 5, 6, 7}
# if element not found it will not give an error
set1.discard(3)
print(set1)
# if element not found it will give an error
set1.remove(9)
print(set1)
