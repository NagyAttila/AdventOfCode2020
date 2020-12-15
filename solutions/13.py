input_ = """1006605
19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,883,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,797,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29"""

# input_ = """939
# 7,13,x,x,59,x,31,19"""

### Part 1 ###
[departure, buses] = input_.split('\n')
departure = int(departure)
buses = [ int(x) for x in buses.split(',') if x != 'x' ]

solution = 0
closest = max(buses)
for bus in buses:
    distance = bus - departure%bus
    if distance < closest:
        closest = distance
        solution = bus

solution *= closest
print("Part #1: ", solution)


### Part 2 ###
[departure, buses] = input_.split('\n')
departure = int(departure)
buses = [ (int(x), i) for i,x in enumerate(buses.split(',')) if x != 'x' ]

### Slow solution
# from itertools import dropwhile, count
# step = 1
# solution = next(dropwhile(lambda x : not all(list(map(lambda y : (x+y[1])%y[0] == 0, buses))), count(0,step)))

### Fast solution
from itertools import dropwhile, count
t = 0
step = 1
for bus, off in buses:
    t = next(dropwhile(lambda t: (t+off)%bus, count(t, step)))
    step *= bus
solution = t

print("Part #2: ", solution)

