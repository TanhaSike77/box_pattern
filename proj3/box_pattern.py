def patterns(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character")
    if width <= 2:
        raise Exception("Width must be greater than 2")
    if height <= 2:
        raise Exception("Height must be greater than 2")

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)
    print(symbol * width)

try:
    patterns("#", 10, 10)
    patterns("$", 3, 5)
    patterns("%", 1, 4)
    patterns("&&", 5, 3)

except Exception as e:
    print("Error:", str(e))

try:
    patterns("&&", 5, 3)
except Exception as e:
    print("Error:", str(e))
