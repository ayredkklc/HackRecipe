from py_edamam import PyEdamam, Edamam

e = Edamam()
'''data = e.search_recipe("onion")
hits_dictionary = data['hits']'''
ingredientwehave = input('Which ingredients do you have? ')
#numbr= input('how many recipies d o')
print('Recipies that match your ingredient amount')
print()


def list_recipes():
    data = e.search_recipe(ingredientwehave)
    hits_dictionary = data['hits']

    for hit in hits_dictionary:
        recipe_dictionary = hit['recipe']
        print(recipe_dictionary['label'])


        ing = recipe_dictionary['ingredients']['text']


        print(ing)
    '''for recipe in recipe_dictionary:
            ingredient_dictionary = recipe['ingredients']
            #ingredient_dictionary = ingr['ingredients']
            print(ingredient_dictionary["food"])
        print(ingredient_dictionary)'''
        #print(recipe_dictionary['ingredients'])
        #print()

def getIngredients(recipe_dictionary):
    for ingr in recipe_dictionary:
        ingredient_dictionary = ingr['ingredients']
        print(ingredient_dictionary["food"])


list_recipes()







'''print(recipe.calories)
    print(recipe.cautions, recipe.dietLabels, recipe.healthLabels)
    print(recipe.url)
    print(recipe.ingredient_quantities)'''


'''for nutrient_data in e.search_nutrient("2 egg whites"):
    print(nutrient_data)
    print(nutrient_data.calories)
    print(nutrient_data.cautions, nutrient_data.dietLabels,
          nutrient_data.healthLabels)
    print(nutrient_data.totalNutrients)
    print(nutrient_data.totalDaily)

for food in e.search_food("coffee and pizza"):
    print(food)
    print(food.category)'''
