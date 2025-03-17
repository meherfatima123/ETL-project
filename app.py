from flask import Flask, jsonify
from faker import Faker
import random
'''Faker is a Python package that generates fake data for you. Whether 
you need to bootstrap your database, create good-looking XML documents,
 fill-in your persistence to stress test it,
 or anonymize data taken from a production service, Faker is for you.'''

app = Flask(__name__)
fake = Faker()

pizza_data = {
    "Margherita": ["Tomato", "Mozzarella", "Basil"],
    "Pepperoni": ["Pepperoni", "Mozzarella", "Tomato Sauce"],
    "Hawaiian": ["Ham", "Pineapple", "Mozzarella", "Tomato Sauce"],
    "Vegetarian": ["Mushrooms", "Bell Peppers", "Onions", "Olives", "Tomato Sauce", "Mozzarella"],
    "BBQ Chicken": ["BBQ Chicken", "Red Onions", "Mozzarella", "BBQ Sauce"],
    "Meat Lovers": ["Pepperoni", "Sausage", "Bacon", "Ham", "Ground Beef", "Mozzarella", "Tomato Sauce"],
    "Supreme": ["Pepperoni", "Sausage", "Green Peppers", "Onions", "Black Olives", "Mushrooms", "Mozzarella", "Tomato Sauce"],
    "Mushroom": ["Mushrooms", "Mozzarella", "Tomato Sauce"],
    "Neapolitan": ["San Marzano Tomatoes", "Mozzarella", "Basil", "Extra Virgin Olive Oil"],
    "Buffalo Chicken": ["Buffalo Chicken", "Blue Cheese", "Mozzarella", "Buffalo Sauce"],
    "Pesto Chicken": ["Grilled Chicken", "Pesto Sauce", "Mozzarella", "Sun-Dried Tomatoes"],
    "Spinach and Feta": ["Spinach", "Feta Cheese", "Mozzarella", "Tomato Sauce"],
    "White Pizza": ["Ricotta Cheese", "Garlic", "Mozzarella", "Olive Oil", "Italian Herbs"],
    "Barbecue Bacon": ["Bacon", "Red Onion", "Barbecue Sauce", "Mozzarella"],
    "Artichoke and Spinach": ["Artichoke Hearts", "Spinach", "Mozzarella", "Garlic", "Parmesan Cheese"],
    "Four Cheese": ["Mozzarella", "Ricotta", "Parmesan", "Gorgonzola"],
    "Chicken Alfredo": ["Grilled Chicken", "Alfredo Sauce", "Mozzarella", "Garlic"],
    "Taco Pizza": ["Seasoned Ground Beef", "Cheddar Cheese", "Lettuce", "Tomato", "Salsa", "Sour Cream"],
    "Philly Cheesesteak": ["Shaved Steak", "Onions", "Peppers", "Mozzarella", "Cheese Sauce"],
    "BBQ Bacon Cheeseburger": ["Ground Beef", "Bacon", "Cheddar Cheese", "Onions", "Pickles", "BBQ Sauce", "Mozzarella"],
    "Greek Pizza": ["Feta Cheese", "Kalamata Olives", "Tomato", "Red Onion", "Cucumber", "Tzatziki Sauce", "Mozzarella"],
    "Buffalo Cauliflower": ["Roasted Cauliflower", "Buffalo Sauce", "Blue Cheese", "Mozzarella"],
    "Mac and Cheese Pizza": ["Macaroni", "Cheddar Cheese Sauce", "Bacon", "Mozzarella"],
    "Capricciosa": ["Ham", "Mushrooms", "Artichokes", "Olives", "Tomato Sauce", "Mozzarella"],
    "Seafood Pizza": ["Shrimp", "Calamari", "Mussels", "Clams", "Garlic", "Tomato Sauce", "Mozzarella"],
    "Tandoori Chicken": ["Tandoori Chicken", "Onions", "Bell Peppers", "Tomatoes", "Mozzarella"],
    "BBQ Ranch Chicken": ["Grilled Chicken", "Bacon", "Red Onion", "BBQ Sauce", "Ranch Dressing", "Mozzarella"],
    "Margarita": ["Mozzarella", "Tomato", "Basil", "Olive Oil"],
    "Sicilian": ["Tomato Sauce", "Mozzarella", "Olive Oil", "Oregano"],
    "Calzone": ["Ricotta Cheese", "Mozzarella", "Pepperoni", "Tomato Sauce"],
    "Meatball": ["Meatballs", "Mozzarella", "Parmesan", "Tomato Sauce"],
    "Veggie Delight": ["Broccoli", "Spinach", "Mushrooms", "Onions", "Peppers", "Tomato Sauce", "Mozzarella"]
}

pizza_sizes = ["Small", "Medium", "Large"]

def generate_fake_pizza():
    pizza_name = random.choice(list(pizza_data.keys()))
    toppings = random.sample(pizza_data[pizza_name], k=random.randint(1, len(pizza_data[pizza_name])))
    return {
        "name": pizza_name + " Pizza",
        "toppings": toppings,
        "size": random.choice(pizza_sizes),
        "price": round(random.uniform(5, 15), 2)
    }

@app.route('/', methods=['GET'])
def get_fake_pizzas():
    pizzas = [generate_fake_pizza() for _ in range(10)]
    return jsonify(pizzas)

if __name__ == '__main__':
    app.run()
