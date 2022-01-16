def get_specific_values(text):
    text_3 = []

    for x in text:
        if len(x) == 3:
            for y in x:
                if y.startswith('f'):
                    text_3.append(y.upper())

    return text_3