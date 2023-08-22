def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(ingredients):
    cheeses = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheeses:
            return ingredient
    return None

dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]
roll_call_dwarves(dwarves)

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
captain_planet_calls = summon_captain_planet(planeteer_calls)
print(captain_planet_calls)

short_words = ["puff", "go", "two"]
print(long_planeteer_calls(short_words))  

assorted_words = ["two", "go", "industrious", "bop"]
print(long_planeteer_calls(assorted_words))
snacks = ["crackers", "gouda", "thyme"]
print(find_the_cheese(snacks)) 

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
print(find_the_cheese(soup))  

ingredients = ["garlic", "rosemary", "bread"]
print(find_the_cheese(ingredients))  
