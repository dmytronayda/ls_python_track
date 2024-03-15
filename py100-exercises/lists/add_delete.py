energy = ["fossil", "solar", "wind", "tidal", "fusion"]


def add_and_remove(remove_elem, add_elem, elements):
    elements.remove(remove_elem)
    elements.append(add_elem)
    return elements


print(
    add_and_remove("fossil", "geothermal", energy)
)  # ['solar', 'wind', 'tidal', 'fusion', 'geothermal']
