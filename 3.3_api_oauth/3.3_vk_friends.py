import requests


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


def vk_friends(access_token):
    answer = requests.get(
        "https://api.vk.com/method/friends.getMutual",
        params=dict(
            access_token=access_token,
            v="5.75",
            source_uid="2588290",
            target_uid="9638962"
        )
    )
    print("Общие друзья:")
    for mutual_friend, i in enumerate(answer.json().get("response"), 1):
        print("{} https://vk.com/id{}".format(i, mutual_friend))


# def main():
#     print(vk_friends("4040909ac9c8aea74622bc73a481d3f5bde9a9db1055c0a22bef311bcd85c1cd86c41e6a88b232f6c6cd1"))


vk_friends("4040909ac9c8aea74622bc73a481d3f5bde9a9db1055c0a22bef311bcd85c1cd86c41e6a88b232f6c6cd1")
