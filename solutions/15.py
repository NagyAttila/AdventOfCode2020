input_ = "15,5,1,4,7,0"
# input_ = "3,1,2"

def solve(xs, bound):
    xs = map(int, input_.split(','))
    m = dict()
    i = 1
    for x in xs:
        m[x] = (i, i)
        i += 1

    while i <= bound:
        [p1, p2] = m[x]
        x = p1 - p2
        if x in m:
            [p1, p2] = m[x]
            p2 = p1
            p1 = i
            m[x] = (p1, p2)
        else:
            m[x] = (i, i)
        i += 1

    return x

print("Part #1: ", solve(input_, 2020))
print("Part #1: ", solve(input_, 30000000))
