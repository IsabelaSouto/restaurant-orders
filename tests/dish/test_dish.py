import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish = Dish("Lasagna", 25.50)
    assert isinstance(dish, Dish)
    assert dish.name == "Lasagna"
    assert dish.price == 25.50

    with pytest.raises(TypeError):
        Dish("Lasagna", "vinte")

    with pytest.raises(TypeError):
        Dish("Lasagna", None)

    with pytest.raises(ValueError):
        Dish("Lasagna", -10.00)

    assert repr(dish) == "Dish('Lasagna', R$25.50)"

    dish2 = Dish("Lasagna", 25.50)
    dish3 = Dish("Pizza", 30.00)

    assert dish == dish2
    assert dish != dish3
    assert dish == dish

    assert hash(dish) == hash(dish2)
    assert hash(dish) != hash(dish3)

    ingredient = Ingredient("queijo mussarela")
    dish.add_ingredient_dependency(ingredient, 200)
    assert dish.recipe.get(ingredient) == 200

    assert dish.get_ingredients() == {ingredient}

    expected_restrictions = ingredient.restrictions
    assert dish.get_restrictions() == expected_restrictions

    with pytest.raises(TypeError):
        Dish("Lasanha", "invalid_price")

    with pytest.raises(ValueError):
        Dish("Lasanha", -10.00)

    invalid_ingredient = Ingredient("nonexistent ingredient")
    assert dish.recipe.get(invalid_ingredient) is None
