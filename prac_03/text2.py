def is_vaild_label(label):
    if len(label) <5:
        return False
    if not label[0].isupper():
        return False
    for char in label:
        if not char.isnumeric():
            return False
    return True
print(is_vaild_label('High5'))

