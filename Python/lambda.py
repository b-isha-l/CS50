people = [
    {"name": "Isha", "house": "Nowhere"},
    {"name": "Shiva", "house": "Elsewhere"},
    {"name": "Shakti", "house": "Everywhere"}
]

# def f(person):
#     return person["name"]

# people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)