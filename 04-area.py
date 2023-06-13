# tests passed! complete! (without validating arguments)
# after adding validation, some asserts fail, but that's correct

def area(length, width):
    if length > 0 and width > 0:
        return length * width
    else:
        print("Invalid argument.")

def perimeter(length, width):
    if length > 0 and width > 0:
        return 2 * length + 2 * width
    else:
        print("Invalid argument.")

def volume(length, width, height):
    if length > 0 and width > 0:
        return length * width * height
    else:
        print("Invalid argument.")

def surfaceArea(length, width, height):
    if length > 0 and width > 0:
        return (2 * length * width) + (2 * length * height) + (2 * width * \
                                                               height)
    else:
        print("Invalid argument.")

def surfaceArea_alt(length, width, height):
    if length > 0 and width > 0:
        return 2 * area(length, width) + 2 * area(length, height) \
        + 2 *  area(height, width)
    else:
        print("Invalid argument.")


assert area(10, 10) == 100

assert area(0, 9999) == 0

assert area(5, 8) == 40

assert perimeter(10, 10) == 40

assert perimeter(0, 9999) == 19998

assert perimeter(5, 8) == 26

assert volume(10, 10, 10) == 1000

assert volume(9999, 0, 9999) == 0

assert volume(5, 8, 10) == 400

assert surfaceArea(10, 10, 10) == 600

assert surfaceArea(9999, 0, 9999) == 199960002

assert surfaceArea(5, 8, 10) == 340

assert surfaceArea_alt(10, 10, 10) == 600

assert surfaceArea_alt(9999, 0, 9999) == 199960002

assert surfaceArea_alt(5, 8, 10) == 340