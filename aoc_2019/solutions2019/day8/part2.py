def solve(image_data, width, height):
    npixels_per_layer = width * height
    pixels = []
    for i in range(0, len(image_data), npixels_per_layer):
        layer = image_data[i : i + npixels_per_layer]
        if i == 0:
            pixels = list(layer)
        else:
            for j, pixel in enumerate(layer):
                pixels[j] += pixel

    rows = []
    for i in range(0, len(pixels), width):
        pixels_part = pixels[i : i + width]
        row_pixels = "".join(pixel.lstrip("2")[0] for pixel in pixels_part)
        rows.append(row_pixels)
    return "\n".join(rows)


if __name__ == "__main__":
    import fileinput

    image_data = "".join(line.strip() for line in fileinput.input())
    output = solve(image_data, 25, 6)
    print(output.replace("0", " ").replace("1", "X"))
