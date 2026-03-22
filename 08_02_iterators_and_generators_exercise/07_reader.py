def read_next(*collections):
    for collection in collections:
        yield from collection

    # for collection in collections:
    #     for el in collection:
    #         yield el



for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
print()
print("============")

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
