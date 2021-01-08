input_ = "247819356"
input_ = "389125467"
from time import time, sleep



def solve_1(STEPS, data):
    def remove(i, n, cs):
        left = cs[:i]
        right = cs[i+n:]
        return left + right

    def add(i, ps, cs):
        return cs[:i] + ps + cs[i:]

    def shift_right(xs, i):
        if i == 0:
            return xs
        return [xs[-1]] + shift_right(xs[:-1],i-1)

    def shift_left(xs, i):
        if i == 0:
            return xs
        return shift_left(xs[1:],i-1) + [xs[0]]

    cups = [int(x) for x in data]
    N = len(cups)
    i = 0
    for k in range(STEPS):

        pickup = []
        left = cups.copy()
        for j in range(1,4):
            pickup.append(cups[j])
        cups = remove(1,3,cups)

        dest = cups[0] - 1
        while not dest in cups:
            if dest == 0:
                dest += N
            else:
                dest -= 1
        dest_i = cups.index(dest) + 1

        cups = add(dest_i,pickup,cups)
        cups = shift_left(cups, 1)
        i += 1

    while cups[0] != 1:
        cups = shift_left(cups,1)
    return ''.join([str(c) for c in cups[1:]])

def solve_2(STEPS, cups, fn):
    def dec(v):
        if v == 1:
            return N
        return v - 1

    def printCups(start):
        p = start
        for _ in range(cups.n):
            print(p.value, end=' ')
            p = p.next
        print('')

    # Create Dest->Elem map
    i = cups.next
    dest2elem = {i.prev.value : i.prev}
    while i != cups:
        dest2elem[i.value] = i
        i = i.next

    N = cups.n
    i = cups
    for k in range(STEPS):
        # print(k,end='\r')

        p1 = i.next
        p2 = p1.next
        p3 = p2.next

        dest_value = dec(i.value)
        while dest_value in [p1.value, p2.value, p3.value]:
            dest_value = dec(dest_value)

        dest = dest2elem[dest_value]

        i.next = p3.next
        i.next.prev = i

        dest.next.prev = p3
        p3.next = dest.next
        dest.next = p1
        p1.prev = dest

        i = i.next

    # printCups(i)
    return fn(dest2elem[1])

t = time()
print("Part #1:", solve_1(100, input_), '(', time()-t, ')')

class LinkedList(object):
    n = 0
    def __init__(self, p, n, v):
        super(LinkedList, self).__init__()
        self.prev = p
        self.next = n
        self.value = v
        LinkedList.n += 1

def get_from_1(linked_list):
    linked_list = linked_list.next
    xs = ''
    while linked_list.value != 1:
        xs += str(linked_list.value)
        linked_list = linked_list.next
    return xs

# Part 1, again
# Create Linked List
values = [int(i) for i in input_]
input_part1 = LinkedList(None, None, values[0])
prev = input_part1
for i in values[1:]:
    new = LinkedList(prev, None, i)
    prev.next = new
    prev = new
prev.next = input_part1
input_part1.prev = prev

# Solve
t = time()
print("Part #1b:", solve_2(100, input_part1, get_from_1), '(',time()-t,')')

# Part 2
# Create Linked List
LinkedList.n = 0
values = [int(i) for i in input_] + list(range(10,1000001))
input_part2 = LinkedList(None, None, values[0])
prev = input_part2
for i in values[1:]:
    new = LinkedList(prev, None, i)
    prev.next = new
    prev = new
prev.next = input_part2
input_part2.prev = prev

# Solve
t = time()
print("Part #2:", solve_2(10000001, input_part2, lambda xs : xs.next.value * xs.next.next.value), '(',time()-t,')')
