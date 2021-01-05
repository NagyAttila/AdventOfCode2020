input_ = """Player 1:
45
10
43
46
25
36
16
38
30
15
26
34
9
2
44
1
4
40
5
24
49
3
41
19
13

Player 2:
28
50
37
20
6
42
32
47
39
22
14
7
21
17
27
8
48
11
23
12
18
35
29
33
31"""

# input_ = """Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10"""

# input_ = """Player 1:
# 43
# 19

# Player 2:
# 2
# 29
# 14"""

import functools

player_1 = input_.split('\n\n')[0].split(':\n')[1]
player_2 = input_.split('\n\n')[1].split(':\n')[1]

player_1 = [ int(x) for x in player_1.splitlines() ]
player_2 = [ int(x) for x in player_2.splitlines() ]

while len(player_1) and len(player_2):
    if player_1[0] > player_2[0]:
        player_1.append(player_1[0])
        player_1.append(player_2[0])
        player_1 = player_1[1:]
        player_2 = player_2[1:]
    else:
        player_2.append(player_2[0])
        player_2.append(player_1[0])
        player_1 = player_1[1:]
        player_2 = player_2[1:]

if player_1:
    solution = functools.reduce(lambda b,a: a[0]*a[1]+b, enumerate(reversed(player_1),1), 0)
else:
    solution = functools.reduce(lambda b,a: a[0]*a[1]+b, enumerate(reversed(player_2),1), 0)
print("Part #1", solution)

### Part 2 ###
def solve(p1, p2):
    def p1_wins(p1_, p2_):
        p1_.append(p1_[0])
        p1_.append(p2_[0])
        p1_ = p1_[1:]
        p2_ = p2_[1:]
        return p1_, p2_

    def p2_wins(p1_, p2_):
        p2_.append(p2_[0])
        p2_.append(p1_[0])
        p1_ = p1_[1:]
        p2_ = p2_[1:]
        return p1_, p2_

    prev = []

    while len(p1) and len(p2):

        if (p1,p2) in prev:
            return True, False
        prev.append((p1.copy(),p2.copy()))

        if p1[0] < len(p1) and p2[0] < len(p2):
            p1_,_ = solve(p1[1:p1[0]+1], p2[1:p2[0]+1])
            if p1_:
                p1, p2 = p1_wins(p1,p2)
            else:
                p1, p2 = p2_wins(p1,p2)
        elif p1[0] > p2[0]:
            p1, p2 = p1_wins(p1,p2)
        else:
            p1, p2 = p2_wins(p1,p2)
    return p1 , p2

player_1 = input_.split('\n\n')[0].split(':\n')[1]
player_2 = input_.split('\n\n')[1].split(':\n')[1]

player_1 = [ int(x) for x in player_1.splitlines() ]
player_2 = [ int(x) for x in player_2.splitlines() ]

player_1, player_2 = solve(player_1, player_2)

if player_1:
    solution = functools.reduce(lambda b,a: a[0]*a[1]+b, enumerate(reversed(player_1),1), 0)
else:
    solution = functools.reduce(lambda b,a: a[0]*a[1]+b, enumerate(reversed(player_2),1), 0)
print("Part #2", solution)
