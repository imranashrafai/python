print("========================Enumerate Function========================")


marks = [78, 12, 43, 2, 42, 33, 11, 89, 56]

for index, mark in enumerate(marks):
    if index == 7:
        print(f"Excelent! Imran. You got {mark} marks.", end=" ")
    print(mark, end=" ")
print()
# it will start index from 1 instwad of 0
for index, mark in enumerate(marks, start=7):
    if index == 15:
        print(f"Poor! Imran. You got {mark} marks.", end=" ")
    print(mark, end=" ")