print(
    "========================Ternary Operators or Conditional Expressions========================"
)

a = 22
b = 22
c = 22
d = 22
print("A") if a > b and a > c and a > d else print(
    "B"
) if b > a and b > c and b > d else print("C") if c > a and c > b and c > d else print(
    "D"
) if d > a and d > c and d > b else print(
    "All Conditions are True."
)
