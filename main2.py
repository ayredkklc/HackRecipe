from py_edamam import PyEdamam, Edamam

e = Edamam()
'''data = e.search_recipe("onion")
hits_dictionary = data['hits']'''
ingredientWeHave = input('Which ingredients do you have? ')

yourIngredients = [item for item in input("Enter the ingredients that you want to use : ").split()]

#numbr= input('how many recipes d o')
print('Recipes that match your ingredient ')
print()


def list_recipes():
    data = e.search_recipe(ingredientWeHave)
    hits_dictionary = data['hits']

    for hit in hits_dictionary:
        recipe_dictionary = hit['recipe']
        print(recipe_dictionary['label'])

        ing = recipe_dictionary['ingredients']
        count = 0

        recipe = [0] * len(ing)
        for i in range(len(ing)):
            recipe[i] = ing[i]['text']
            count += 1
            print(recipe[i])
        #if(count <= numberOfIngredients):


        print()

        '''for ing in recipe_dictionary['ingredients']:
            ing = recipe_dictionary['ingredients']'''

        '''if ingredientwehave.input in ing:
            print
            "found"'''

        #print(ing)
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