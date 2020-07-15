def string_split(input):
    delims = ',.!?|;:-+'
    for i in delims:
        input = input.replace(i, '')
    result = input.split(" ")
    return result
string_example = "This is an example string."
print(string_example)

print(string_split(string_example))
