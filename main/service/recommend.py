
recommend_dict = {
    "calories": 0,
    "carbohydrate": 0,
    "proteins": "yogurt_img.png",
    "fat": 0,
    "dietary_fiber": "banana_img.png",
    "sodium": "misosoup_img.png",
    "sodium_chloride_equivalent": "misosoup_img.png",
    "potassium": "hijiki_img.png",
    "calcium": "yogurt_img.png",
    "iron": "rebanira_img.png",
    "magnesium": "almond_img.png",
    "phosphorus": "cheese_img.png",
    "vitamin_A": "ocha_img.png",
    "vitamin_B1": "pumpkin_img.png",
    "vitamin_B2": "salmon_img.png",
    "vitamin_B6": "garlic_img.png",
    "vitamin_B12": "salmon_img.png",
    "niacin": "coffee_img.png",
    "vitamin_C": "strawberry_img.png",
    "vitamin_D": "cheese_img.png",
    "vitamin_E": "almond_img.png"
}


recommend_menu_dict = {
    "calories": 0,
    "carbohydrate": 0,
    "proteins": "yogurt",
    "fat": 0,
    "dietary_fiber": "banana",
    "sodium": "miso-soup",
    "sodium_chloride_equivalent": "miso-soup",
    "potassium": "hijiki",
    "calcium": "yogurt",
    "iron": "rebanira",
    "magnesium": "almond",
    "phosphorus": "cheese",
    "vitamin_A": "ocha",
    "vitamin_B1": "pumpkin",
    "vitamin_B2": "salmon",
    "vitamin_B6": "garlic",
    "vitamin_B12": "salmon",
    "niacin": "coffee",
    "vitamin_C": "strawberry",
    "vitamin_D": "cheese",
    "vitamin_E": "almold"
}

def recommend(per_dict):
    key_of_min_value = min(per_dict)
    recommend_img = recommend_dict[key_of_min_value]
    recommend_menu = recommend_menu_dict[key_of_min_value]
    return recommend_img, recommend_menu




