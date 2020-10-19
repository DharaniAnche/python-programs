def find_duplicates(elements):
    duplicates,seen= set(),set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)

print(find_duplicates([1,1,2,3,4,5,5,98,98,47,2,90]))