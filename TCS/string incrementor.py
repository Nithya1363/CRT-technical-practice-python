def increment_string(s):
    if s[-1].isdigit():
        num_part = ''
        for char in reversed(s):
            if char.isdigit():
                num_part = char + num_part
            else:
                break
        incremented_num = str(int(num_part) + 1).zfill(len(num_part))
        return s[:-len(num_part)] + incremented_num
    else:
        return s + '1'

user_input = input("Enter a string: ")
result = increment_string(user_input)
print(result)
