from collections import namedtuple

Products = namedtuple("Products", ['id', 'name', 'price', 'category'])

data = {
    1: Products(1, "Apple",         50,     1),
    2: Products(2, "Banana",        20,     1),
    3: Products(3, "Orange",        15,     1),
    4: Products(4, "Shirt",         120,    2),
    5: Products(5, "Short",         100,    2),
    6: Products(6, "Sock",          20,     2),
    7: Products(7, "Chocolate",     80,     3),
    8: Products(8, "Chips",         85,     3),
    9: Products(9, "Pink Candy",    60,     3),
}