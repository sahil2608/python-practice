def areaOfTriangle(a, b, c):
    s = (a + b + c) * .5
    print(s)
    area = (s * (s - a) * (s - b) * (s - c)) ** .5
    return area


print(areaOfTriangle(int(input()), int(input()), int(input())))
