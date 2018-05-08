import os


def main():
    answer = None
    search_memory = []
    while answer is not "q":
        answer = input("Введите значение для поиска или нажмите q, чтобы выйти.\nВнимание! Вторая и последующие "
                       "итерации поиска будут проходить среди уже отобранных файлов ")
        found_keys = find_keys(answer, search_memory)
        if len(found_keys) > 1:
            print("Вот в этих файлах есть {}:".format(answer))
            for i, single_key in enumerate(found_keys, 1):
                print(i, single_key)
            search_memory = found_keys
        elif len(found_keys) == 1:
            print("Нашелся всего один файл, содержащий {}".format(answer))
        else:
            print("Кажется, ничего не нашлось. Попробуйте поискать что-то другое\n")


def find_keys(answer, search_memory):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    iteration_list = []
    if not search_memory:
        for listed_file in os.listdir(os.path.join(current_dir, "migrations")):
            if listed_file.endswith(".sql"):
                with open(os.path.join(current_dir, "migrations", listed_file)) as f:
                    if answer in f.read():
                        iteration_list.append(f.name)
    else:
        for previously_found in search_memory:
            with open(previously_found) as f:
                if answer in f.read():
                    iteration_list.append(f.name)
    return iteration_list


main()
