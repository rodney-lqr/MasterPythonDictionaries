# Creating a dictionary of universities

# University One
university1 = {
    "name": "University of the Philippines Diliman",
    "location": "Quezon City",
    "established": 1908,
    "ranking": 1,
}

# University Two
university2 = {
    "name": "Ateneo de Manila University",
    "location": "Quezon City",
    "established": 1859,
    "ranking": 2,
}

# University Three
university3 = {
    "name": "De La Salle University",
    "location": "Manila",
    "established": 1911,
    "ranking": 3,
}

# University Four
university4 = {
    "name": "University of Santo Tomas",
    "location": "Manila",
    "established": 1611,
    "ranking": 4,
}

university5 = {
    "name": "Mapúa University",
    "location": "Manila",
    "established": 1925,
    "ranking": 5,
}

allUniversities = (university1, university2, university3, university4, university5)

for i, universities in enumerate(allUniversities):
    print(f"University {i+1}: {universities}")