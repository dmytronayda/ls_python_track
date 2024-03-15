char_sequence = "TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu"


def is_included(str, char):
    return char in str


print(is_included(char_sequence, "x"))  # True
print(is_included(char_sequence, "5"))  # False
print(is_included(char_sequence, "_"))  # False
