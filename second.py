from py_edamam import PyEdamam, Edamam

e = Edamam()

foodname = input('What food are you craving? ')
numberOfIngredients = int(input('Enter the total number of ingredients you want to use: '))
yourIngredients = []
for i in range(numberOfIngredients):
    yourIngredients.append(input("Enter the ingredients that you want to use : "))
data = e.search_recipe(foodname)
hits_dictionary = data['hits']


def list_recipes():
    recipecount = 0
    print('Recipes that match your ingredient ')
    print()
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

            print(recipe_dictionary['label'])
            recipecount += 1
            for i in recipe:
                print(i)
    if recipecount == 0:
        print("dont exist.")
    return


def allergies():
    count = 0
    print("Here are our diet labels: “balanced”, “high-protein”, “high-fiber”, “low-fat”, “low-carb”, “low-sodium” ")
    user_health_label = input('Which health label are you looking for? ')
    print()
    print('Recipes that match health preference ')
    print()
    for hit in hits_dictionary:

        recipe_dictionary = hit['recipe']
        for healthLabel in recipe_dictionary['healthLabels']:
            if healthLabel == user_health_label:
                print(recipe_dictionary['label'])
                count += 1
    if count == 0:
        print("dont exist.")
    return


def diet_preference():
    count = 0
    print("Here are our diet labels: “vegan”, “vegetarian”, “paleo”, “dairy-free”, “gluten-free”, “wheat-free”, “fat-free”, “low-sugar”, “egg-free”, “peanut-free”, “tree-nut-free”, “soy-free”, “fish-free”, “shellfish-free” ")
    user_diet_label = input('Which health label are you looking for? ')
    print()
    print('Recipes that match your diet preference ')
    print()
    for hit in hits_dictionary:
        recipe_dictionary = hit['recipe']
        for dietLabel in recipe_dictionary['dietLabels']:
            if dietLabel == user_diet_label:
                print(recipe_dictionary['label'])
                count += 1
    if count == 0:
        print("dont exist.")
    return


def calorie_preferences():
    calorieAmount = int(input("Enter the max calorie amount you want to consume"))
    print('Recipes that match your calorie preference ')
    print()
    count = 0
    for hit in hits_dictionary:
        recipe_dictionary = hit['recipe']
        caloriesInRecipe = recipe_dictionary["calories"]
        if(caloriesInRecipe <= calorieAmount):
            ing = recipe_dictionary['ingredients']
            print(recipe_dictionary['label'])
            print()
            recipe = []
            for i in range(len(ing)):
                if ing[i]['text'] not in recipe:
                    recipe.append(ing[i]['text'])
            for i in recipe:
                print(i)
            print()
            print("Calories: ", recipe_dictionary['calories'])
            print()
            count += 1
    if count == 0:
        print("dont exist.")
    return


def number_ingredient_recipies():
    ingredientAmount = int(input("Enter the amount of ingredients you want to use "))
    print('Recipes that match your ingredient amount preference ')
    print()
    count = 0
    for hit in hits_dictionary:
        recipe_dictionary = hit['recipe']
        ing = recipe_dictionary['ingredients']
        recipe = []
        for i in range(len(ing)):
            if ing[i]['text'] not in recipe:
                recipe.append(ing[i]['text'])
        if len(ing) == ingredientAmount:
            print(recipe_dictionary['label'])
            count += 1
    if count == 0:
        print("dont exist.")
    return




calorie_preferences()
#diet_preference()
#list_recipes()


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