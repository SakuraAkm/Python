import string


def high(x):
    if x is None or x == "":
        return 0

    alphabet = string.ascii_lowercase
    alpha_arr = []
    arr = x.split()
    arr2 = []
    result = 0

    for letter in alphabet:
        alpha_arr.append(letter)

    for word in arr:
        for letter in word:
            result += alpha_arr.index(letter) + 1
        arr2.append(result)
        result = 0

    return arr[arr2.index(max(arr2))]


print(
    high(
        input(
            "you can write many words, the output will be the word with the highest point\nfeel free to add your words: "
        )
    )
)
