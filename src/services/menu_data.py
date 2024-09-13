import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str) -> None:
        dishes_dict = {}

        with open(source_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            for row in reader:
                dish_name, price, ingredient_name, quantity = row
                price = float(price)
                quantity = int(quantity)

                if dish_name not in dishes_dict:
                    dish = Dish(dish_name, price)
                    dishes_dict[dish_name] = dish
                else:
                    dish = dishes_dict[dish_name]

                ingredient = Ingredient(ingredient_name)

                dish.add_ingredient_dependency(ingredient, quantity)

        self.dishes = set(dishes_dict.values())
