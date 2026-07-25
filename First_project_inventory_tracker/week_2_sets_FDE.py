# # what is set? : Set cannot contain duplicate every item must be unique.

# #example :

# # ingredients = {'tomatoes', 'cheese', 'buns', 'lettuce', 'tomatoes', }

# # print(ingredients)



# # Example 2 : Membership check

# ingredients = {'tomatoes', 'cheese', 'buns', 'lettuce'}

# if 'tomatoes' in ingredients:
#     print ('tomatoes in stock')
# else:
#     print('tomatoes is not in stock')


# # Example 3 - Add and remove

# ingredients = {'tomatoes', 'cheese', 'buns'}

# # add a new ingredient

# ingredients.add('lettuce')


# # Example 4: Real UseCase

# # required = {'tomatoes', 'cheese', 'buns', 'lettuce', 'cola-syrup'}

# # in_stock = {'tomatoes', 'buns', 'lettuce'}

# # missing = required- in_stock
# # print(missing)
required = input('Required Items: ').split(' ')
set_required = set(required)
in_stock = {'tomatoes', 'buns', 'lettuce'}

def check_missing(set_required, in_stock):
    needed = set_required - in_stock
    for item in needed:
        print(f"⚠️ WARNING: {item} is missing!")
    return needed

result = check_missing(set_required, in_stock)
print("Missing items:", result)