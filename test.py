import pytest

from main import Category, Product


@pytest.fixture
def object_category():
    return Category('револьверы', 'размер барабана')


def test_category(object_category):
    assert object_category.title == 'револьверы'
    assert object_category.description == 'размер барабана'
    assert object_category._goods == []

    product = Product('патроны', 'калибр', 1000.0, 30)
    object_category.add_products(product)

    assert Category.total_unique_products == 1
    assert object_category.display_list_products == 'патроны, 1000.0 руб. Остаток: 30 шт.'


@pytest.fixture
def object_product():
    return Product('патроны', 'калибр', 1000.0, 30)


def test_product(object_product):
    assert object_product.title == 'патроны'
    assert object_product.description == 'калибр'
    assert object_product.price == 1000.0
    assert object_product.quantity == 30


@pytest.fixture(autouse=True)
def cleanup_total():
    Category.total_categories = 0
    Category.total_unique_products = 0


def test_total():
    category = Category('револьверы', 'размер барабана')
    product = Product('патроны', 'калибр', 1000.0, 30)
    category.add_products(product)

    assert Category.total_categories == 1
    assert Category.total_unique_products == 1
