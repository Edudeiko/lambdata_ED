"""Part 4 - Class Report"""

from random import randint, sample, uniform
from acme import Product

# Important to Capitalize
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + '' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price=price, weight=weight,
                                flammability=flammability))

    return products


def inventory_report(products):
    unique_names = set()
    total_price = 0
    total_weight = 0
    total_flammability = 0.0
    for product in products:
        unique_names.add(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:', len(unique_names))
    print('Average price:', total_price/len(products))
    print('Average weight:', total_weight/len(products))
    print('Average flammability:', total_flammability/len(products))

if __name__ == '__main__':
    inventory_report(generate_products())


# ```
# $ python acme_report.py 
# ACME CORPORATION OFFICIAL INVENTORY REPORT
# Unique product names: 19
# Average price: 56.8
# Average weight: 54.166666666666664
# Average flammability: 1.258097155966675
# ```