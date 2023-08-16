# https://inventwithpython.com/pythongently/exercise6/
# don't use endswith()

def ordinalSuffix(number):
    if number % 10 == 1 and number % 100 != 11:
        return str(number) + "st"
    elif number % 10 == 2 and number % 100 != 12:
        return str(number) + "nd"
    elif number % 10 == 3 and number % 100 != 13:
        return str(number) + "rd"
    else:
        return str(number) + "th"

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'

# print(ordinalSuffix(2))

# for i in range(101):
#     print(ordinalSuffix(i))

# scratchwork
# first, second, third, fouth, fifth, sixth, seventh, eighth, ninth, tenth,
# all the teens end in th, then the 20s all use the same as the single digits,
# then 30th, 40th ...
# so it's all th unless the number ends in 1, 2, or 3, but is not 11, 12, 13
