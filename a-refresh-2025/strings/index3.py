# modifying strings
msg = "A kong string with a silly typo"
new_msg = msg[0:2] + "L" + msg[3:]
# print(new_msg)

# pet = "Cats & Dogs"
# pet.index("&")
# pet.index("Dogs")
# # check if it's there
# "bull" in pet

# Exercise..................

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_domain = email[:index] + "@" + new_domain
        return new_domain
    return email

# replace_domain("saalu@example.com", "example.com", "africa.org")

" ".join(["This", "is", "good"])
"...".join(["This", "is", "good"])

"Check this example".split()