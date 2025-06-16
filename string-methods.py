

print("========================String Methods========================")
# Strings are Immutable: can not change
a = "imran!!!"
b = "IMRAN"
print(
    "Lower to Upper " + a.upper()
)  # in this it can not change the original string it just make new string and then convert into Upper case
print("Upper to Lower " + a.lower())

# removing tralling char at the end of string
print(a.strip("!"))
# replace in all coccurences of specific string
print(a.replace("imran", "ali"))
# capital 1st character
c = "Hello i am imran imran AShraf Learning pyTHON"
print(a.capitalize())
print(c.capitalize())
d = "welcome to console"
# center method give 25 spaces to the left of string
print(d.center(50))
# tell how many time words your string have
print(c.count("imran"))
# give boolean result check that given string end eith specific word or not
print(d.endswith("console"))
# we can give specific perid to check this
print(d.endswith("to", 8, 10))
# return index number of first most word only if not found then return -1 only
print(d.find("to"))
# return index number of first most word only if not found then give error
# print(d.index("imran"))
# return true if string has alphabets and numbers in string  spaces or special charact if have then return false
print(d.isalnum())
# check if stirng has only aphabets then return true
print(d.isalpha())
# check if stirng has olowercase alphabets then return true
print(d.islower())
# check if stirng has not special character like \n oothers then return true
print(d.isprintable())
# check if stirng has white spces then return true
print(d.isspace())
# check if stirng has each word capital then return true
print(d.istitle())
# check if stirng has uppercase alphabets then return true
print(d.isupper())
# give boolean result check that given string starts with specific word or not
print(d.startswith("console"))
# we can give specific perid to check this
print(d.startswith("to", 8, 10))
# convert uppercase to lowercase and lowercase to uppercase
print(d.swapcase())
# convert string to title capital each alphabet of word
print(d.title())
print(d.reversed())