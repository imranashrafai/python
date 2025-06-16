print("========================Kon Bny Ga Crore Patti========================")

questions = [
    [
        "Who is the current Interim PM of Pakistan ?",
        "Imran Khan",
        "Shehbaz Sharif",
        "Anwar Ul Huq",
        "Hamza Shehbaz",
        3,
    ],
    [
        "Who is the current Chairman of SUPARCO ?",
        "Hamza Shehbaz",
        "Ahmed Bilal",
        "Ashraf Ghani",
        "Mohsin Naqvi",
        2,
    ],
    [
        "Who is the current COAS of Pakistan ?",
        "Gen Qamar bajwa",
        "Gen Asif Nadeem",
        "Gen Babar Anjum",
        "Gen Hafiz Asim Munir",
        4,
    ],
    [
        "Inflation rate in the year of 2023 is: ",
        "12%",
        "-10%",
        "27.7%",
        "1.32%",
        3,
    ],
    [
        "People who are always ready to fight for their country: ",
        "Pakistani",
        "Indian",
        "American",
        "Saudi",
        1,
    ],
    [
        "How much Pakistani ready to sacrifice their lives for Pakistan? ",
        "80%",
        "89%",
        "11%",
        "59%",
        2,
    ],
    [
        "How many IPPS in Pakistan ?",
        10,
        32,
        50,
        75,
        4,
    ],
]
level = [1000, 5000, 10000, 40000, 100000, 3000000, 10000000]
money = 0
try:
    for i in range(0, len(questions)):
        question = questions[i]
        print(f"Question for Rs. {level[i]}")
        print(question[0])
        print(f"a. {question[1]}               b. {question[2]}")
        print(f"c. {question[3]}               d. {question[4]}")
        reply = int(input("Enter correct option (1-4) or  0 for Quit Game: "))

        if reply == 0:
            break
        if reply == question[-1]:
            print(f"Good Job! you choosen correct option and you won Rs. {level[i]}")
            if i == 3:
                money = 100000
            elif i == 6:
                money = 10000000
        else:
            print("You choosen wrong option! ")
            break

except ValueError:
    print("Input Error Occured!")
finally:
    print(f"Money to take home is Rs. {money}")
