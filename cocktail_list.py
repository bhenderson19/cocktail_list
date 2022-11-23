import requests

def getCocktails(ingredients):
    BASE_URL = "http://www.thecocktaildb.com/api/json/v1/"
    API_KEY = "1"
    cocktails=[[] for i in range(len(ingredients))]
    all=set()
    i=0
    valid=True
    for ingredient in ingredients:
        URL = BASE_URL + API_KEY + "/filter.php?i=" + ingredient

        response = requests.get(URL)
        if response.status_code == 200:
            try:
                main=response.json()['drinks']
                for drink in main:
                    cocktails[i].append(drink.get('strDrink'))
                    all.add(drink.get('strDrink'))
            except:
                all = ["Not a valid Ingredient"]
                valid=False
        else:
            cocktails = ["error"]
        i+=1

    if valid:
        for list in cocktails:
            all = set.intersection(all,set(list))

    if len(all) == 0:
        print("testing")
        all={"No Cocktails :("}
    
    return all