input_txt2 = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

def mysplit(s):
    head = s.strip("0123456789")
    tail = int(s[len(head):])
    return head,tail

dial = 50
zeroes_counter = 0
rotations = 0

instructions = input_txt.split()

for instruction in instructions:
    head,tail = mysplit(instruction)
    tail_mod = tail % 100
    rotations += tail // 100
    start = dial
    
    if head == "L":
        end = (start - tail_mod) % 100

        if tail_mod > start and start != 0:
            rotations += 1
    else:
        end = (start + tail_mod) % 100

        if (start + tail_mod) >= 100 and end != 0:
            rotations += 1

    dial = end
    if dial == 0: zeroes_counter += 1
    
    
print("part 1: ", zeroes_counter)
print("part 2: ", zeroes_counter + rotations)