# solved

# https://inventwithpython.com/pythongently/exercise5/
# asks to print it as on string instead of on separate lines

def fizzBuzz(upTo):
    # i didn't HAVE to use a list, but i didn't feel like rewriting `end=""` in
    # every dang case's print statement, so this seemed faster (to write)...
    # but if you cared about it being faster to execute then yeah don't use a 
    # list or even a result variable, jsut directly print each i, with end=""
    results = []
    for i in range(1, upTo + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return " ".join(results)

print(fizzBuzz(20))