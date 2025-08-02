class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is sweet".format(self.color, self.flavor)

golden = Apple("yellow", "soft")
print(golden.color)
print(golden)