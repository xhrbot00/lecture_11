import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(file_path, "r") as json_file:
        dict = json.load(json_file)

    seq = dict[field]
    return seq


def linear_search(seq, num):
    """

    :param seq:
    :param num:
    :return:
    """
    indices = []
    count = 0
    for position, i in enumerate(seq):
        if i == num:
            indices.append(position)
            count += 1

    dict = {
        "positions": indices,
        "count": count
    }

    return dict


def patter_search(sequence, pattern):
    """

    :param sequence:
    :param pattern:
    :return:
    """

    pattern_size = len(pattern)
    positions = set()

    left_idx = 0
    right_idx = pattern_size

    while right_idx < len(sequence):
        for idx_p in range(pattern_size):
            if pattern[idx_p] != sequence[left_idx + idx_p]:
                break
        else:
            positions.add(left_idx + pattern_size // 2)

        left_idx += 1
        right_idx += 1

    # for idx_s, i in enumerate(sequence):
    #     for idx_p in range(pattern_size):
    #         if pattern[idx_p] != sequence[idx_s + idx_p]:
    #             break
    #     else:
    #         positions.add(idx_s + pattern_size // 2)

    return positions


def binary_search(seq, number):
    left_end = 0
    right_end = len(seq) - 1

    while left_end <= right_end:
        middle = (left_end + right_end) // 2

        if number < seq[middle]:
            right_end = middle - 1
        elif number > seq[middle]:
            left_end = middle + 1
        else:
            return middle

    return None


def main():
    #linear search
    file_name = "sequential.json"
    seq = read_data(file_name, "unordered_numbers")
    print(seq)
    res = linear_search(seq, num=0)
    print(res)

    #pattern search
    sequnce = read_data(file_name, "dna_sequence")
    res_2 = patter_search(sequnce, "ATA")
    print(res_2)

    #binary
    seq = read_data(file_name, "ordered_numbers")
    res_3 = binary_search(seq, number=13)
    print(res_3)


if __name__ == '__main__':
    main()