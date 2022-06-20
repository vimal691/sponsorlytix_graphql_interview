from fastapi import FastAPI
from schema import schema
from starlette.graphql import GraphQLApp


app=FastAPI()

app.add_route('/products', GraphQLApp(schema=schema))


@app.get('/')
async def index():
    return {"message": "Hi This is the root page. To get started go to http://127.0.0.1:8000/products"}