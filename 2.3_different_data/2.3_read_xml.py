import chardet
from xml.etree import ElementTree
from pprint import pprint


def open_file(filename):
    encode = None
    data = None
    with open("files_to_read/{}".format(filename), "rb") as f:
        specimen = f.read()
        encode = chardet.detect(specimen)
    with open("files_to_read/{}".format(filename), encoding=encode["encoding"]) as f:
        data = ElementTree.parse(f)
        pprint(data)
    return data


def count_frequency(filename):
    data = open_file(filename)
    calc_dict = {}
    values = []
    for news_item in data["rss"]["channel"]["items"]:
        values.extend(news_item["description"].strip().split(" "))
    for word in values:
        if len(word) < 6:
            values.remove(word)
        elif word in calc_dict.keys():
            calc_dict[word] += 1
        else:
            calc_dict[word.lower()] = 1
    print("\nИтак, самые популярные слова в файле {}:".format(filename))
    for k in (sorted(calc_dict, key=calc_dict.get, reverse=True)[:10]):
        print("слово '{}' упоминается {} раз".format(k, calc_dict[k]))


def main():
    answer = None
    while answer is not "q":
        try:
            answer = input(
                "\nПривет! У нас есть четыре файла с новосятми. ('newsafr.json', 'newscy.json', 'neewsfr.json' "
                "и 'newsit.json') \nВведите название файла и узнаете топ10 самых употребляемых в нем слов. "
                "\nУчитываются только слова длиннее 6 букв. Чтобы выйти нажмите q \n")
            if "q" not in answer:
                count_frequency(answer)
        except FileNotFoundError:
            print("Не удалось открыть файл с именем '{}'. Попробуйте еще раз".format(answer))
            continue
    print("Хорошего дня!")


open_file("newsafr.xml")
