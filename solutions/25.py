def transform(loop_size, subject_number):
    value = 1
    for _ in range(1,loop_size+1):
        value *= subject_number
        value %= 20201227
    return value

def get_loop_sizes(card_subject_number_of_7, door_subject_number_of_7):
    value = 1
    i = 1
    card_found = False
    door_found = False
    subject_number = 7
    while not card_found or not door_found:
        value *= subject_number
        value %= 20201227
        if value == card_subject_number_of_7:
            card_found = i
        if value == door_subject_number_of_7:
            door_found = i
        i += 1
    return card_found, door_found

def solve_1(card_public_key, door_public_key):
    card_loop_size, door_loop_size = get_loop_sizes(card_public_key, door_public_key)
    return transform(card_loop_size, door_public_key)

print("Example:", solve_1(5764801, 17807724))
print("Part #1:", solve_1(8458505, 16050997))
