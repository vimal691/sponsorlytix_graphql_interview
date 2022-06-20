About Code and pre-requisite:

    1. From folder graphql_fastapi_python problem run `pipenv shell`. 
    This will create a virtual environment.
    2. Now run `pip install requirements.txt`. This will install all the
    dependencies for the project
    3. Quick Explanation: code is divided into Model, Schema, Server(main)
        i) model.py file contain db right now. But generally it will have
            db connection code.
        ii) schema.py file contains definition and interaction with db.
        iii) server or main.py will create fastapi and routing.

To run code:

    1. go to assignment folder and type `uvicorn main:app --reload` 
    in terminal and press enter
    2. click on link `http://127.0.0.1:8000` and go to products endpoint
        `http://127.0.0.1:8000/products`
    3. write following query for each of the senarios
        i). ProductDetails return single product. 
            Query an Id of product to filter.

            query{
              productDetails(key:9){
                id
                name
                price
                category	
              }
            }
        ii). ProductOverview
            
            query{
              productOverview{
                id
                name
                price
                category
              }
            }

            
        iii). ProductsByCategory return the products of specific category. 
            Require category Id to filter.

            query{
              productsByCategory(key: 3) {
                id
                name
                price
              }
            }
