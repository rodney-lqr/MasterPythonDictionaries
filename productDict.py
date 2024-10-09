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


#Changing the price of product number four
product4["price"] = 70
print("\nUpdated Product 4:")
print(product4)


#Accessing the quantity of product number five
print("\nQuantity of Product 5:", product5["quantity"])


#Adding a model to the dictionary of products
product1["model"] = "Dell XPS 15"
product2["model"] = "Acer Nitro 5"
product3["model"] = "Sony WH-1000XM3"
product4["model"] = "Logitech G733"
product5["model"] = "Razer DeathAdder"

print("\nUpdated Products:")

for i, product in enumerate(allProduct):
    print(f"Product {i+1}: {product}")