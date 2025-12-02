test_txt = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

final_txt = """redacted due to AoC rules : )
"""

txt = final_txt.split(",")


def part_1(txt) -> int:
    res = 0
    for ranges in txt:
        lower, upper = ranges.split("-")
        lower = int(lower)
        upper = int(upper)
        
        for num in range(lower, upper + 1):
            num_str = str(num)
            l = len(num_str)
            if l % (l/2) != 0:
                continue
            divider = int(l / 2)
            if num_str[divider:] == num_str[:divider]:
                res += num
    return res
                        
def part_2(txt) -> int:
    res = 0
    for ranges in txt:
        lower, upper = ranges.split("-")
        lower = int(lower)
        upper = int(upper)
        for num in range(lower, upper + 1):
            s = str(num)
            L = len(s)

            for size in range(1, L):
                if L % size != 0:
                    continue

                parts = [s[i:i+size] for i in range(0, L, size)]

                if len(set(parts)) == 1:
                    res += num
                    break 
    return res
                    
print("part 1:  ",part_1(txt))
print("part 2:  ",part_2(txt))

            

