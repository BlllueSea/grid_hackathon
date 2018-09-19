from .settings import *



def get_food_key_from_value(predict_value):

    k= [k for k, v in FOOD_LIST.items() if v == predict_value]
    food_key = k[0]
    return food_key



def choose_reference_list(sex):

    if sex == 0:
        reference_dict = REFERENCE_NUTRITION_LIST["M"]
    else:
        reference_dict = REFERENCE_NUTRITION_LIST["F"]

    return reference_dict



def compare_nutrition(predict_value, sex):

    per_list = []
    real_value_list = []
    reference_dict = choose_reference_list(sex)
    food_name = get_food_key_from_value(predict_value)

    def compare_calories():
        calories = NUTRITION_LIST[food_name]["calories"]
        reference_calories = reference_dict["calories"]
        per_calories = calories / reference_calories * 100
        return per_calories, calories


    def compare_carbohydrate():
        carbohydrate = NUTRITION_LIST[food_name]["carbohydrate"]
        reference_carbohydrate = reference_dict["carbohydrate"]
        per_carbohydrate = carbohydrate / reference_carbohydrate * 100
        return per_carbohydrate, carbohydrate


    def compare_proteins():
        proteins = NUTRITION_LIST[food_name]["proteins"]
        reference_proteins = reference_dict["proteins"]
        per_proteins = proteins / reference_proteins * 100
        return per_proteins, proteins


    def compare_fat():
        fat = NUTRITION_LIST[food_name]["fat"]
        reference_fat = reference_dict["fat"]
        per_fat = fat / reference_fat * 100
        return per_fat, fat


    def compare_dietary_fiber():
        dietary_fiber = NUTRITION_LIST[food_name]["dietary_fiber"]
        reference_dietary_fiber = reference_dict["dietary_fiber"]
        per_dietary_fiber = dietary_fiber / reference_dietary_fiber * 100
        return per_dietary_fiber, dietary_fiber


    def compare_sodium():
        sodium = NUTRITION_LIST[food_name]["sodium"]
        reference_sodium = reference_dict["sodium"]
        per_sodium = sodium / reference_sodium * 100
        return per_sodium, sodium


    def compare_sodium_chloride_equivalent():
        sodium_chloride_equivalent = NUTRITION_LIST[food_name]["sodium_chloride_equivalent"]
        reference_sodium_chloride_equivalent = reference_dict["sodium_chloride_equivalent"]
        per_sodium_chloride_equivalent = sodium_chloride_equivalent / reference_sodium_chloride_equivalent * 100
        return per_sodium_chloride_equivalent, sodium_chloride_equivalent


    def compare_potassium():
        potassium = NUTRITION_LIST[food_name]["potassium"]
        reference_potassium = reference_dict["potassium"]
        per_potassium = potassium / reference_potassium * 100
        return per_potassium, potassium


    def compare_calcium():
        calcium = NUTRITION_LIST[food_name]["calcium"]
        reference_calcium = reference_dict["calcium"]
        per_calcium = calcium / reference_calcium * 100
        return per_calcium, calcium


    def compare_iron():
        iron = NUTRITION_LIST[food_name]["iron"]
        reference_iron = reference_dict["iron"]
        per_iron = iron / reference_iron * 100
        return per_iron, iron


    def compare_magnesium():
        magnesium = NUTRITION_LIST[food_name]["magnesium"]
        reference_magnesium = reference_dict["magnesium"]
        per_magnesium = magnesium / reference_magnesium * 100
        return per_magnesium, magnesium


    def compare_phosphorus():
        phosphorus = NUTRITION_LIST[food_name]["phosphorus"]
        reference_phosphorus = reference_dict["phosphorus"]
        per_phosphorus = phosphorus / reference_phosphorus * 100
        return per_phosphorus, phosphorus


    def compare_vitamin_A():
        vitamin_A = NUTRITION_LIST[food_name]["vitamin_A"]
        reference_vitamin_A = reference_dict["vitamin_A"]
        per_vitamin_A = vitamin_A / reference_vitamin_A * 100
        return per_vitamin_A, vitamin_A


    def compare_vitamin_B1():
        vitamin_B1 = NUTRITION_LIST[food_name]["vitamin_B1"]
        reference_vitamin_B1 = reference_dict["vitamin_B1"]
        per_vitamin_B1 = vitamin_B1 / reference_vitamin_B1 * 100
        return per_vitamin_B1, vitamin_B1


    def compare_vitamin_B2():
        vitamin_B2 = NUTRITION_LIST[food_name]["vitamin_B2"]
        reference_vitamin_B2 = reference_dict["vitamin_B2"]
        per_vitamin_B2 = vitamin_B2 / reference_vitamin_B2 * 100
        return per_vitamin_B2, vitamin_B2


    def compare_vitamin_B6():
        vitamin_B6 = NUTRITION_LIST[food_name]["vitamin_B6"]
        reference_vitamin_B6 = reference_dict["vitamin_B6"]
        per_vitamin_B6 = vitamin_B6 / reference_vitamin_B6 * 100
        return per_vitamin_B6, vitamin_B6


    def compare_vitamin_B12():
        vitamin_B12 = NUTRITION_LIST[food_name]["vitamin_B12"]
        reference_vitamin_B12 = reference_dict["vitamin_B12"]
        per_vitamin_B12 = vitamin_B12 / reference_vitamin_B12 * 100
        return per_vitamin_B12, vitamin_B12


    def compare_niacin():
        niacin = NUTRITION_LIST[food_name]["niacin"]
        reference_niacin = reference_dict["niacin"]
        per_niacin = niacin / reference_niacin * 100
        return per_niacin, niacin


    def compare_vitamin_C():
        vitamin_C = NUTRITION_LIST[food_name]["vitamin_C"]
        reference_vitamin_C = reference_dict["vitamin_C"]
        per_vitamin_C = vitamin_C / reference_vitamin_C * 100
        return per_vitamin_C, vitamin_C


    def compare_vitamin_D():
        vitamin_D = NUTRITION_LIST[food_name]["vitamin_D"]
        reference_vitamin_D = reference_dict["vitamin_D"]
        per_vitamin_D = vitamin_D/ reference_vitamin_D * 100
        return per_vitamin_D, vitamin_D


    def compare_vitamin_E():
        vitamin_E = NUTRITION_LIST[food_name]["vitamin_E"]
        reference_vitamin_E = reference_dict["vitamin_E"]
        per_vitamin_E = vitamin_E / reference_vitamin_E * 100
        return per_vitamin_E, vitamin_E



    per_calories, calories = compare_calories()
    per_carbohydrate, carbohydrate = compare_carbohydrate()
    per_proteins, proteins = compare_proteins()
    per_fat, fat = compare_fat()
    per_dietary_fiber, dietary_fiber = compare_dietary_fiber()
    per_sodium, sodium = compare_sodium()
    per_sodium_chloride_equivalent, sodium_chloride_equivalent = compare_sodium_chloride_equivalent()
    per_potassium, potassium = compare_potassium()
    per_calcium, calcium = compare_calcium()
    per_iron, iron = compare_iron()
    per_magnesium, magnesium = compare_magnesium()
    per_phosphorus, phosphorus = compare_phosphorus()
    per_vitamin_A, vitamin_A = compare_vitamin_A()
    per_vitamin_B1, vitamin_B1 = compare_vitamin_B1()
    per_vitamin_B2, vitamin_B2 = compare_vitamin_B2()
    per_vitamin_B6, vitamin_B6 = compare_vitamin_B6()
    per_vitamin_B12, vitamin_B12 = compare_vitamin_B12()
    per_niacin, niacin = compare_niacin()
    per_vitamin_C, vitamin_C = compare_vitamin_C()
    per_vitamin_D, vitamin_D = compare_vitamin_D()
    per_vitamin_E, vitamin_E = compare_vitamin_E()






    per_list.append(per_calories)
    per_list.append(per_carbohydrate)
    per_list.append(per_proteins)
    per_list.append(per_fat)
    per_list.append(per_dietary_fiber)
    per_list.append(per_sodium)
    per_list.append(per_sodium_chloride_equivalent)
    per_list.append(per_potassium)
    per_list.append(per_calcium)
    per_list.append(per_iron)
    per_list.append(per_magnesium)
    per_list.append(per_phosphorus)
    per_list.append(per_vitamin_A)
    per_list.append(per_vitamin_B1)
    per_list.append(per_vitamin_B2)
    per_list.append(per_vitamin_B6)
    per_list.append(per_vitamin_B12)
    per_list.append(per_niacin)
    per_list.append(per_vitamin_C)
    per_list.append(per_vitamin_D)
    per_list.append(per_vitamin_E)


    real_value_list.append(calories)
    real_value_list.append(carbohydrate)
    real_value_list.append(proteins)
    real_value_list.append(fat)
    real_value_list.append(dietary_fiber)
    real_value_list.append(sodium)
    real_value_list.append(sodium_chloride_equivalent)
    real_value_list.append(potassium)
    real_value_list.append(calcium)
    real_value_list.append(iron)
    real_value_list.append(magnesium)
    real_value_list.append(phosphorus)
    real_value_list.append(vitamin_A)
    real_value_list.append(vitamin_B1)
    real_value_list.append(vitamin_B2)
    real_value_list.append(vitamin_B6)
    real_value_list.append(vitamin_B12)
    real_value_list.append(niacin)
    real_value_list.append(vitamin_C)
    real_value_list.append(vitamin_D)
    real_value_list.append(vitamin_E)


    for i in range(len(per_list)):
        if per_list[i] > 120:
            per_list[i] == 120
        else:
            pass

    per_dict = {
        "calories": per_list[0],
        "carbohydrate": per_list[1],
        "proteins": per_list[2],
        "fat": per_list[3],
        "dietary_fiber": per_list[4],
        "sodium": per_list[5],
        "sodium_chloride_equivalent": per_list[6],
        "potassium": per_list[7],
        "calcium": per_list[8],
        "iron": per_list[9],
        "magnesium": per_list[10],
        "phosphorus": per_list[11],
        "vitamin_A": per_list[12],
        "vitamin_B1": per_list[13],
        "vitamin_B2": per_list[14],
        "vitamin_B6": per_list[15],
        "vitamin_B12": per_list[16],
        "niacin": per_list[17],
        "vitamin_C": per_list[18],
        "vitamin_D": per_list[19],
        "vitamin_E": per_list[20]
    }


    real_value_dict = {
        "calories": real_value_list[0],
        "carbohydrate": real_value_list[1],
        "proteins": real_value_list[2],
        "fat": real_value_list[3],
        "dietary_fiber": real_value_list[4],
        "sodium": real_value_list[5],
        "sodium_chloride_equivalent": real_value_list[6],
        "potassium": real_value_list[7],
        "calcium": real_value_list[8],
        "iron": real_value_list[9],
        "magnesium": real_value_list[10],
        "phosphorus": real_value_list[11],
        "vitamin_A": real_value_list[12],
        "vitamin_B1": real_value_list[13],
        "vitamin_B2": real_value_list[14],
        "vitamin_B6": real_value_list[15],
        "vitamin_B12": real_value_list[16],
        "niacin": real_value_list[17],
        "vitamin_C": real_value_list[18],
        "vitamin_D": real_value_list[19],
        "vitamin_E": real_value_list[20]
    }



    return food_name, per_dict, real_value_dict