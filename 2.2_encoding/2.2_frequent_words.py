import chardet


def open_file(filename):
    encode = None
    data = None
    with open("files_to_read/{}".format(filename), "rb") as f:
        specimen = (f.readline())
        encode = chardet.detect(specimen)
    with open("files_to_read/{}".format(filename), encoding=encode["encoding"]) as f:
        data = f.read()
    return (data)


def count_frequency(filename):
    data = open_file(filename)
    values = data.strip().split(" ")
    for word in values:
        if len(word) < 6:
            values.remove(word)


# удалил все слова короче 6 символов, но посчитать оставшиеся не могу

def main():
    answer = None
    while answer is not "q":
        try:
            answer = input("Привет! У нас есть четыре файла с новосятми. Введите название файла и узнаете топ10 самых "
                           "употребляемых в нем слов. Учитываются только слова длиннее 6 букв. Чтобы выйти нажмите q \n")
            if "q" not in answer:
                count_frequency(answer)
        except FileNotFoundError:
            print("Не удалось открыть файл с именем {}. Попробуйте еще раз".format(answer))
            continue
    print("Хорошего дня!")


count_frequency("newsafr.txt")
