#  Code to change old_domain  to new_domain

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain('abu@rascal.com', 'rascal.com', 'gmail.com'))