file_counts = {"jpg":10, "txt":14, "py":34, "csv":25}
for extension in file_counts:
    print(extension)

# to get keys and values from dictionary
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extention".format(amount, ext))

# to get keys and values from dictionary
print(file_counts.keys())


# to get keys and values from dictionary
print(file_counts.values())