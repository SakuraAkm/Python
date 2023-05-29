def is_valid_walk(walk):
    arr = [0, 0]
    print(walk)
    for direction in walk:
        if direction == "n":
            arr[0] += 1
        elif direction == "s":
            arr[0] -= 1
        elif direction == "e":
            arr[1] += 1
        elif direction == "w":
            arr[1] -= 1
    result = abs(arr[0]) + abs(arr[1])
    return True if result == 0 and len(walk) == 10 else False


# arr = ["n", "s", "e", "s", "o"] # False
arr = ["n", "s", "e", "s", "w", "n", "n", "w", "e", "s"]  # True
print(is_valid_walk(arr))
