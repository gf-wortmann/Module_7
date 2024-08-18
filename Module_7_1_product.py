# класс Product

class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return self.name + ', ' + str(self.weight) + ', ' + self.category

    def __eq__(self, other):
        if self.name == other.name and self.weight == other.weight and self.category == other.category:
            return True
        else:
            return False


