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

import os

from pprint import pprint

from diploma_data import ACC_TOKEN, TARGET_VK


def get_user_communities(token, vkid):
    print("Запрос списка сообществ пользователя {}".format(vkid))
    communities_list = requests.get(
        "https://api.vk.com/method/groups.get",
        params=dict(
            access_token=token,
            v="5.75",
            user_id=vkid,
            # count="50" # use to speed up testing
        )
    )
    return communities_list.json()


def get_community_info(token, *group_ids):
    print("Запрос информации об уникальных сообществах")
    groups_list = ",".join([str(item) for item in group_ids[0]])
    communities_info = requests.get(
        "https://api.vk.com/method/groups.getById",
        params=dict(
            access_token=token,
            v="5.75",
            group_ids="{}".format(groups_list),
            fields="members_count"
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
            # count="50" # use to speed up testing
        )
    )
    return friends_list.json()


def compare_communities(token, vkid):
    user_communities = set(get_user_communities(token, vkid)["response"]["items"])
    user_friends = list(get_user_friends(token, vkid)["response"]["items"])
    user_friends_communities = []
    count = len(user_friends)
    print("У пользователя {} друзей. Сейчас мы запросим их сообщества"
          .format(count))
    for friend in user_friends:
        print("Осталось опросить {} профилей".format(count))
        count -= 1
        try:
            user_friends_communities.append(set(
                get_user_communities(token, friend)["response"]["items"]))
            time.sleep(0.38)
        except KeyError:
            print("Запрос сообществ пользователя {} завершился неудачей.\n"
                  "Возможно, настройки приватности или блокировка".format(friend))
            continue
    print("Идет сравнение списков сообществ...")
    for community_set in user_friends_communities:
        user_communities -= community_set
    return user_communities


def prepare_data(communities_info):
    output_communities_info = {"unique_communities":[]}
    try:
        for one_community_info in communities_info["response"]:
            del one_community_info["is_closed"]
            del one_community_info["photo_50"]
            del one_community_info["photo_100"]
            del one_community_info["photo_200"]
            del one_community_info["screen_name"]
            del one_community_info["type"]
            output_communities_info["unique_communities"].append(one_community_info)
    except KeyError:
        print("Похоже, у искомого пользователя закрыта информация о сообществах")
    return output_communities_info


def write_to_file(data):
    if os.path.isfile("groups.json"):
        with open("groups.json", "a") as f:
            json.dump(data, f, ensure_ascii=False)
    else:
        with open("groups.json", "w") as f:
            json.dump(data, f, ensure_ascii=False)


if __name__ == "__main__":
    answer = ""
    user_id = None
    while answer.lower() != "q":
        answer = input("Эта программа поможет узнать, в каких сообществах "
                       "ВК состоит пользователь, но не состоит никто из его "
                       "друзей\nВведите spygame, чтобы проверить пользователя,"
                       " или q, чтобы выйти\n")
        if answer.lower() == "spygame":
            user_id = input("Введите id пользователя для проверки или нажмите "
                            "enter для того чтобы проверить https://vk.com/"
                            "tim_leary\n")
            if user_id:
                user_communities = compare_communities(ACC_TOKEN, user_id)
            else:
                user_communities = compare_communities(ACC_TOKEN, TARGET_VK)
            unique_communities = get_community_info(ACC_TOKEN, user_communities)
            output_data = prepare_data(unique_communities)
            write_to_file(output_data)
            answer = input("Результаты были записаны в файл groups.json.\n"
                              "Если хотите вывести их на экран - введите print\n"
                              "Если хотите повторить сначала - нажмите enter\n"
                              "Если хотите завершить выполнение - введите q\n")
            if answer.lower() == "print":
                pprint(output_data)
        else:
            continue
