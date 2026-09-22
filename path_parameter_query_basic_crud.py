# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class User(BaseModel):
#     name: str
#     age: int 
#     email : str

# @app.get("/")
# def home():
#     return {"message": "Welcome to the FastAPI application!"}



# @app.get("/about")
# def about():
#     return {"message": "This is a simple FastAPI application."}


# #path paremter example

# @app.get("/user/{user_id}")
# def get_user(user_id : int )-> dict:
#     return {"user id": user_id , "message" : f"User with id {user_id} has been retrieved successfully."}


# #answer path parameter : path parameter is a variable that is part of the URL path and is used to capture values from the URL. In FastAPI, you can define path parameters by including them in the route path using curly braces {}. For example, in the route "/user/{user_id}", "user_id" is a path parameter that captures the value provided in the URL when making a request to that endpoint.

# # query parameter example

# #/users?user=jon doe

# @app.get("/query")
# def get_query(user: str = None)->dict:
#     return {"user":user, "message": f"Query parameter received: {user}"} 

# #diff in path parameter and query parameter : Path parameters are part of the URL path and are used to capture values from the URL, while query parameters are included in the URL after a question mark (?) and are used to pass additional data to the server. Path parameters are typically required, while query parameters are optional.


# @app.get("/product")
# def get_product(product_id : int = 100 ) -> dict:
#     return {"product": product_id, "message": f"Product ID received: {product_id}"}


# #multiple query parameters example

# @app.get("/items")
# def get_items(name :str = None, price : int = 0 ) ->dict:
#     return {"name": name, "price": price, "message": f"Item with name {name} and price {price} has been retrieved successfully."}



# #post api
# # @app.post("/create-user")
# # def create_user(name:str , age:int) -> dict:
# #     return {
# #         "name": name,
# #         "age": age,
# #         "message": f"User with name {name} and age {age} has been created successfully." # we are returning a dictionary with the name, age, and a message indicating that the user has been created successfully.  
# #     }

# @app.post("/create-user")
# def create_user(user: User)->dict:
#     return {
#         "message": "User created successfully.",
#         "data": user  #in this one we are doing the same thing but we are using a dictionary to pass the data instead of individual parameters. This allows us to pass more complex data structures and makes it easier to handle the data in the backend.
#     }


# #now nested model example

# class Address(BaseModel):
#     city: str
#     pincode : int


# class UserWithAddress(BaseModel):
#     name: str
#     age: int
#     address: Address


# @app.post("/create-user-with-address")
# def create_user_with_address(user: UserWithAddress) -> dict:
#     return {
#         "message": "User with address created successfully.",
#         "name": user.name,
#         "age": user.age,
#         "address": {
#             "city": user.address.city,
#             "pincode": user.address.pincode
#         }
#     }   
