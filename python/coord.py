def coord(x, y):
    return x + y * 1j

def left(c):
    return c * 1j

def right(c):
    return c * -1j

def reverse(c):
    return -c

def print_grid_dict(mat, mapper=str):
    x_min = int(min(c.real for c in mat))
    x_max = int(max(c.real for c in mat))
    y_min = int(min(c.imag for c in mat))
    y_max = int(max(c.imag for c in mat))
    for y in range(y_max, y_min-1,-1):
        print("".join(map(mapper, [mat[coord(x, y)]for x in range(x_min, x_max+1)])))
