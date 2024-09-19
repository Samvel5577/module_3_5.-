def get_multiplied_digits(number):
    str_number = str(number)

    first = int(str_number[0])

    if len(str_number) > 1:

        if first == 0:
            return get_multiplied_digits(int(str_number[1:]))
        else:

            return first * get_multiplied_digits(int(str_number[1:]))
    else:

        return first if first != 0 else 1


result = get_multiplied_digits(240)
print(result)
