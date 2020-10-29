fullname = ('Saalu', 'I', 'Wendela')
print(type(fullname))

def convert_seconds(sec):
    hours = sec // 3600
    minutes = (sec - hours * 3600 ) // 60
    remaining_sec = sec - hours * 3600 - minutes * 60
    return hours, minutes, remaining_sec

result = convert_seconds(5000)
print(result)
hours, minutes, sec = result
print(hours,minutes, sec)