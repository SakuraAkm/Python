def tower_builder(n_floors):
    arr = []
    ast = 1
    spz = n_floors

    for x in range(n_floors):
        spz -= 1
        arr.append(" " * spz + "*" * ast + " " * spz)
        ast += 2
    return "\n".join(arr)


print(tower_builder(int(input("Add how many floor the tree need to have: "))))
