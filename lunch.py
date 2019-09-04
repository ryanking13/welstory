from collections import defaultdict
import requests
import json
try:
    from session import cookies
except:
    from session_template import cookies
    if not cookies['JSESSIONID']:
        print('[-] Add session id on `session_template.py`')
        exit(1)


url = 'http://mw.welstory.com/nmenu_today.do'

class Menu:
    
    def __init__(self, menu):
        self.course = menu['course_txt']
        self.name = menu['menu_name']
        self.image = menu['image_url'] + menu['photo_cd'] if menu['image_url'] is not None else ''
        self.kcal = menu['kcal']

    def __repr__(self):
        return f'{self.name}({self.kcal} kcal)'
    
    def dump(self):
        return {
            'name': self.name,
            'image': self.image,
            'kcal': self.kcal,
        }

class Course:
    
    def __init__(self):
        self.kcal = 0
        self.main = None
        self.side = []
    
    def add_menu(self, menu):
        m = Menu(menu)
        if menu['tot_kcal'] != 0: # only main dish contains tot_kcal value
            self.kcal = menu['tot_kcal']
            self.main = m
        else:
            self.side.append(m)
    
    def __repr__(self):
        return (
            f'{repr(self.main)}/' + '/'.join([repr(s) for s in self.side])
        )
    
    def dump(self):
        d = {
            'kcal': self.kcal,
            'course': self.main.course,
            'main': self.main.dump(),
            'side': [s.dump() for s in self.side],
        }

        return d


def get_menu(restaurant_code='REST000133', date='20190904', meal_type='2'):
    data = {
        'MODULE': 'TODAY_MENU_LIST',
        'app_type': '1001',
        'device_type': 'I',
        'restaurant_code': restaurant_code,
        'date': date,
        'meal_type': meal_type,
    }

    resp = requests.post(url, cookies=cookies, data=data, allow_redirects=False)

    if (resp.status_code != 200):
        raise(ConnectionError("Authentication failed, maybe cookie expired"))

    menus = resp.json()['menu_array']

    courses = defaultdict(lambda: Course())
    for menu in menus:
        course = menu['course_txt']
        courses[course].add_menu(menu)
    
    courses_dump = [c.dump() for c in courses.values()]
    return courses_dump


if __name__ == '__main__':
    print(get_menu())