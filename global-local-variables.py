print("========================Global & Local Variables========================")
# local are defined in functions and they are destroyed after running function

value = 19
result = 0


def addition():
    localValue = 23
    # for updating value of global variables then use global keyword
    global result
    global value
    value = 34
    result = value + localValue
    print("Addition of local and global Variables is: ", result)


addition()
print("Global Value is: ", result)
