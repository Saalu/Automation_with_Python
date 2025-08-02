file_counts = {"jpg":10, "txt":14, "png":12, "csv": 3, "py":23}
# print(file_counts.values())
# print(file_counts.keys())
# print(file_counts.items())


# for ext, amt in file_counts.items():
#     print("There are {} files with the .{} extension".format(amt, ext))


    # task
def count_letters(txt):
    result = {}
    for letter in txt:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

count_letters("billion")