import requests


# access_token = "4040909ac9c8aea74622bc73a481d3f5bde9a9db1055c0a22bef311bcd85c1cd86c41e6a88b232f6c6cd1"
# my_vk = "2588290"
# test_target_vk = "9638962"


# def get_token():
#     params = dict(
#         client_id="6483145",
#         redirect_uri="https://oauth.vk.com/blank.html",
#         display="page",
#         scope="friends",
#         response_type="token",
#         v="5.75"
#     )
#     print("?".join(("https://oauth.vk.com/authorize", urlencode(params))))
#    Не получилось взять токен в автоматическом режиме. Оставил для генерации ссылок


def vk_friends(access_token, source_acc, target_acc):
    answer = requests.get(
        "https://api.vk.com/method/friends.getMutual",
        params=dict(
            access_token=access_token,
            v="5.75",
            source_uid=source_acc,
            target_uid=target_acc
        )
    )
    try:
        print("Общие друзья:")
        for i, mutual_friend in enumerate(answer.json().get("response"), 1):
            print("{} https://vk.com/id{}".format(i, mutual_friend))
    except TypeError:
        print("Ответ пришел пустой. Кажется неправильный токен или id")


def main():
    answer = ""
    while "q" not in answer:
        answer = input("Привет! Давай узнаем общих друзей. Чтобы выйти введи q, чтобы продолжить input any key ")
        if "q" in answer:
            continue
        else:
            source_acc = input("Введи id кого будешь сравнивать (только цифры) ")
            target_acc = input("Введи id с кем будешь сравнивать (только цифры) ")
            token = input("Введи актуальный токен (вверху есть закоменченый код для генерации) ")
            vk_friends(token, source_acc, target_acc)


main()
