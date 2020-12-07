def parse_single(specification):
    bag_str, content_str = specification.split(" contain ")
    bag_color, _ = bag_str.rsplit(" ", 1)

    if content_str.startswith("no other"):
        return {bag_color: {}}

    items = {}
    for item_str in content_str.split(", "):
        bag_spec, _ = item_str.rsplit(" ", 1)
        count, color = bag_spec.split(" ", 1)
        items[color] = int(count)
    return {bag_color: items}


def parse_content(content):
    bag_specs = {}
    for line in content.splitlines():
        spec = parse_single(line.strip())
        bag_specs.update(spec)
    return bag_specs
