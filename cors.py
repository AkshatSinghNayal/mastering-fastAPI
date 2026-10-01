# Import FastAPI.
# FastAPI is the framework we use to create our API.
from fastapi import FastAPI


# Import CORSMiddleware.
#
# CORS = Cross-Origin Resource Sharing
#
# It allows a frontend running on a different origin
# (for example, localhost:5173) to communicate with
# our FastAPI backend (for example, localhost:8000).
from fastapi.middleware.cors import CORSMiddleware


# Create the FastAPI application.
#
# "app" is the main object that we use to create
# routes/endpoints and configure our API.
app = FastAPI()


# ---------------------------------------------------------
# CORS CONFIGURATION
# ---------------------------------------------------------

# List of frontend origins that are allowed to access
# our FastAPI backend.
#
# An "origin" consists of:
#
#     protocol + domain + port
#
# Example:
#
#     http://localhost:5173
#
# IMPORTANT:
# "localhost" by itself is normally not enough.
# The protocol and port should generally be included.
#
# If your frontend is running on Vite, the default
# development URL is commonly:
#
#     http://localhost:5173
#
origins = [
    "http://localhost:5173"
]


# Add CORS middleware to our FastAPI application.
#
# Middleware is code that runs around/alongside requests
# before they reach our route and/or before the response
# goes back to the client.
app.add_middleware(
    
    # Tell FastAPI that we want to use the CORS middleware.
    CORSMiddleware,

    
    # -----------------------------------------------------
    # Which origins are allowed?
    # -----------------------------------------------------
    #
    # Only origins listed in "origins" are allowed.
    #
    # In our example:
    #
    #     http://localhost:5173
    #
    # is allowed to communicate with this API.
    allow_origins=origins,


    # -----------------------------------------------------
    # Allow credentials
    # -----------------------------------------------------
    #
    # Allows the browser to include credentials such as
    # cookies in cross-origin requests.
    #
    # This is useful when your application uses
    # cookie-based authentication.
    allow_credentials=True,


    # -----------------------------------------------------
    # Which request headers are allowed?
    # -----------------------------------------------------
    #
    # "*" means allow all request headers.
    #
    # Examples of headers:
    #
    #     Content-Type
    #     Authorization
    #     Accept
    #
    allow_headers=["*"],


    # -----------------------------------------------------
    # Which HTTP methods are allowed?
    # -----------------------------------------------------
    #
    # "*" means allow all HTTP methods.
    #
    # Common HTTP methods include:
    #
    #     GET     -> retrieve data
    #     POST    -> create/send data
    #     PUT     -> update data
    #     PATCH   -> partially update data
    #     DELETE  -> delete data
    #
    allow_methods=["*"]
)


# ---------------------------------------------------------
# ROUTE / ENDPOINT
# ---------------------------------------------------------

# @app.get("/") is a FastAPI decorator.
#
# It tells FastAPI:
#
#     "When a client sends a GET request to '/',
#      execute the function immediately below."
#
# So:
#
#     GET http://localhost:8000/
#
# will call the "home()" function.
@app.get("/")
def home():

    # Return a Python dictionary.
    #
    # FastAPI automatically converts this dictionary
    # into a JSON response.
    #
    # The client will receive:
    #
    #     {
    #         "msg": "cors enabled api"
    #     }
    return {
        "msg": "cors enabled api"
    }