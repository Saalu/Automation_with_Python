
# nums = [ 2, 4, 6]
# msg = "Numbers: {0} {2} {1}".format(nums[0], nums[2], nums[1])
# print(msg)

# a ="{x} <{y}>".format(x=5, y=12.5604)
# print(a)

name = 'Saalu'
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celcius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>1.2f} C".format(x, to_celcius(x)))