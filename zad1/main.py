def add_numbers(number1: int, number2: int):
    return number1 + number2


def join_strings(string1: str, string2: str):
    strings = [string1, string2]
    return " ".join(strings)


def show_alphabet(how_many: int):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet[0:how_many]


def language_dictionary(language: str):
    dict= {
        "Polish": "Poland",
        "German": "Germany"
    }

    ans = None

    if language in dict.keys():
        return dict[language]
    else:
        for lang, count in dict.items():
            if language == count:
                return lang

if __name__ == '__main__':
    print(add_numbers(1, 2.5))
    print(join_strings("Spoko", "Test"))
    print(show_alphabet(3))
