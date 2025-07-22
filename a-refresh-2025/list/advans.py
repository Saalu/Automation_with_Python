# task
animals = ["Lion", "Zebra", "Monkey", "Dolphin"]
chars = 0
for animal in animals:
    chars += len(animals)
# print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

# enumerate func
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# solve problem -- NOT WORKING CHECK LATER
def full_emails(people):
    result = []
    for email, name in person:
        result.append("{} <{}>".format(name,email))
    return result

# print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

multiples = []
for x in range(1,11):
    multiples.append(x*7)

# print(multiples)

langs = ["Python", "Ruby", "Javascript", "Go", "Java"]
lengths = [len(langs) for lang in langs]
print(lengths)






