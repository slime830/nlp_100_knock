import random


def print_separater(problem_num):
    print("-" * 10)
    print(f"problem{problem_num}")


def problem00(s):
    return "".join(list(reversed(s)))


def problem01(s):
    return "".join([s[i] for i in [j for j in range(7) if j % 2 == 0]])


def problem02(s1, s2):
    out_s = str()
    for c1, c2 in zip(s1, s2):
        out_s += c1 + c2

    return out_s


def problem03(s):
    words = [w.replace(",", "").replace(".", "") for w in s.split()]
    c_num_list = list()
    for word in words:
        c_num_list.append(len(word))

    return c_num_list


def problem04(s):
    words = [w.replace(",", "").replace(".", "") for w in s.split()]
    first_character_list = [0, 4, 5, 6, 7, 8, 14, 15, 18]
    output_dict = dict()
    for i, word in enumerate(words):
        if i in first_character_list:
            output_dict[word[0]] = i
        else:
            output_dict[word[:2]] = i

    return output_dict


def problem05(s):
    words = [w.replace(",", "").replace(".", "") for w in s.split()]
    characters = [c for c in s]
    # word n-gram
    word_bigrams = list()
    for i in range(len(words) - 1):
        word_bigrams.append(words[i] + " " + words[i + 1])
    # character n-gram
    character_bigrams = list()
    for i in range(len(characters) - 1):
        character_bigrams.append(characters[i] + characters[i + 1])

    return word_bigrams, character_bigrams


def problem06(input_s1, input_s2, bigram):
    _, X = problem05(input_s1)
    _, Y = problem05(input_s2)

    X = set(X)
    Y = set(Y)

    union = X | Y
    intersection = X & Y
    difference = X - Y

    return union, intersection, difference, bigram in X, bigram in Y


def problem07(x, y, z):
    return "{}時の{}は{}".format(x, y, z)


def problem08(s):
    def cipher(s):
        output_characters = list()
        for c in s:
            if c.islower():
                output_characters.append(chr(219 - ord(c)))
            else:
                output_characters.append(c)

        return "".join(output_characters)

    return cipher(s)


def problem09(s):
    def characterShuffle(word):
        head_character = word[0]
        tail_character = word[-1]
        middle_characters = list(word[1:-1])
        random.shuffle(middle_characters)
        return head_character + "".join(middle_characters) + tail_character

    words = [w.replace(",", "").replace(".", "") for w in s.split()]
    shufflewords = [characterShuffle(word) for word in words]

    return " ".join(shufflewords)


def main():
    print_separater("00")
    print(problem00("stressed"))
    print_separater("01")
    print(problem01("パタトクカシーー"))
    print_separater("02")
    print(problem02("パトカー", "タクシー"))
    print_separater("03")
    print(
        problem03(
            "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        )
    )
    print_separater("04")
    print(
        problem04(
            "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
        )
    )
    print_separater("05")
    print(problem05("I am an NLPer"))
    print_separater("06")
    print(problem06("paraparaparadise", "paragraph", "se"))
    print_separater("07")
    print(problem07(12, "気温", "22.4"))
    print_separater("08")
    cypher = problem08("this is test string")
    original = problem08(cypher)
    print(cypher, " -> ", original)
    print_separater("09")
    print(problem09("messi ronald neymar"))


if __name__ == "__main__":
    main()
