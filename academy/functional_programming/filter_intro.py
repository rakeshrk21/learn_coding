menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

print("-" * 40)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

print("-" * 40)


def meals_without_spam(mean_list):
    return "spam" not in mean_list


print("-" * 40)
my_meals = list(filter(meals_without_spam, menu))
print(my_meals)