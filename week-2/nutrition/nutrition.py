NUTRITION = [
    {"fruits": "apple", "calories": "130"},
    {"fruits": "banana", "calories": "110"},
    {"fruits": "grapefruit", "calories": "60"},
    {"fruits": "honeydew melon", "calories": "50"},
    {"fruits": "lemon", "calories": "15"},
    {"fruits": "nectarine", "calories": "60"},
    {"fruits": "peach", "calories": "60"},
    {"fruits": "pineapple", "calories": "50"},
    {"fruits": "strawberries", "calories": "50"},
    {"fruits": "tangerine", "calories": "50"},
    {"fruits": "avocado", "calories": "50"},
    {"fruits": "kiwifruit", "calories": "90"},
    {"fruits": "pear", "calories": "100"},
    {"fruits": "sweet cherries", "calories": "100"},
]

ask = input("Item: ").lower()
for item in NUTRITION:
    if ask == item["fruits"]:
        print("Calories:", item["calories"])
