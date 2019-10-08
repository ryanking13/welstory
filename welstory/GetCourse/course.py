class Menu:
    def __init__(self, menu):
        self.type = menu["menu_meal_type"]  # breakfast(1)/lunch(2)/dinner(3)
        self.course = menu["course_txt"]  # A/B/C
        self.name = menu["menu_name"]
        self.image = (
            menu["image_url"] + menu["photo_cd"]
            if menu["image_url"] is not None
            else ""
        )
        self.kcal = menu["kcal"]

    def __repr__(self):
        return f"{self.name}({self.kcal} kcal)"

    def dump(self):
        return {"name": self.name, "image": self.image, "kcal": self.kcal}


class Course:
    def __init__(self):
        self.kcal = 0
        self.main = None
        self.side = []

    def add_menu(self, menu):
        m = Menu(menu)
        if menu["tot_kcal"] != 0:  # only main dish contains tot_kcal value
            self.kcal = menu["tot_kcal"]
            self.main = m
        else:
            self.side.append(m)

    def __repr__(self):
        return f"{repr(self.main)}/" + "/".join([repr(s) for s in self.side])

    def dump(self):
        d = {
            "type": self.main.type,
            "kcal": self.kcal,
            "course": self.main.course,
            "main": self.main.dump(),
            "side": [s.dump() for s in self.side],
        }

        return d
