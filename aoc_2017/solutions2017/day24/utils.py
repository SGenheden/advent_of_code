def find_bridges(bridge, components, bridges):
    found = False
    for component in components:
        alt_component = (component[1], component[0])
        if component in bridge or alt_component in bridge:
            continue
        if component[0] == bridge[-1][1]:
            found = True
            new_bridge = bridge[:] + [component]
            find_bridges(new_bridge, components, bridges)
        elif component[1] == bridge[-1][1]:
            found = True
            new_bridge = bridge[:] + [alt_component]
            find_bridges(new_bridge, components, bridges)
    if not found:
        bridges.append(bridge)


def make_components(components_spec):
    components = []
    for spec in components_spec:
        a, b = spec.strip().split("/")
        components.append((int(a), int(b)))
    return components
