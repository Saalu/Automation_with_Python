animals = ['lion', 'monkey', 'dog']
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {:2f}".format(chars, chars/len(animals)))

winners = ['Adnan', 'Seedof', 'Reese']

for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


def full_emails(people):
    result =[]
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return  result
print(full_emails([("alex@yahoo.com", "Alex Diego"), ("sarah@gmai.com", 'Sarah Banks')]))

# next lesson  ==========
multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

multiples = [x*7 for x in range(1,12)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Java"]
lengths = [len(language) for language in languages]
print(lengths)

z=[x for x in range(0,101) if x % 3 == 0]
print(z)