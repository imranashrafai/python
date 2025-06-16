print("======================== Dictionary ========================")
# use for mapping
dis = {1001: "M. Mohsin", 1003: "M. Huzaifa", 1006: "M. Imran"}
print(dis.values())
print(dis.keys())


for keys in dis.keys():
    print(f"Value corresponding to the key {keys} is {dis[keys]}")


# print values with keys
print(dis.items())


for key, item in dis.items():
    print(f"Value corresponding to the key {key} is {item}")


print("======================== Dictionary Methods ========================")
clea = {101: "Imran", 102: "Ali", 103: "Mani", 104: "Jutt"}
ep1 = {101: "Imran", 102: "Ali", 103: "Mani", 104: "Jutt"}
ep2 = {90: "Irfan", 94: "Abdul"}
# merge two dictionaries
ep1.update(ep2)
print(ep1)
# pop the element with its key from dictionary
ep1.pop(104)
print(ep1)
# clear the dictionary and return empty dictionary like => {}
clea.clear()
print(clea)
#del the element against the given key if key will not give it will del the dictionary
del ep2[90]
print(ep2)
