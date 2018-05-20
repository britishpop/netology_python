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
        counters_list = requests.get(
            MANAGE_URL,
            headers=self.authorize()
        )
        return counters_list.json()

    def visits(self):
        params = dict(

        )
        requests.get("?".join(STAT_URL, params))
        pass

    def showings(self):
        pass

    def visitors(self):
        pass

test_user = YaMetrikaShow(ACC_TOKEN)

pprint(test_user.counters())
