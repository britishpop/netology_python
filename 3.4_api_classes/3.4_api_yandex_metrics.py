import requests
from pprint import pprint
from urllib.parse import urlencode


APP_ID = "ab6ca069a2d3464fb5ac78eb18e67ee3"
ACC_TOKEN = "AQAAAAAOGKB-AAUB912-kZcEdE8pnMe6g7FsRiA"
AUTH_URL = "https://oauth.yandex.ru/authorize"
STAT_URL = "https://api-metrika.yandex.ru/stat/v1/data/"
MANAGE_URL = "https://api-metrika.yandex.ru/management/v1/counters"

# params=dict(
#     response_type="token",
#     client_id=APP_ID,
#     scope="metrika:write metrika:read",
#     display="popup"
# )
#
# print("?".join((AUTH_URL, urlencode(params))))

class YaMetrikaShow:
    def __init__(self, token):
        self.token = token

    def authorize(self):
        return {"Authorization": "OAuth {}".format(self.token)}

    def counters(self):
        counters_info = requests.get(
            MANAGE_URL,
            headers=self.authorize()
        )
        counters_list = [x["id"] for x in counters_info.json()["counters"]]
        return counters_list

    def visits(self):
        for counter in test_user.counters():
            params = dict(ids=counter,metrics="ym:s:visits")
            visits_counter = requests.get(
                "?".join((STAT_URL, urlencode(params))),
                headers=self.authorize())
            return visits_counter.json()

    def showings(self):
        for counter in test_user.counters():
            params = dict(ids=counter,metrics="ym:s:pageviews")
            showings_counter = requests.get(
            "?".join((STAT_URL, urlencode(params))),
            headers=self.authorize())
        return showings_counter.json()

    def visitors(self):
        for counter in test_user.counters():
            params = dict(ids=counter,metrics="ym:s:users")
            visitors_counter = requests.get(
            "?".join((STAT_URL, urlencode(params))),
            headers=self.authorize())
        return visitors_counter.json()

test_user = YaMetrikaShow(ACC_TOKEN)

if __name__ == "__main__":
    answer = ""
    while "q" not in answer.lower():
        answer = input("\nПривет! Давайте посмотрим на результаты метрик.\n"
                       "Введите, какую метрику вы хотите увидеть?\n"
                       "Доступные метрики:\n"
                       "'visits' - посещения\n"
                       "'showings' - просмотры\n"
                       "'visitors' - показы\n"
                       "Вся информация собирается с сайта https://britishpop."
                       "github.io/\n")
        if answer.lower() == "visits":
            print("\nКоличество посещений за последнюю неделю: ",
                  round(test_user.visits()["data"][0]["metrics"][0]))
        elif answer.lower() == "showings":
            print("\nКоличество просмотров за последнюю неделю: ",
                  round(test_user.showings()["data"][0]["metrics"][0]))
        elif answer.lower() == "visitors":
            print("\nКоличество посетителей за последнюю неделю: ",
                  round(test_user.visitors()["data"][0]["metrics"][0]))
