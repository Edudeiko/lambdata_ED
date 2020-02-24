"""Part 1, organize product"""

import random


class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
                    self.name = name
                    self.price = price
                    self.weight = weight
                    self.flammability = flammability
                    self.identifier = identifier

# ```python
# >>> from acme import Product
# >>> prod = Product('A Cool Toy')
# >>> prod.name
# 'A Cool Toy'
# >>> prod.price
# 10
# >>> prod.weight
# 20
# >>> prod.flammability
# 0.5
# >>> prod.identifier
# 2812086  # your value will vary
# ```
# success!!!

# """Part 2, add two methods"""

    def stealability(self):
        pricevsweight = self.price/self.weight
        if pricevsweight < 0.5:
            return f"Not so stealable..."
        elif pricevsweight < 1:
            return f"Kinda stealable."
        else:
            return f"Very stealable!"

    def explode(self):
        boom = self.flammability*self.weight
        if boom < 10:
            return f"...fizzle."
        elif boom < 50:
            return f"...boom!"
        else:
            return f"...BABOOM!!"

# ```python
# >>> from acme import Product
# >>> prod = Product('A Cool Toy')
# >>> prod.stealability()
# 'Kinda stealable.'
# >>> prod.explode()
# '...boom!'
# ``` 
# success!!!

# Part 3 - A Proper Inheritance

class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
    #   super().__init__(name, price, weight, flammability)
                 identifier=random.randint(1000000, 9999999)):
                    self.name = name
                    self.price = price
                    self.weight = weight
                    self.flammability = flammability
                    self.identifier = identifier

    def explode(self):
        return f"...it's a glove."

    def punch(self):
        if self.weight < 5:
            return f'That tickles.'
        elif self.weight < 15:
            return f'Hey that hurt!'
        else:
            return f'OUCH!'

# ```python
# >>> from acme import BoxingGlove
# >>> glove = BoxingGlove('Punchy the Third')
# >>> glove.price
# 10
# >>> glove.weight
# 10
# >>> glove.punch()
# 'Hey that hurt!'
# >>> glove.explode()
# "...it's a glove."
# ```
# success!!!