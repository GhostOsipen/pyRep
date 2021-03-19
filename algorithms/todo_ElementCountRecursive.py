def element_count_recursive(elems: list) -> int:
    if elems == []:
       pass
    else:
        elems.pop(0)
        return element_count_recursive(elems) + 1

print(element_count_recursive([2,4,6]))