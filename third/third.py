with open("input.txt", "r") as f:
    data = f.readlines()

res1 = 0
res2 = 0

def part1(digits):
    global res1
    n = len(digits)
    if n == 0:
        return
    elif n == 1:
        res1 += digits[0]
        return
    elif n == 2:
        res1 += digits[0] * 10 + digits[1]
        return
    else:
        curr = digits[0] * 10 + digits[1]
        for digit in digits[2:]:
            curr = max(curr, digit + curr % 10 * 10, digit + curr // 10 * 10)
        res1 += curr


def part2(digits):
    global res2
    curr = 0
    n = len(digits)
    if n < 12:
        return
    elif n == 12:
        return int("".join([str(n) for n in digits]))
    else:
        for i in range(11, -1, -1):
            max_digit = max(digits[: (len(digits) - i)])
            max_idx = digits.index(max_digit)
            digits = digits[max_idx + 1 :]
            curr = curr * 10 + max_digit
        res2 += curr


for line in data:
    line = line.strip()
    if not line:
        continue
    digits = [int(digit) for digit in str(line)]
    part1(digits)
    part2(digits)

print(f"Part 1: {res1}")
print(f"Part 2: {res2}")
