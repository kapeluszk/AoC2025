test = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

impt = """
redacted
"""

ranges, checks = impt.split("\n\n")

ranges_clean = ranges.split("\n")
checks_clean = checks.split("\n")

def part_1() -> int:
    range_list = []

    for rang in ranges_clean:
        lower,upper = rang.split("-")
        range_list.append([int(lower),int(upper)])

    counter = 0
    for check in checks_clean:
        for rng in range_list:
            if check != "":
                if rng[0] <= int(check) <= rng[1]:
                    counter += 1
                    break
    return counter

def part_2() -> int:
    counter = 0
    range_list = []
    for rang in ranges_clean:
        lower,upper = rang.split("-")
        range_list.append([int(lower),int(upper)])

    range_list.sort(key=lambda x: x[0])

    merged = [range_list[0]]
    for current in range_list[1:]:
        last = merged[-1]
        if current[0] <= last[1]+1:
            last[1] = max(last[1],current[1])
        else:
            merged.append(current)
    
    for rng in merged:
        counter += rng[1] - rng[0] + 1
    return counter

print("part 1: ", part_1())
print("part 2: ", part_2())





