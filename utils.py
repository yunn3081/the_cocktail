import requests
import json

#取得cocktail的ingredients並整理成string，方便輸出
def print_ingredient(ingredient_list, p):
    ingredients_list_string = ''
    #利用迴圈跑ingredient_list以建立string
    for i in range(len(ingredient_list[p])):
        if i != len(ingredient_list[p]) - 1:
            ingredients_list_string += 'Ingredient ' + str(i + 1) + ': ' + ingredient_list[p][i] + '\n' #如果不是最後一位，就要加空格
        else:
            ingredients_list_string += 'Ingredient ' + str(i + 1) + ': ' + ingredient_list[p][i] #如果是最後一位，就不要加空格
    return ingredients_list_string #回傳整理好的string

#取得cocktails的list位置及instruction
def find_cocktail_spot(cocktail_list, instruction_list, cocktail):
    p = cocktail_list.index(cocktail) #取得cocktail在cocktail list中的位置
    return p, instruction_list[p] #回傳位置及其instruction

#整理data
#category表示基酒種類
def build_list(category):
    f = r"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + category #取得API連結
    data = requests.get(f) #使用requests產生http請求
    tt = json.loads(data.text) #下載檔案

    cocktail_list = [] #建立cocktail list
    instruction_list = [] #建立instruction list
    ingredient_list = [] #建立ingredient list

    for i in (tt['drinks']):
        cocktail_list.append(i['strDrink']) #append cocktail name
        instruction_list.append(i['strInstructions']) #append instruction
        ingredient = []
        #append ingredients
        if i['strIngredient1']:
            ingredient.append(i['strIngredient1'])
        if i['strIngredient2']:
            ingredient.append(i['strIngredient2'])
        if i['strIngredient3']:
            ingredient.append(i['strIngredient3'])
        if i['strIngredient4']:
            ingredient.append(i['strIngredient4'])
        if i['strIngredient5']:
            ingredient.append(i['strIngredient5'])
        if i['strIngredient6']:
            ingredient.append(i['strIngredient6'])
        if i['strIngredient7']:
            ingredient.append(i['strIngredient7'])
        if i['strIngredient8']:
            ingredient.append(i['strIngredient8'])
        if i['strIngredient9']:
            ingredient.append(i['strIngredient9'])
        if i['strIngredient10']:
            ingredient.append(i['strIngredient10'])
        if i['strIngredient11']:
            ingredient.append(i['strIngredient11'])
        if i['strIngredient12']:
            ingredient.append(i['strIngredient12'])
        if i['strIngredient13']:
            ingredient.append(i['strIngredient13'])
        if i['strIngredient14']:
            ingredient.append(i['strIngredient14'])
        if i['strIngredient15']:
            ingredient.append(i['strIngredient15'])

        ingredient_list.append(ingredient) #將ingredient推入ingredient list
    return cocktail_list, instruction_list, ingredient_list #回傳所有整理好的資訊

def cocktails(categories, cocktails):

    cocktails_list, instructions_list, ingredients_list = build_list(categories) #整理data
    cocktail_spot, cocktail_instruction = find_cocktail_spot(cocktails_list, instructions_list, cocktails) #取得cocktails的list位置及instruction
    ingredients_list_string = print_ingredient(ingredients_list, cocktail_spot) #取得cocktail的ingredients並整理成string，方便輸出

    return cocktail_instruction, ingredients_list_string #回傳instruction及ingredients(The Cocktails會用到)