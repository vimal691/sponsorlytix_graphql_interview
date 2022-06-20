from graphene import (
    ObjectType,
    String,
    Int,
    Field,
    Schema,
    List
)

from models import data

"""
    class ProductType:
        id:int
        name:str
        price:int
        category:int
"""


class ProductsType(ObjectType):
    id = Int()
    name = String()
    price = Int()
    category = Int()

    # resolvers
    def resolve_id(products, info):
        return products.id

    def resolve_name(products, info):
        return products.name

    def resolve_price(products, info):
        return products.price

    def resolve_category(products, info):
        return products.category


class Query(ObjectType):
    product_overview = List(ProductsType)
    product_details = Field(ProductsType, key=Int())
    products_by_category = List(ProductsType, key=Int())

    def resolve_product_overview(root, info):
        return data.values()

    def resolve_product_details(root, info, key):
        return data[key]

    def resolve_products_by_category(root, info, key):
        result = []
        for x in data:
            if data[x].category == key:
                result.append(data[x])
        return result



# schema
schema = Schema(query=Query)


# #query
# query_string="{allProducts{id name price category}}"

# print(schema.execute(query_string))