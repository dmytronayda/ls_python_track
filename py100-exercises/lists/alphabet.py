alphabet = "abcdefghijklmnopqrstuvwxyz"


def split_str(str):
    char_list = []
    for char in str:
        char_list.append(char)
    return char_list


print(
    split_str(alphabet)
)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
