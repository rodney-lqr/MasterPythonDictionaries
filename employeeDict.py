# Creating a dictionary of employees

#Employee One
employee1 = {
    "name": "Rodney Idanan",
    "position": "Software Engineer",
    "salary": 85000,
    "experience": 5,

}

#Employee Two
employee2 = {
    "name": "Mark Walter Inductivo",
    "position": "Product Manager", 
    "salary": 95000,
    "experience": 8,

}

#Employee Three
employee3 = {
    "name": "Fiercieval Soriano", 
    "position": "UX Designer", 
    "salary": 72000,
    "experience": 4,
}

#Employee Four
employee4 = {
    "name": "Jame Kents Cano", 
    "position": "Data Analyst", 
    "salary": 68000, 
    "experience": 3
}

employee5 = {
    "name": "Roerenz Avelino",
    "position": "Marketing Specialist",
    "salary": 60000,
    "experience": 2,
}

allEmployees = (employee1, employee2, employee3, employee4, employee5)

for i, employee in enumerate(allEmployees):
    print(f"Employee {i+1}: {employee}")
