from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Testa se a classe pode ser instanciada corretamente
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("bacon")
    ingredient4 = Ingredient("água")

    # Verifica se o atributo name é atribuído corretamente
    assert ingredient1.name == "queijo mussarela"
    assert ingredient3.name == "bacon"

    # Verifica se o atributo restrictions é populado corretamente
    assert ingredient1.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }
    assert ingredient3.restrictions == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED
    }
    assert ingredient4.restrictions == set()

    # Testa o método mágico __repr__
    assert repr(ingredient1) == "Ingredient('queijo mussarela')"
    assert repr(ingredient3) == "Ingredient('bacon')"

    # Testa o método mágico __eq__
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    # Testa o método mágico __hash__
    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
