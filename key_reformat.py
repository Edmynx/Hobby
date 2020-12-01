# Author: Edmund Aduse Poku
# Given a key, reformat it such that the characters are bundled into
# groups of 3 (except possibly the first one) separated by -


def key_reformat(string, k):
    # allocate space for the formatted text
    # the formatted text can occupy space at most the sum of the length
    # of the original string (assuming no initial separators) and the number of
    # separators used, which is at most the size of (floor(string/k) - 1)
    string_list = [None] * (len(string) + len(string)//k - 1)

    i = len(string) - 1  # start reading from the last character of string
    j = len(string_list) - 1  # start indexing from the end of the list
    group_count = 0  # count the number of characters in the current batch

    while i > -1:

        if group_count == k:
            group_count = 0  # reset group_count for the next batch of characters
            string_list[j] = "-"  # indication for next group to follow
            j -= 1
        print(i)

        if string[i] != "-":
            string_list[j] = (string[i].upper() if string[i].isalpha() else string[i])
            group_count += 1
            j -= 1
        i -= 1
    print(string_list)
    return "".join(string_list[j+1:])  # return a string of the filled in spots


# Some test code
S = "24110r74k"
Sk = 1
print(key_reformat(S, Sk))

S = "2-4110r-7-4k"
Sk = 4
print(key_reformat(S, Sk))

S = "r"
Sk = 1
print(key_reformat(S, Sk))

S = "2-440r7-4k"
Sk = 4
print(key_reformat(S, Sk))

