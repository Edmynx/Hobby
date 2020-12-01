# Form subsets in an intelligent manner
# Created by Edmund Aduse Poku for the fun of it
# Called (A-Poku) Three Pointer
# Three-pointer is a method under construction


def three_pointer(list):
    subsets = [{}]  # add the empty list (special case)
    for i in range(len(list)):  # i is pointer 1
        subsets.append({list[i]})  # add set of first pointer to the list of sets
        for j in range(i+1, len(list)):  # pointer 2
            subsets.append({list[i], list[j]})
            k = len(list) - 1  # pointer 3
            while k != j:
                subsets.append({list[i], list[j], list[k]})
                if j < k - 1:
                    subsets.append(set(list[i:k+1]))
                k -= 1
    print(subsets)
    return subsets


def three_pointer_derivative(s):
    subsets = []
    for element in s:
        # The for-loop is skipped for the first element in s
        # because subsets is empty then. Hence the problem
        # of redundancy is solved, ie 1st element !added twice
        for i in range(len(subsets)):
            subset = set(subsets[i])
            subset.add(element)
            subsets.append(subset)
        subsets.append({element})
    subsets.append({})
    return subsets


def test1(number, let="false"):
    letters = []
    if let and 27 > number:
        letters = (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

    this_list = []
    for i in range(number):
        if len(letters) > 0:
            this_list.append(letters[i])
        else:
            this_list.append(i)
        print("length of set = " + str(len(this_list)), "; number of subsets = " + str(len(three_pointer(this_list))), "\n")


def test2(number):
    this_set = set()
    for i in range(number):
        this_set.add(i)
        print("length of set = " + str(len(this_set)), "; number of subsets = " + str(len(three_pointer_derivative(this_set))))


test1(6)

