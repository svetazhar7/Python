rooms = { #список комнат
    "start": {
        "title": "Комната №1",
        "description": "Вы в начале лабиринта. Сможете ли из него выбраться?",
        "actions": {
            "1": {
                "text": "1. Проход на запад",
                "room": "room2"
            }
        }
    },
    "room2": {
        "title": "Комната №2",
        "description": "Вы находитесь в комнате №2.",
        "actions": {
            "1": {
                "text": "1. Проход на восток",
                "room": "start"
            },
            "2": {
                "text": "2. Проход на запад",
                "room": "room3"
            }
        }
    },
    "room3": {
        "title": "Комната №3",
        "description": "Вы находитесь в комнате №3.",
        "actions": {
            "1": {
                "text": "1. Проход на север",
                "room": "room5"
            },
            "2": {
                "text": "2. Проход на восток",
                "room": "room2"
            },
            "3": {
                "text": "3. Проход на запад",
                "room": "room4"
            }
        }
    },
    "room4": {
        "title": "Комната №4",
        "description": "Вы находитесь в комнате №4.",
        "actions": {
            "1": {
                "text": "1. Проход на восток",
                "room": "room3"
            }
        }
    },
    "room5": {
        "title": "Комната №5",
        "description": "Вы находитесь в комнате №5.",
        "actions": {
            "1": {
                "text": "1. Проход на юг",
                "room": "room3"
            },
            "2": {
                "text": "2. Проход на восток",
                "room": "room6"
            }
        }
    },
    "room6": {
        "title": "Комната №6",
        "description": "Вы находитесь в комнате №6.",
        "actions": {
            "1": {
                "text": "1. Проход на север",
                "room": "room7"
            },
            "2": {
                "text": "2. Проход на восток",
                "room": "room8"
            },
            "3": {
                "text": "3. Проход на запад",
                "room": "room5"
            }
        }
    },
    "room7": {
        "title": "Комната №7",
        "description": "Вы находитесь в комнате №7.. Вы нашли выход из лабиринта!",
        "actions": {}
    },
    "room8": {
        "title": "Комната №8",
        "description": "Вы находитесь в комнате №8.",
        "actions": {
            "1": {
                "text": "1. Проход на запад",
                "room": "room6"
            },
            "2": {
                "text": "2. Проход на юг",
                "room": "room9"
            }
        }
    },
    "room9": {
        "title": "Комната №9",
        "description": "Вы находитесь в комнате №9.",
        "actions": {
            "1": {
                "text": "1. Проход на север",
                "room": "room8"
            },
            "2": {
                "text": "2. Проход на юг",
                "room": "room10"
            }
        }
    },
    "room10": {
        "title": "Комната №10",
        "description": "Вы находитесь в комнате №10.",
        "actions": {
            "1": {
                "text": "1. Проход на север",
                "room": "room9"
            }
        }
    }
}

visited = set()  # список посещенных комнат


def dead_ends():
    dead_ends_list=[]
    for room in rooms:
        if (len(rooms[room]["actions"])==1):#если в конате только один выход
            dead_ends_list.append(rooms[room])
    if len(dead_ends_list) > 0:  # если тупики есть
        print("Тупики в следующих комнатах:")
        for room in dead_ends_list:  #список тупиков
            print(" ",room["title"])
    else:  # Если в игре нет тупиков
        print("Тупики в данной игре отсутсвуют!")


dead_ends()
