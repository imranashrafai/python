print("======================== f-strings ========================")
# use to print values of variable

nameProduct = "Shoes E40"
priceProduct = 219.9810
Consumer = "Imran Ashraf"
date = "9-3-2023"
print(f"{Consumer} bought {nameProduct} on {date} in {priceProduct:.2f} dollars!")
print(f"{(2*300)//2.2}")
print(type(f"{(2*300)//2.2}"))
# If i want to show esitist variable name then
print(
    f"{{Consumer}} bought {{nameProduct}} on {{date}} in {{priceProduct:.2f}} dollars!"
)
