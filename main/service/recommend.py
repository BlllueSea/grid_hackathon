import random
import numpy as np
from operator import itemgetter

recommend_dict = {
    "calories": 0,
    "carbohydrate": 0,
    "proteins": ["yogurt_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "fat": 0,
    "dietary_fiber": ["banana_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "sodium": ["misosoup_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "sodium_chloride_equivalent": ["misosoup_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "potassium": ["hijiki_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "calcium": ["nori_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "iron": ["rebanira_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "magnesium": ["almond_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "phosphorus": ["cheese_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "vitamin_A": ["ocha_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "vitamin_B1": ["pumpkin_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "vitamin_B2": ["salmon_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "vitamin_B6": ["garlic_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "vitamin_B12": ["salmon_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "niacin": ["coffee_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "vitamin_C":[ "strawberry_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "vitamin_D": ["cheese_img.png","natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
    "vitamin_E": ["almond_img.png""natto_img.png","kozakana_img.png","cheese_img.png","momendohu_img.png","horenso_img.png","almond_img.png"],
}

recommend_menu_dict = {
    "calories": 0,
    "carbohydrate": 0,
    "proteins": ["yogurt","natto","kozakana","cheese","momendohu","horenso","almond"],
    "fat": 0,
    "dietary_fiber": ["banana","natto","kozakana","cheese","momendohu","horenso","almond"],
    "sodium": ["miso-soup","natto","kozakana","cheese","momendohu","horenso","almond"],
    "sodium_chloride_equivalent": ["miso-soup","natto","kozakana","cheese","momendohu","horenso","almond"],
    "potassium": ["hijiki","natto","kozakana","cheese","momendohu","horenso","almond"],
    "calcium": ["nori","natto","kozakana","cheese","momendohu","horenso","almond"],
    "iron": ["rebanira","natto","kozakana","cheese","momendohu","horenso","almond"],
    "magnesium": ["almond","natto","kozakana","cheese","momendohu","horenso","almond"],
    "phosphorus": ["cheese","natto","kozakana","cheese","momendohu","horenso","almond"],
    "vitamin_A": ["ocha","natto","kozakana","cheese","momendohu","horenso","almond"],
    "vitamin_B1": ["pumpkin","natto","kozakana","cheese","momendohu","horenso","almond"],
    "vitamin_B2": ["salmon","natto","kozakana","cheese","momendohu","horenso","almond"],
    "vitamin_B6": ["garlic","natto","kozakana","cheese","momendohu","horenso","almond"],
    "vitamin_B12":[ "salmon","natto","kozakana","cheese","momendohu","horenso","almond"],
    "niacin": ["coffee","natto","kozakana","cheese","momendohu","horenso","almond"],
    "vitamin_C": ["strawberry","natto","kozakana","cheese","momendohu","horenso","almond"],
    "vitamin_D": ["cheese","natto","kozakana","cheese","momendohu","horenso","almond"],
    "vitamin_E": ["almold","natto","kozakana","cheese","momendohu","horenso","almond"]
}



def recommend(per_dict):
    rand1 = random.randint(0, 4) #random for choosing the small vitamins
    rand2 = random.randint(0, 6) #random for choosing which item to recommend
    inOrder = sorted(per_dict.items(), key = itemgetter(1))
    key_of_recommend_nutrient = inOrder[rand1][0]
    print(key_of_recommend_nutrient)
    recommend_img = recommend_dict[key_of_recommend_nutrient][rand2]
    recommend_menu = recommend_menu_dict[key_of_recommend_nutrient][rand2]
    print(recommend_img)
    print(recommend_menu)
    return recommend_img, recommend_menu
