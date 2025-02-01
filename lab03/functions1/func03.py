
def solve(numlegs, numheads):
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    return x, y
numheads = 35
numlegs = 94
x, y = solve(numlegs, numheads)
print(f"chickens: {x}, rabbits: {y}")
