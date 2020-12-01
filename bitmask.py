# Author: Edmund Aduse Poku
# Solve the subset sum problem using bitmasks


# (1 << i) shifts 1 to the index i (wanted position)
def set_bit(bitmask, i):
    # | (logical OR) allows setting value at index i to 1
    # since the value of bitmask at index i, regardless of its value, is "ORED" with 1
    return bitmask | (1 << i)


def unset_bit(bitmask, i):
    # ~ (logical NOT) flips the value at every index of (1 << i) to the opposite value
    # & (logical AND) here sets the value at index i to 0 and leaves those at every other
    # position unchanged since the former and the latter are "ANDED" with 0 and 1, respectively
    return bitmask & ~(1 << i)


def is_bit_set(bitmask, i):
    # & (logical AND) here leaves the value at index i unchanged but sets that at every other
    # index to 0 since the former and the latter are "ANDED" with 1 and 0, respectively
    # the returned value is a positive number (ie true) if the value at index i is 1
    # and false, otherwise (that is if it is 0)
    return bitmask & (1 << i)


# Count how many subsets have sum of elements greater
# than or equal to a given value

# Using Bitmask
# Runtime O(2^n times n)
def subset_sum(main_set, size, value):
    # label the elements in main_set with indices using a map
    # so that it is easier to operate on them using a bitmask
    # order of the indices doesn't matter for a set
    element_index = 0
    element_index_mapping = {}
    for element in main_set:  # Runs in O(n) time
        element_index_mapping[element_index] = element
        element_index += 1

    num_subsets = 0  # number of subsets that whose sum
    for set_bitmask in range(2**size):  # O(2^n)
        # Each subset is a number that can be thought of as a bitmask, with
        # each index indicating the position of values in the original set
        # (or binary num) represented by its corresponding decimal num

        element_sum = 0  # sum the values represented in this particular bitmask (or subset)

        # Go through the bits for each bitmask
        # And find the bits that are represented
        # And sum the values represented by those bits
        for index in range(size):  # Runs in O(n) time
            if is_bit_set(set_bitmask, index):
                element_sum += element_index_mapping[index]

        if element_sum == value:
            # == is used here as we want the subset sum to be exactly equal to the target
            # >= can be used if the subset sum has to be at least the target
            num_subsets += 1

    return num_subsets


# Bit shift
# Shift 0
i = 4  # shift 1 to the left by 0 (should give 0b00000 = 0)
print("shift 0 to the left by 0, ans = ", 0 << i)

# Shift 1
i = 0  # shift 1 to the left by 0 (should give 0b1 = 1)
print("shift 1 to the left by 0, ans = ", 1 << i)
i = 1  # shift 1 to the left by 1 (should give 0b10 = 2)
print("shift 1 to the left by 1, ans = ", 1 << i)
i = 4  # shift 1 to the left by 4 (should give 0b10000 = 16)
print("shift 1 to the left by 4, ans = ", 1 << i)

# Shift 5
i = 0  # shift 5 (=0b101) to the left by 0 (should give 0b101 = 5)
print("shift 5 to the left by 0, ans = ", 5 << i)
i = 1  # shift 5 (=0b101) to the left by 1 (should give 0b1010 = 10)
print("shift 5 to the left by 1, ans = ", 5 << i)
i = 4  # shift 5 (=0b101) to the left by 4 (should give 0b1010000 = 80)
print("shift 5 to the left by 4, ans = ", 5 << i)

print("subset sum", subset_sum({2, 3, 5}, 3, 5))