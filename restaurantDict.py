# Creating a dictionary of restaurants

# Restaurant One
restaurant1 = {
    "name": "The Gourmet Kitchen",
    "cuisine": "French",
    "location": "New York City",
    "rating": 4.8,
}

# Restaurant Two
restaurant2 = {
    "name": "Sushi Paradise",
    "cuisine": "Japanese",
    "location": "Los Angeles",
    "rating": 4.6,
}

# Restaurant Three
restaurant3 = {
    "name": "Pasta Heaven",
    "cuisine": "Italian",
    "location": "Chicago",
    "rating": 4.7,
}

# Restaurant Four
restaurant4 = {
    "name": "Taco Fiesta",
    "cuisine": "Mexican",
    "location": "Austin",
    "rating": 4.5,
}

# Restaurant Five
restaurant5 = {
    "name": "Burger Barn",
    "cuisine": "American",
    "location": "Dallas",
    "rating": 4.4,
}

allRestaurants = (restaurant1, restaurant2, restaurant3, restaurant4, restaurant5)

for i, restaurant in enumerate(allRestaurants):
    print(f"Restaurant {i+1}: {restaurant}")