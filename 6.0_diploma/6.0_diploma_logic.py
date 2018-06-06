# задача https://docs.google.com/document/d/1sDD59rDrrqzjLu_fZKpXlnig05RUW_YH5PUpKmeyG8w/edit
# 1. Получить токен ВК
# 2. Подключиться к API ВК
# 3. Получить список групп пользователя
# 3.1. Сохранить в массив
# 4. Получить список друзей пользователя
# 4.1. Сохранить в список
# 5. Получить список групп друзей пользователя
# 5.1 Опрашивать API не чаще трех раз в секунду
# 5.2 Сохранить в массивы
# 5.3 Сохранить массивы в список
# 6. Поочередно сравнить массив групп пользователя со всеми массивами групп
# друзей пользователя
# 6.1 Каждый раз при сравнении удалять из массива пользователя совпавшие элементы
# 6.1.1 Возможно постоянно сохранять новый массив несовпавших групп и сравнивать
# только его
# 7. получить информацию об уникальных для пользователя сообществах
# 8. записать полученную информацию в json


import requests

import time

import json

from pprint import pprint

from diploma_data import ACC_TOKEN, TARGET_VK


test_set = set([33938434, 24112387, 53280908, 9624588, 15010187, 130785301,
               124123414, 22440983, 23750039, 47855390, 75185191, 32174764,
                40599470, 28140719, 72326580, 23391543, 16984508, 92307020,
                 30786903, 45491419, 41960539, 41783644, 25205856, 92337511,
                  1210474, 18133228, 22898541, 98748657])

def get_user_communities(token, vkid):
    print("Запрос списка сообществ пользователя {}".format(vkid))
    communities_list = requests.get(
        "https://api.vk.com/method/groups.get",
        params=dict(
            access_token=token,
            v="5.75",
            user_id=vkid,
            count="50"
        )
    )
    return communities_list.json()


def get_community_info(token, *args):
    print(args)
    print("Запрос информации об уникальных сообществах")
    community_info = requests.get(
        "https://api.vk.com/method/groups.get",
        params=dict(
            access_token=token,
            v="5.75",
            group_ids=args,
            fields="id, name, members_count"
        )
    )
    return communities_info.json()

def get_user_friends(token, vkid):
    print("Запрос списка друзей пользователя {}".format(vkid))
    friends_list = requests.get(
        "https://api.vk.com/method/friends.get",
        params=dict(
            access_token=token,
            v="5.75",
            user_id=vkid,
            count="50"
        )
    )
    return friends_list.json()


def compare_communities(token, vkid):
    user_communities = set(get_user_communities(token, vkid)["response"]["items"])
    user_friends = list(get_user_friends(token, vkid)["response"]["items"])
    user_friends_communities = []
    counter = 1
    for friend in user_friends:
        try:
            user_friends_communities.append(set(
                get_user_communities(token, friend)["response"]["items"]))
            time.sleep(0.38)
        except KeyError:
            print("Запрос сообществ пользователя {} завершился неудачей.\n"
                  "Возможно, настройки приватности".format(friend))
            continue
    for community_set in user_friends_communities:
        print("Сравнение списков сообществ, шаг {}".format(counter))
        user_communities -= community_set
        counter += 1
    return user_communities

pprint(get_community_info(ACC_TOKEN, test_set))
