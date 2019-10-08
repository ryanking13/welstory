from collections import defaultdict
import datetime
import requests
import json
from .course import Course


class MealType:
    LUNCH = 2
    DINNER = 3


class RestaurantCode:
    # TODO: add more codes
    MULTICAMPUS = "REST000133"
    SNURESEARCH = "REST000176"


LOGIN_URL = "http://mw.welstory.com/nsimple_member_insert.do"
MENU_URL = "http://mw.welstory.com/nmenu_today.do"


def today():
    # YYYYMMDD format
    return str(datetime.datetime.today().strftime("%Y%m%d"))


def login():
    sess = requests.session()
    sess.post(
        LOGIN_URL,
        data={
            "MODULE": "LOGIN_SIMPLE",
            "mem_name": "김이박",
            "phone": "01012341234",
            "birth": "000000",
            "sex": "3",
            "agree_date": today(),
            "agree_event": "0",
            "device_type": "I",
            "app_type": "1001",
        },
    )

    return sess


def get_menu(code=RestaurantCode.SNURESEARCH, date=None, meal_type=MealType.LUNCH):
    if date is None:
        date = today()

    data = {
        "MODULE": "TODAY_MENU_LIST",
        "app_type": "1001",
        "device_type": "I",
        "restaurant_code": code,
        "date": date,
        "meal_type": meal_type,
    }

    sess = login()
    resp = sess.post(MENU_URL, data=data, allow_redirects=False)

    # if authentication failed, status_code will be 302(redirect)
    if resp.status_code != 200:
        raise (ConnectionError("Authentication failed, maybe cookie expired"))

    menus = resp.json()["menu_array"]

    courses = defaultdict(lambda: Course())
    for menu in menus:
        # menu_course_type identifies where menu belongs to
        course = menu["menu_course_type"]
        courses[course].add_menu(menu)

    courses_dump = [c.dump() for c in courses.values()]
    return courses_dump


if __name__ == "__main__":
    print(get_menu())
