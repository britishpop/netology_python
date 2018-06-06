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


import requests

from pprint import pprint

from diploma_data import ACC_TOKEN, TARGET_VK


def get_user_communities(token, vkid):
    print("Запрос списка сообществ пользователя {}".format(vkid))
    communities_list = requests.get(
        "https://api.vk.com/method/groups.get",
        params=dict(
            access_token=token,
            v="5.75",
            user_id=vkid
        )
    )
    return communities_list.json()


def get_user_friends(token, vkid):
    print("Запрос списка друзей пользователя {}".format(vkid))
    friends_list = requests.get(
        "https://api.vk.com/method/friends.get",
        params=dict(
            access_token=token,
            v="5.75",
            user_id=vkid
        )
    )
    return friends_list.json()


def compare_communities(token, vkid):
    user_communities = set(get_user_communities(token, vkid)["response"]["items"])
    user_friends = list(get_user_friends(token, vkid)["response"]["items"])
    user_friends_communities = []
    for friend in user_friends:
        try:
            user_friends_communities.append(set(
                get_user_communities(token, friend)["response"]["items"]))
        except KeyError:
            print("Запрос сообществ пользователя {} завершился неудачей.\n"
                  "Возможно, настройки приватности".format(friend))
            continue
    pprint(user_friends_communities)
    # for i, community_set in enumerate(user_friends_communities), 1:
    #     print("Сравнение списков сообществ, шаг {}".format(i))
    #     user_communities.different(community_set) # TODO: add set method for comparison

# pprint(get_user_communities(ACC_TOKEN, TARGET_VK)["response"]["items"])

pprint(compare_communities(ACC_TOKEN, TARGET_VK))
