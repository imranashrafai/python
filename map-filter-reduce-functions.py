print("========================Map,Filter & Reduce Function========================")

from functools import reduce

# Map Function use to perform specific task on iterable thins like list
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cube = lambda x: x * x * x

# it will return object and you have to change it to any datatype you wanna
mappedLi = list(map(cube, li))
print("Mapped List(Cube of each element of list) is :", mappedLi)

# Filter function perform specific task on iterable things to check conditions:
newli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filteredLi = list(filter(lambda x: x > 6, newli))
print("Filtered List is: ", filteredLi)

# Reduce function perform specific task on iterable things eg. add,sub,division :
# you should impor this (from functools import reduce) to use reduce function
newnewli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
reducedLi = reduce(lambda x, y: x + y, newnewli)
print(reducedLi)
