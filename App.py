from fastapi import FastAPI , Request
from mockdata import products
app = FastAPI()

#@get. is used for sending request to get the fetch data we want
@app.get("/")
def get_root():

    return {"message": "FastApi Initialized"}

@app.get("/products")
def get_products():
    return products

#Path Params# you have to describe their type too#
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct

    return{
        "Error":"Product not found for this ID."
    }

#query params# 
@app.get("/greet")
def greet(request:Request):
    query_params = dict(request.query_params)
    print(query_params)
    return {
        "greet": f" Hello {query_params.get("name")},Your age is {query_params.get("age")} "
    }
