#zip: zip(*iterables)
#built-in iterables (like: list, string, dict), or user-defined iterables
lang=['python','java','c']
creators=['guido','james','denis']
for lang,creators in zip(lang,creators):
    print(lang,creators)
