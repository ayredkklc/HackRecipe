from py_edamam import PyEdamam, Edamam
import random
e = Edamam()
'''data = e.search_recipe("onion")
hits_dictionary = data['hits']'''
foodname = input('What food are you craving? ')

numberOfIngredients = int(input('Enter the total number of ingredients you want to use: '))
yourIngredients = []
for i in range(numberOfIngredients):
    yourIngredients.append(input("Enter the ingredients that you want to use : "))

data = e.search_recipe(foodname)
hits_dictionary = data['hits']


# numbr= input('how many recipes d o')


#yourIngredients = [item for item in input("Enter the ingredients that you want to use : ").split()]


#youringredients = re.split(' |,', youringredients)

def list_recipes():

    data = e.search_recipe(foodname)
    hits_dictionary = data['hits']

    recipeList = []


    for hit in hits_dictionary:
        recipe_dictionary = hit['recipe']

        ing = recipe_dictionary['ingredients']
        count = 0
        recipe = []
        for i in range(len(ing)):
            if ing[i]['text'] not in recipe:
                recipe.append(ing[i]['text'])
                # count += 1

        for x in yourIngredients:
            for y in range(len(recipe)):
                if x in recipe[y]:
                    count += 1
                    break
                else:
                    continue

        if count == len(yourIngredients):
            print()
            #print(recipe_dictionary['label'])
            recipeList.append(recipe_dictionary)

            '''for i in recipe:
                print(i)'''

    return recipeList




def by_calories(rlist,  calories):
    print('Recipes that match your ingredient ')
    print()
    for i in range(len(rlist)):
        current = rlist[i]
        if current['calories'] > calories:
            rlist.remove(rlist[i])
        else:
            ing = current['ingredients']
            print(current["label"])
            print()
            recipe = []
            for i in range(len(ing)):
                if ing[i]['text'] not in recipe:
                    recipe.append(ing[i]['text'])
            for i in recipe:
                print(i)
            print()
            print("Calories: ", current['calories'])
            print()
    return rlist



def list_recipes_print():
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








'''yes_no = int(input("Do you have any clories limit: press 1 for yes 2 for no"))
#we can make it better but for now im just testing
if(yes_no == 1):
    myCalories = int(input("Enter the max amount of calories you want: "))
    ex = list_recipes()
    print()
    by_calories(ex, myCalories)
else:
    list_recipes_print()'''



def restaurant_roulette():
    list = ["McDonald's", "Burger King", "Taco bell", "Subway", "Popeye’s", "Panda Express", "Wendy’s", "Pizza Hut", "Arby’s"]
    print(random.choice(list))


def recipe_roulette(rlist):
    random_recipe = random.choice(rlist)

    ing = random_recipe['ingredients']
    print(random_recipe["label"])
    print()
    recipe = []
    for i in range(len(ing)):
        if ing[i]['text'] not in recipe:
            recipe.append(ing[i]['text'])
    for i in recipe:
        print(i)
    print()
    print("Calories: ", random_recipe['calories'])
    print()


ex = list_recipes()
recipe_roulette(ex)

#random_restaurant_pick()

def diet_preference(rlist):
    count = 0
    print("Here are our diet labels: “vegan”, “vegetarian”, “paleo”, “dairy-free”, “gluten-free”, “wheat-free”, “fat-free”, “low-sugar”, “egg-free”, “peanut-free”, “tree-nut-free”, “soy-free”, “fish-free”, “shellfish-free” ")
    user_diet_label = input('Which health label are you looking for? ')
    print()
    print('Recipes that match your diet preference ')
    print()
    for i in range(len(rlist)):
        recipe_dictionary = rlist[i]
        for dietLabel in recipe_dictionary['dietLabels']:
            if dietLabel == user_diet_label:

                ing = recipe_dictionary['ingredients']
                print(recipe_dictionary["label"])
                print()
                recipe = []
                for i in range(len(ing)):
                    if ing[i]['text'] not in recipe:
                        recipe.append(ing[i]['text'])
                for i in recipe:
                    print(i)
                print()
                print("Diet labels: ", recipe_dictionary['dietLabels'])
                print()
                count += 1
    if count == 0:
        print("doesn't exist.")
    return

diet_preference(ex)