# Author: Edmund Aduse Poku
# Given the schedules for two people, find available times they can meet if the
# meeting needs to be held for a certain number of minutes


def convert_tstring_to_tfloat(tstring_list):
    for i in range(len(tstring_list)):
        tstring_list[i] = tstring_list[i].split(":")
        tstring_list[i] = float("".join(tstring_list[i][0:-2]).join(".").join(tstring_list[i][-2:]))


def convert_tfloat_to_tstring(tfloat_list):
    for i in range(len(tfloat_list)):
        tfloat_list[i] = str(tfloat_list[i]).split(":")
        tfloat_list[i] = ("".join(tfloat_list[i][0:-2]).join(".").join(tfloat_list[i][-2:]))
    return tfloat_list


def condense(combined_schedule, block_begin, block_end, k):
    # merge the given block [block_begin, block_end] with the current combined
    # schedule block if they overlap or share the same boundary
    if block_begin <= combined_schedule[k][1]:
        combined_schedule[k] = [combined_schedule[k][0], block_end]
    else:
        combined_schedule.append([block_begin, block_end])
        k += 1
    return k


def combine_schedule(schedule1, boundaries1, schedule2, boundaries2):
    # pre-process the given string times to float times
    for block in schedule1:
        convert_tstring_to_tfloat(block)

    for block in schedule2:
        convert_tstring_to_tfloat(block)

    convert_tstring_to_tfloat(boundaries1)
    convert_tstring_to_tfloat(boundaries2)

    combined_boundary_begin = max(boundaries1[0], boundaries2[0])
    combined_boundary_end = min(boundaries1[1], boundaries2[1])

    combined_schedule = [[combined_boundary_begin, combined_boundary_begin]]

    # i, j, and k keep track of the current block in schedule 1,
    # schedule 2, and the combined schedule, respectively
    i = j = k = 0
    while i < len(schedule1) and j < len(schedule2):
        if schedule1[i][1] <= schedule2[j][0]:
            # if the end time for schedule 1's current block occurs before or at the start
            # time for schedule 2's current block (ie if the 2 blocks don't overlap and
            # block 1 comes first), then do one of the following:
            k = condense(combined_schedule, schedule1[i][0], schedule1[i][1], k)
            i += 1  # move on to the next block in schedule 1

        elif schedule1[i][1] <= schedule2[j][1]:
            # if the end time for schedule 1's current block occurs after the start time
            # but before or at the end time for schedule 2's current block, (ie if the 2
            # blocks overlap), then merge them into one block with a start time that's a
            # min of their start times and an end time equal to block's 2 end time
            k = condense(combined_schedule, min(schedule1[i][0], schedule2[j][0]), schedule1[i][1], k)

            if schedule1[i][1] == schedule2[j][1]:
                # if the end time for schedule 1's current block occurs exactly at the end
                # time for schedule 2's current block, then the start time for schedule
                # 1's next block occurs on or after the latter's end time, implying that
                # schedule 2's current block can be safely skipped in the next comparison
                j += 1

            i += 1
        else:
            # otherwise, the end time for schedule 1's current block must occur
            # after the end time for schedule 2's current block, and one of the
            # following 2 cases hold:

            if schedule1[i][0] < schedule2[j][1]:
                # the start time for schedule 1's current block occurs before the end
                # time for schedule 2's current block, implying that the 2 blocks can
                # be merged into one block with a start time that's a min of their
                # start times and an end time equal to block's 1 end time
                k = condense(combined_schedule, min(schedule1[i][0], schedule2[j][0]), schedule1[i][1], k)

            else:
                # the start time for schedule 1's current block occurs after the end
                # time for schedule 2's current block, implying that the 2 blocks
                # have to be added separately to the combined schedule with block 2
                # showing up first in the combined schedule
                combined_schedule.append([schedule2[j][0], schedule2[j][1]])
                combined_schedule.append([schedule2[i][0], schedule2[i][1]])
                k += 2

            # since the end time for schedule 1's current block occurs exactly at the end
            # time for schedule 2's current block, the start time for schedule 1's next
            # block occurs after the latter's end time, implying that schedule 2's current
            # block can be safely skipped in the next comparison
            j += 1

    if i < len(schedule1):
        for block in schedule1[i:]:
            k = condense(combined_schedule, block[0], block[1], k)

    else:
        for block in schedule2[j:]:
            k = condense(combined_schedule, block[0], block[1], k)

    condense(combined_schedule, combined_boundary_end, combined_boundary_end, k)

    return combined_schedule


def find_free_blocks(schedule):
    free_blocks = []
    for i in range(len(schedule) - 1):
        free_blocks.append(convert_tfloat_to_tstring([schedule[i][1], schedule[i+1][0]]))

    return free_blocks


# Test
sched1 = [["8:30", "9:45"], ["9:50", "11:10"], ["12:30", "14:45"], ["15:30", "19:45"]]
sched2 = [["8:53", "9:30"], ["9:35", "10:20"], ["10:30", "13:00"], ["16:30", "17:45"], ["18:30", "20:45"]]
bound1 = ["7:00", "21"]
bound2 = ["8:45", "20"]
meet = 1

comb_schedule = combine_schedule(sched1, bound1, sched2, bound2)
print(comb_schedule)
print(find_free_blocks(comb_schedule))

