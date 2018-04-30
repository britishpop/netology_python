import os


def main():
    answer = None
    while answer is not "q":
        answer = input("Welcome, stranger! Got many good things on sale! What are you buying? \n Or you could always "
                       "input q to exit ")
        found_keys = find_keys(answer)
        if len(found_keys) > 1:
            for one_line in enumerate(found_keys):
                print("Документов с этим значением много. Смотрите:\n {}".format(one_line))
                find_keys(answer)
        elif len(found_keys) == 1:
            print("Это единственный файл с таким значением. На этом наши полномочия все: \n {}".format(found_keys[1]))
        else:
            print("Better luck next time. We found nothing")
            break


def find_keys(answer):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    iteration_list = []
    for i, listed_file in enumerate(os.listdir(os.path.join(current_dir, "migrations"))):
        if listed_file.endswith(".sql"):
            with open(os.path.join(current_dir, "migrations", listed_file)) as f:
                if answer in f.read():
                    iteration_list.append(f)
    return iteration_list


# how to list all files with *.sql?
# listed all files with *.sql
# how to get all file names of *.sql files
# read file with a for cycle
# if item in file
# append filename to list
# substitute filename from list to os.path.join
# repeat search
# print list


main()

# if __name__ == '__main__':
#     # ваша логика
#     pass
