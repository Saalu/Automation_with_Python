file_counts = {"jpg":10, "txt":14, "py":34, "csv":25}
print(file_counts)
print(file_counts['txt'])  #accessing value in dictionary

print("py" in file_counts)

file_counts['txt'] = 17

print(file_counts)

del file_counts['csv']
print(file_counts)
