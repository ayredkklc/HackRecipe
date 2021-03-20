from py_edamam import PyEdamam, Edamam

e = Edamam()
'''data = e.search_recipe("onion")
hits_dictionary = data['hits']'''
foodname = input('What food are you craving? ')

yourIngredients = [item for item in input("Enter the ingredients that you want to use : ").split()]
numberOfIngredients = input('Enter the total number of ingredients you want to use: ')


#numbr= input('how many recipes d o')
print('Recipes that match your ingredient ')
print()


def list_recipes():
    data = e.search_recipe(foodname)
    hits_dictionary = data['hits']

    for hit in hits_dictionary:
        recipe_dictionary = hit['recipe']

        ing = recipe_dictionary['ingredients']
        count = 0
        recipe = []
        for i in range(len(ing)):
            if ing[i]['text'] not in recipe:
                recipe.append(ing[i]['text'])
                #count += 1

        for x in yourIngredients:
            for y in range(len(recipe)):
                if x in recipe[y]:
                    count+=1
                    break
                else:
                    continue

        if count == len(yourIngredients):
            print()
            print(recipe_dictionary['label'])

            for i in recipe:
                print(i)


        #if(count <= numberOfIngredients):




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