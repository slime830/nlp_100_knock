import json
import re
from urllib import request
import requests

title_column_name = "title"
text_column_name = "text"


def print_separater(problem_num):
    print("-" * 10)
    print(f"problem{problem_num}")

def print_dict(dict:dict):
    for key,value in dict.items():
        print(key+" + "+value)

def problem20(word="イギリス"):
    with open("jawiki-country.json", "r", encoding="utf-8") as f:
        allLines = f.readlines()
    for oneline in allLines:
        line_dict = json.loads(oneline)
        if line_dict.get(title_column_name) == word:
            return line_dict.get(text_column_name)


def problem21(document):
    return re.findall(r"^(.*\[\[Category:.*\]\].*)$", document, re.MULTILINE)


def problem22(document):
    return re.findall(r"^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$", document, re.MULTILINE)


def problem23(document):
    # return re.findall(r"^(\={2,})\s*(.+?)\s*(\={2,}).*$",document,re.MULTILINE)
    return [
        [p[1], len(p[0]) - 1]
        for p in re.findall(r"^(\={2,})\s*(.+?)\s*(\={2,}).*$", document, re.MULTILINE)
    ]


def problem24(document):
    return re.findall(r"\[\[ファイル:(.+?)\|", document)


def problem25(document):
    template = re.findall(
        r"^\{\{基礎情報.*?$(.*?)^\}\}", document, re.MULTILINE + re.DOTALL
    )
    return dict(
        re.findall(
            r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))",
            template[0],
            re.MULTILINE + re.DOTALL,
        )
    )


def problem26(document, template_dict):
    return {key: re.sub(r"\'{2,5}", "", value) for key, value in template_dict.items()}


def problem27(document, template_dict):
    return {
        key: re.sub(
            r"\[\[(?:[^|]*?\|)??([^|]*?)\]\]", r"\1", re.sub(r"\'{2,5}", "", value)
        )
        for key, value in template_dict.items()
    }

def problem28(document,template_dict):
    return {
        key:
        re.sub(
            r'\{\{(?:lang|仮リンク)(?:[^|]*?\|)*?([^|]*?)\}\}' , r'\1',
            re.sub(
                r'<.+?>',"",
                re.sub(
                    r'https?://[\w!?/\+\-_~=;\.,*&@#$%\(\)\'\[\]]+',"",
                    re.sub(
                        r"\[\[(?:[^|]*?\|)??([^|]*?)\]\]", r"\1", re.sub(r"\'{2,5}", "", value)
                    )
                )
            )
        )
        for key,value in template_dict.items()
    }

def problem29(template_dict):
    url="https://commons.wikimedia.org/w/api.php?action=query&titles=File:" + template_dict.get("国旗画像").replace(" ","_") + '&prop=imageinfo&iiprop=url&format=json'
    data = requests.get(url)
    return re.search(r"\"url\":\"(.+?)\"",data.text).group(1)

def main():
    print_separater(20)
    uk_document = problem20()
    print(uk_document)
    print_separater(21)
    print(problem21(uk_document))
    print_separater(22)
    print(problem22(uk_document))
    print_separater(23)
    print(problem23(uk_document))
    print_separater(24)
    print(problem24(uk_document))
    print_separater(25)
    template_dict = problem25(uk_document)
    print_dict(template_dict)
    print_separater(26)
    print_dict(problem26(uk_document, template_dict))
    print_separater(27)
    print_dict(problem27(uk_document, template_dict))
    print_separater(28)
    print_dict(problem28(uk_document,template_dict))
    print_separater(29)
    print(problem29(template_dict))
    

if __name__ == "__main__":
    main()
