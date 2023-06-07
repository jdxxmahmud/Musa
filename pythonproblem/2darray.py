#problem - Problem: Create a function that takes a list of dictionaries and returns the sum of people’s budgets.

def get_budget(lst):
    total = 0 
    for i in range(0, len(lst)):
         total = total + lst[i]['budget']

    return total 

arr_one = [
{ "name": "John", "age": 21, "budget": 23000 },
{ "name": "Steve", "age": 32, "budget": 40000 },
{ "name": "Martin", "age": 16, "budget": 2700 }
]

arr_two = [
{ "name": "John", "age": 21, "budget": 29000 },
{ "name": "Steve", "age": 32, "budget": 32000 },
{ "name": "Martin", "age": 16, "budget": 1600 }
]

print(get_budget(arr_one))
print(get_budget(arr_two))