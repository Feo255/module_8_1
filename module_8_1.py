

def add_everything_up(a, b):
    try:

        result = a + b
        return result

    except(TypeError):
        a_ = str(a)
        b_ = str(b)
        summ = a_ +b_
        return summ


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))