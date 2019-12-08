from collections import Counter


def solve(image_data, width, height):
    npixels_per_layer = width * height
    min_zeros = None
    result = None
    for i in range(0, len(image_data), npixels_per_layer):
        layer = image_data[i : i + npixels_per_layer]
        counts = Counter(layer)
        if min_zeros is None or counts["0"] < min_zeros:
            result = counts["1"] * counts["2"]
            min_zeros = counts["0"]
    return result


if __name__ == "__main__":
    import fileinput

    image_data = "".join(line.strip() for line in fileinput.input())
    output = solve(image_data, 25, 6)
    print(f"Solution is {output}")
