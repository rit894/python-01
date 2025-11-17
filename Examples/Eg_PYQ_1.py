# Data organization: dictionary of states
states = {
    "Andhra Pradesh": {
        "official": ["Telugu", "English"],
        "spoken": ["Urdu", "Hindi", "Banjara", "Tamil", "Kannada", "Marathi", "Oriya"]
    },
    "Karnataka": {
        "official": ["Kannada", "English"],
        "spoken": ["Urdu", "Telugu", "Tamil", "Marathi"]
    },
    "Kerala": {
        "official": ["Malayalam", "English"],
        "spoken": ["Hindi", "Kannada", "Tamil", "Tulu"]
    },
    "Tamilnadu": {
        "official": ["Tamil", "English"],
        "spoken": ["Telugu", "Kannada", "Urdu", "Malayalam", "Hindi"]
    },
    "Telangana": {
        "official": ["Telugu", "Urdu"],
        "spoken": ["Hindi", "Tamil", "Kannada", "Marathi", "Oriya"]
    }
}


def max_languages_state():
    max_count = 0
    max_state = ""
    for state, langs in states.items():
        total = len(langs["official"]) + len(langs["spoken"])
        if total > max_count:
            max_count = total
            max_state = state
    print(max_state)

def count_spoken(state_name):
    if state_name in states:
        print(len(states[state_name]["spoken"]))
    else:
        print("Error")


def states_with_language(language):
    result = []
    for state, langs in states.items():
        if language in langs["spoken"] and language not in langs["official"]:
            result.append(state)
    if result:
        print(" ".join(result))
    else:
        print("Error")

def unique_languages():
    lang_count = {}
    for state, langs in states.items():
        for lang in langs["spoken"]:
            lang_count[lang] = lang_count.get(lang, 0) + 1
    for lang, count in lang_count.items():
        if count == 1:
            print(lang)


user_input = input().strip()

if user_input == "1":
    max_languages_state()
elif user_input.startswith("2,"):
    _, state_name = user_input.split(",")
    count_spoken(state_name)
elif user_input.startswith("3,"):
    _, language = user_input.split(",")
    states_with_language(language)
elif user_input == "4":
    unique_languages()
else:
    print("Error")