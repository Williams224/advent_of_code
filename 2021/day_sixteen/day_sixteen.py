import math

HEX_DICT = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex_to_bin(hex_string):
    binary_list = list(map(lambda x: HEX_DICT[x], list(hex_string)))
    full_binary = "".join(binary_list)
    return list(full_binary)


def strings_to_bin(string_list):
    string_list_r = list(reversed(string_list))
    ret_val = 0
    for i in range(0, len(string_list_r)):
        ret_val += int(string_list_r[i]) * int(math.pow(2, i))

    return ret_val


def split_binary(start_pos, binary_list):
    packet_version = binary_list[start_pos : start_pos + 3]
    type_id = binary_list[start_pos + 3 : start_pos + 6]
    if type_id == ["1", "0", "0"]:
        start_values = start_pos + 6
        read = True
        curr_start = start_values
        curr_end = curr_start + 5
        while read:
            val = binary_list[curr_start:curr_end]
            if val[0] == 1:
                read = True
            else:
                read = False

        return binary_list[start_pos:curr_end], curr_end

    else:
        length_type_id = binary_list[start_pos + 6]
        if length_type_id == "0":
            length_number_bin = list(
                reversed(binary_list[start_pos + 7 : start_pos + 7 + 15])
            )
            length_number = 0
            for i in range(0, len(length_number_bin)):
                length_number += int(length_number_bin[i]) * int(math.pow(2, i))

            end_pos = start_pos + 7 + 15 + length_number
            return binary_list[start_pos:end_pos], end_pos
        else:
            length_number_bin = list(
                reversed(binary_list[start_pos + 7 : start_pos + 7 + 15])
            )
            n_sub_packets = 0
            for i in range(0, len(length_number_bin)):
                n_sub_packets += int(length_number_bin[i]) * int(math.pow(2, i))

            end_pos = start_pos + 7 + 11 + (n_sub_packets * 11)
            return binary_list[start_pos:end_pos], end_pos


if __name__ == "__main__":
    with open("day_sixteen/input.txt") as f:
        line = f.readlines()

    hex_list = list(line[0])

    binary_list = list(map(lambda x: HEX_DICT[x], hex_list))
    full_binary = "".join(binary_list)

    first_list, end_pos = split_binary(0, list(full_binary))
    print(len(full_binary))
    print(first_list)
