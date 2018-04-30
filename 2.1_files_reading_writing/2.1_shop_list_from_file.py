def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                new_shop_list_item = dict(ingredient)
                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingredient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
        else:
            print("Блюдо {} в кулинарной книге отсутствует".format(dish))
    return shop_list


def get_cook_book():
    cook_book = {}
    with open("2.1_cook_book_example.txt", encoding='utf8') as f:
        for line in f:
            ingredients = []
            ingredients_count = int(f.readline())
            counter = 0
            while counter < ingredients_count:
                counter += 1
                single_ingredient = list(f.readline().strip().split(" | "))
                ingredients.append(dict(ingredient_name=single_ingredient[0], quantity=int(single_ingredient[1]),
                                        measure=single_ingredient[2]))
            f.readline()
            cook_book[line.strip().lower()] = ingredients
    return cook_book



def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
