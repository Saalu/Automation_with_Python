name = "Saalu"
number = len(name) * 5
print("Hello {}, your lucky number is {}".format(name, number))
print("your lucky {number}, how do you feel {name}".format(name=name, number=len(name) *3))

price = 7.5
with_tax = price * 1.09
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))