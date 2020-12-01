# Suppose you have one-dimensional storage segments, like
# 5, 3, 4, 2, 3,
# where the numbers are the height of storage
# You have some objects and you want to fit them to storage. Say your objects are
# 5, 1, 3, 4, 3,
# Requirement:
# a) Tunnel restriction: The objects are pushed from left to right to segments.
# b) No stacking. One object per storage.
# Goal: fit as many objects as possible to the storage area and find the maximum number of objects you can fit.
#  s: 3, 4, 2, 3
#  o: 5, 1, 3, 4, 3,
#  return 3


def fit_max_objects(storage, objects):
    count = 0

    # observation: if the objects are sorted, then small sized objects can be pushed
    # first as those have a better chance of going through constraints than bigger
    # sized objects. Precisely put, whatever constraint an object cannot go through,
    # a number greater than it will not stand a chance of going through either.
    # More precisely put, if any object stand a chance of filling memories at the
    # far right of the one-dimensional storage segments, then they are small sized
    # objects. The algorithm thus fill those first and keep track of the last memory
    # segment used, which is affected by the last storage segment that a relatively
    # small sized object could go through/fit
    sorted_objects = sorted(objects)

    last_i = len(storage)  # last memory segment used
    for obj in sorted_objects:  # try fitting every object
        i = 0

        # make sure that the object can go through (or fit) the current storage segment
        # and that it is not stored in or past the last memory segment used
        while i < last_i and obj <= storage[i]:
            i += 1
        if i > 0:
            count += 1
        last_i = i - 1

    return count


# Test
print(fit_max_objects([3, 4, 2, 3], [5, 1, 3, 4, 3]))
