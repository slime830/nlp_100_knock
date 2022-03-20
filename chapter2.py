import argparse
from collections import OrderedDict

import numpy as np

f = open("./popular-names.txt", "r", encoding="utf-8")
allLines = [oneline.replace("\n", "") for oneline in f.readlines()]
rows = [oneline.split("\t") for oneline in allLines]
f.close()


def print_separater(problem_num):
    print("-" * 10)
    print(f"problem{problem_num}")


def problem10():
    return len(allLines)


def problem11():
    concat_string = str()
    for oneline in allLines:
        concat_string += oneline
    return concat_string.replace("\t", " ")


def problem12(col1_filepath, col2_filepath):
    with open(col1_filepath, "w", encoding="utf-8") as f1, open(
        col2_filepath, "w", encoding="utf-8"
    ) as f2:
        for row in rows:
            f1.write("{}\n".format(row[0]))
            f2.write("{}\n".format(row[1]))


def problem13(col1_filepath, col2_filepath, merge_filepath):
    with open(col1_filepath, "r", encoding="utf-8") as f1, open(
        col2_filepath, "r", encoding="utf-8"
    ) as f2:
        col1 = [string.replace("\n", "") for string in f1.readlines()]
        col2 = [string.replace("\n", "") for string in f2.readlines()]
        assert len(col1) == len(col2)

    with open(merge_filepath, "w", encoding="utf-8") as fo:
        for c1, c2 in zip(col1, col2):
            fo.write("{}\t{}\n".format(c1, c2))


def problem14(n=5):
    return allLines[:n]


def problem15(n=5):
    return allLines[-n:]


def problem16(n=5):
    return np.array_split(allLines, n)


def problem17(col1_filepath):
    with open(col1_filepath, "r", encoding="utf-8") as f:
        col1_set = set([word.replace("\n", "") for word in f.readlines()])
    return col1_set


def problem18():
    return sorted(rows, key=lambda x: x[2])


def problem19(col1_filepath):
    with open(col1_filepath, "r", encoding="utf-8") as f:
        col1_list = set([word.replace("\n", "") for word in f.readlines()])
    count_dict = OrderedDict()
    for c1 in col1_list:
        if c1 in count_dict.keys():
            count_dict[c1] = count_dict.get(c1) + 1
        else:
            count_dict[c1] = 1

    return OrderedDict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))


def main(args):
    col1_filepath = "./col1.txt"
    col2_filepath = "./col2.txt"
    merge_filepath = "./merge_columns.tsv"

    print("head num : ", args.head)
    print("tail num : ", args.tail)
    print("split num : ", args.split)
    print("--------------------------------")

    print_separater(10)
    print(problem10())
    print_separater(11)
    print(problem11())
    print_separater(12)
    problem12(col1_filepath, col2_filepath)
    print_separater(13)
    problem13(col1_filepath, col2_filepath, merge_filepath)
    print_separater(14)
    print(problem14(args.head))
    print_separater(15)
    print(problem15(args.tail))
    print_separater(16)
    print(problem16(args.split))
    print_separater(17)
    print(problem17(col1_filepath))
    print_separater(18)
    print(problem18())
    print_separater(19)
    print(problem19(col1_filepath))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--head", type=int, default=5)
    parser.add_argument("--tail", type=int, default=5)
    parser.add_argument("--split", type=int, default=5)

    args = parser.parse_args()

    main(args)
