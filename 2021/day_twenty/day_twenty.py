import numpy as np


def read_enhancement_algo(filename):
    with open(filename, "r") as f:
        raw = np.array(list(f.read()))

    return (raw == "#").astype(int)


def read_input_image(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    raw = np.array(list(map(lambda x: list(x.strip("\n")), lines)))
    return (raw == "#").astype(int)


def get_kernal_area(row, col):
    return [row - 1, row, row + 1], [col - 1, col, col + 1]


def get_binary_value(image, row, col, pad_val):
    krs, kcs = get_kernal_area(row, col)
    max_r = image.shape[0] - 1
    max_c = image.shape[1] - 1
    binary_string = ""
    for kr in krs:
        for kc in kcs:
            if kr < 0 or kc < 0 or kr > max_r or kc > max_c:
                binary_string += str(pad_val)
            else:
                binary_string += str(image[kr][kc])

    return binary_string


def get_output_pixel_value(binary_string, enhancement_algo):
    return enhancement_algo[int(binary_string, 2)]


def enhance_image(image, enchancement, pad_val=0):
    n_pad_r = 2
    n_pad_c = 2
    output_image = np.ones(
        (image.shape[0] + 2 * n_pad_r, image.shape[1] + 2 * n_pad_c), dtype=int
    )
    for r_out in range(0, output_image.shape[0]):
        for c_out in range(0, output_image.shape[1]):
            r = r_out - n_pad_r
            c = c_out - n_pad_c
            bin = get_binary_value(image, r, c, pad_val)
            o = get_output_pixel_value(bin, enchancement)
            output_image[r_out][c_out] = o
    if pad_val == 0:
        if enchancement[0] == 0:
            new_pad_val = 0
        else:
            new_pad_val = 1
    elif pad_val == 1:
        if enchancement[-1] == 0:
            new_pad_val = 0
        else:
            new_pad_val = 0
    return output_image, new_pad_val


if __name__ == "__main__":

    enhancement_algo = read_enhancement_algo("day_twenty/image_enhancement.txt")
    print(enhancement_algo)
    print(len(enhancement_algo))

    input_image = read_input_image("day_twenty/image.txt")
    print(input_image)
    print(input_image.shape)

    enhanced_image, pad_val = enhance_image(input_image, enhancement_algo)
    for i in range(0, 49):
        enhanced_image, pad_val = enhance_image(
            enhanced_image, enhancement_algo, pad_val
        )

    print(enhanced_image)
    print(enhanced_image.shape)

    print(np.sum(enhanced_image))
