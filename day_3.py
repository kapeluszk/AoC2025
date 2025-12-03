test = """987654321111111
811111111111119
234234234234278
818181911112111"""

inpt = """redacted
"""

nums = [[int(i) for i in line] for line in inpt.splitlines()]

def find_biggest_n(digits_num, txt):
    res = 0
    for t in txt:
        jooltage = 0
        start = 0
        ln = len(t)
        for digit in range(digits_num -1, -1, -1):
            end = ln - digit
            m = t[start]
            index = start
            for i in range(start + 1, end):
                if t[i] > m:
                    m = t[i]
                    index = i
            jooltage = 10 * jooltage + m
            start = index + 1
        res += jooltage
    return res

print(find_biggest_n(2,nums)) 
print(find_biggest_n(12,nums))
        
            
        
        