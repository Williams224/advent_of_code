import math


def int_to_snafu(char):
    if char == 2:
        return "2"
    elif char == 1:
        return "1"
    elif char == 0:
        return "0"
    elif char == -1:
        return "-"
    elif char == -2:
        return "="
    else:
        raise ValueError(char)


def SNAFU_to_decimal(SNAFU_val):
    snafu_list = list(reversed(list(SNAFU_val)))
    vals_to_sum = []
    for i in range(0, len(snafu_list)):
        if snafu_list[i] == "=":
            val = -2
        elif snafu_list[i] == "-":
            val = -1
        else:
            val = int(snafu_list[i])
        vals_to_sum.append(math.pow(5, i) * val)

    return sum(vals_to_sum)


def to_base_5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n //= 5
    return s


def decimal_to_SNAFU(val):
    normal_base5 = to_base_5(val)
    if not ("3" in normal_base5 or "4" in normal_base5):
        return normal_base5
    else:
        contains_bad_chars = True
        normal_base_list = [int(c) for c in list(normal_base5)]
        while contains_bad_chars:
            if len(normal_base_list) > 1:
                stop = len(normal_base_list) - 1
            else:
                stop = len(normal_base_list)
            for i in range(0, stop):
                if i == 0:
                    if normal_base_list[i] > 2:
                        normal_base_list.insert(0, 1)
                        normal_base_list[i + 1] -= 5
                        break
                if normal_base_list[i + 1] == 3:
                    normal_base_list[i] += 1
                    normal_base_list[i + 1] = -2
                if normal_base_list[i + 1] == 4:
                    normal_base_list[i] += 1
                    normal_base_list[i + 1] = -1
            contains_bad_chars = (3 in normal_base_list) or (4 in normal_base_list)

        final_val = "".join([int_to_snafu(v) for v in normal_base_list])
        print(final_val)
        return final_val

    # # increment biggest val
    # if normal_base5[0] == "2":
    #     new_base_5 = "1" + "0" * len(normal_base5)
    # elif normal_base5[0] == "1":
    #     new_base_5 = "2" + "0" * (len(normal_base5) - 1)
    # elif (normal_base5[0]) == "0":
    #     new_base_5 = "1" + "0" * (len(normal_base5) - 1)

    # # take diff to required val
    # nn = to_base_5(int(SNAFU_to_decimal(new_base_5)) - int(val))
    # # if it is already now compatible base 5 we take it away char by char and return
    # if not ("3" in nn or "4" in nn):
    #     snafu_list = list(reversed(list(nn)))
    #     new_base_5_reversed = list(reversed(list(new_base_5)))
    #     for i in range(0, len(snafu_list)):
    #         new_val = int(new_base_5_reversed[i]) - int(snafu_list[i])
    #         new_char = int_to_snafu(new_val)
    #         new_base_5_reversed[i] = new_char

    #     new_base_5_reversed.reverse()
    #     return "".join(new_base_5_reversed)
    # else:
    #     pass


if __name__ == "__main__":
    with open(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_twenty_five/input.txt", "r"
    ) as f:
        test_input = list(map(lambda x: x.strip("\n").strip(), f.readlines()))

    total = sum(list(map(lambda x: SNAFU_to_decimal(x), test_input)))

    print(total)

    r = decimal_to_SNAFU(int(total))
    print(r)
