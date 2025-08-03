def rectangle_maker(v):
    x = 0
    y = 0
    for point in v:
        x ^= point[0]
        y ^= point[1]
    return [x,y]

v = [[1, 4], [3, 4], [3, 10]]
print(rectangle_maker(v))