def parse_garbage(stream):
    stream = stream[1:]
    garbage = ""
    while True:
        if stream[0] == "!":
            stream = stream[2:]
        elif stream[0] == ">":
            return stream[1:], garbage
        else:
            garbage += stream[0]
            stream = stream[1:]


def parse_group(stream):
    stream = stream[1:]  # Remove first {
    garbages = []
    children = []
    while True:
        if stream[0] == "<":
            stream, garbage = parse_garbage(stream)
            garbages.append(garbage)
        elif stream[0] == "{":
            stream, child = parse_group(stream)
            children.append(child)
        elif stream[0] == "}":
            break
        else:
            stream = stream[1:]
    return stream[1:], {"children": children, "garbage": garbages}
