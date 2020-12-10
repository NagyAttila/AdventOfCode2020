input_ = """67
118
90
41
105
24
137
129
124
15
59
91
94
60
108
63
112
48
62
125
68
126
131
4
1
44
77
115
75
89
7
3
82
28
97
130
104
54
40
80
76
19
136
31
98
110
133
84
2
51
18
70
12
120
47
66
27
39
109
61
34
121
38
96
30
83
69
13
81
37
119
55
20
87
95
29
88
111
45
46
14
11
8
74
101
73
56
132
23"""

# input_ = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4"""

# input_ = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""

xs = list(map(int, input_.split('\n')))

xs = [0] + sorted(xs) + [max(xs)+3]
ds = list()
c1 = 0
c3 = 0
for i in range(1,len(xs)):
    if xs[i] - xs[i-1] == 1:
        c1 += 1
    elif xs[i] - xs[i-1] == 3:
        c3 += 1

solution = c1 * c3
print("Part #1: ", solution)

### Part 2: Slow Solution ###

# def fn(xs_):
#     if len(xs_) < 2 :
#         return 1

#     acc = 0
#     for i in [1,2,3]:
#         if   len(xs_) > 1 and xs_[1] - xs_[0] == i :
#             acc += fn(xs_[1:])
#         elif len(xs_) > 2 and xs_[2] - xs_[0] == i :
#             acc += fn(xs_[2:])
#         elif len(xs_) > 3 and xs_[3] - xs_[0] == i :
#             acc += fn(xs_[3:])
#     return acc

# xs = list(map(int, input_.split('\n')))
# xs = [0] + sorted(xs) + [max(xs)+3]
# solution = fn(xs)

### Part 2: Fast Solution ###
from numpy import diff as diff

ni = 0
solution = 1
dxs = diff(xs)
for i in range(len(dxs)):
    if dxs[i] == 1:
        ni += 1
    elif dxs[i] == 3:
        if ni == 2: solution *= 2
        elif ni == 3: solution *= 4
        elif ni == 4: solution *= 7
        ni = 0

print("Part #2: ", solution)
