print("========================Emulate do-while loop========================")

# do-while loop always emulate by Infinte While loop
i = 0
# behaving as do
while True:
    print(i, end=" ")
    i = i + 1
    # behaving as while like=> while(1%100==0)
    if i % 10 == 0:
        break
