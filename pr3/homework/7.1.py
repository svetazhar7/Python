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

# Определение начальной комнаты
current_room = "start"

# Главный игровой цикл
while True:
    # Вывод описания текущей комнаты
    print(rooms[current_room]["title"])
    print(rooms[current_room]["description"])

    # Вывод списка действий в текущей комнате
    for action in rooms[current_room]["actions"].values():
        print(action["text"])

    # Получение выбранного действия от игрока
    chosen_action = input("> ")
    print()
    # Изменение текущей комнаты в соответствии с выбранным действием
    current_room = rooms[current_room]["actions"][chosen_action]["room"]
    if (current_room == "room7"): #если дошли до конца
        print(rooms[current_room]["title"], "\n")
        print(rooms[current_room]["description"])
        break
