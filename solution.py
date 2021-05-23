def rev_dec(num) -> int:
    """Return the decimal number of the reversed bits of num"""
    rev_num_bits = []
    while num > 0:
        rev_num_bits.append(num % 2)
        num = num // 2

    decimal_rev_bits = rev_num_bits[::-1] # Reverses the list
    rev_decimal = 0

    for ind, bit in enumerate(decimal_rev_bits):
        if bit == 1:
            rev_decimal += 2 ** ind

    return rev_decimal

t = int(input())
nums = []

while t > 0:
    nums.append(int(input()))
    t -= 1

results = map(rev_dec, nums)
print(*results, sep='\n')