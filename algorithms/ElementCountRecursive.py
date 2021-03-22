def element_count_recursive(elems: list) -> int:
    return 0 if elems == [] else 1 + element_count_recursive(elems[1:])