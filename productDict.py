# Define the products dictionary

#Product Number One
product1 = {"name": "Laptop", 
            "price": 1200, 
            "quantity": 5
            }

#Product Number Two
product2 = {"name": "Monitor",
             "price": 300,
             "quantity": 8
            }

#Product Number Three
product3 = {"name": "Headphones",
             "price": 150,
             "quantity": 25
            }

#Product Number Four
product4 = {"name": "Keyboard",
            "price": 50,
            "quantity": 30
            }

#Product Number Five
product5 = {"name": "Mouse",
            "price": 30,
            "quantity": 15
            }   

allProduct = (product1, product2, product3, product4, product5)


for i, product in enumerate(allProduct):
    print(f"Product {i+1}: {product}")
