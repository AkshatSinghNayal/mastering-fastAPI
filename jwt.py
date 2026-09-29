from fastapi import FastAPI, HTTPException, Header, Depends
from jose import jwt
from datetime import datetime, timedelta, timezone


# Create the FastAPI application
app = FastAPI()


# Secret key used to SIGN and VERIFY the JWT
#
# When creating the token:
#
#     SECRET_KEY -> signs the token
#
# When verifying:
#
#     SECRET_KEY -> verifies that the token
#                   was signed with the correct key
#
# IMPORTANT:
# In a real application, don't hardcode this.
# Store it in an environment variable.
SECRET_KEY = "ABC"


# Algorithm used for signing the JWT
ALGORITHM = "HS256"


# ---------------------------------------------------------
# CREATE JWT TOKEN
# ---------------------------------------------------------

def create_token(data: dict):

    # Make a copy of the data so we don't modify
    # the original dictionary
    #
    # Example:
    #
    #     data = {"sub": "admin"}
    #
    # to_encode becomes:
    #
    #     {"sub": "admin"}
    to_encode = data.copy()


    # Create an expiration time
    #
    # datetime.now(timezone.utc)
    #     = current UTC time
    #
    # timedelta(days=30)
    #     = 30 days
    #
    # So the token will expire 30 days from now.
    expire = datetime.now(timezone.utc) + timedelta(days=30)


    # Add the expiration time to the JWT payload
    #
    # "exp" is a standard JWT claim.
    #
    # JWT libraries automatically check this when decoding
    # the token.
    to_encode.update({
        "exp": expire
    })


    # Create/sign the JWT
    #
    # to_encode
    #     = data that will be stored inside the token
    #
    # SECRET_KEY
    #     = key used to sign the token
    #
    # algorithm
    #     = signing algorithm
    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


    # Return the generated JWT string
    return token


# ---------------------------------------------------------
# LOGIN ENDPOINT
# ---------------------------------------------------------

@app.post("/login")
def login(username: str, password: str):

    # Check whether the username and password are correct
    #
    # Here we're just hardcoding the credentials for learning.
    #
    # Real applications normally check a database.
    if username != "admin" or password != "1234":

        # Stop the request and return HTTP 401
        #
        # 401 = Unauthorized
        raise HTTPException(
            status_code=401,
            detail="invalid credentials"
        )


    # Credentials are correct.
    #
    # Create a JWT containing the user's identity.
    #
    # "sub" means "subject".
    #
    # It is commonly used to store the identity/user ID
    # associated with the token.
    #
    # IMPORTANT:
    # Your original code had:
    #
    #     {"sub": str}
    #
    # That stores the Python "str" type itself.
    #
    # We want:
    #
    #     {"sub": "admin"}
    token = create_token({
        "sub": username
    })


    # Send the token back to the client
    return {
        "access_token": token
    }


# ---------------------------------------------------------
# VERIFY JWT TOKEN
# ---------------------------------------------------------

def verify_token(
    # Header(None) tells FastAPI:
    #
    # "Get the value from an HTTP header."
    #
    # However, this expects a header literally named "token".
    #
    # Example:
    #
    #     token: abc123
    #
    # For the more common Authorization header approach,
    # you would use Header(None, alias="Authorization").
    token: str = Header(None)
):

    try:

        # Decode and VERIFY the JWT
        #
        # jwt.decode() does several things:
        #
        # 1. Checks the token's signature
        # 2. Uses SECRET_KEY to verify the signature
        # 3. Checks the expiration ("exp")
        # 4. Returns the payload if everything is valid
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )


        # Return the decoded payload
        #
        # Example:
        #
        #     {
        #         "sub": "admin",
        #         "exp": ...
        #     }
        #
        # Returning it is important because this value
        # will become the value of "user" in secure_data().
        return payload


    # If decoding/verification fails, the token is invalid.
    except Exception:

        # HTTP 401 = Unauthorized
        raise HTTPException(
            status_code=401,
            detail="invalid token"
        )


# ---------------------------------------------------------
# PROTECTED / SECURED ENDPOINT
# ---------------------------------------------------------

@app.get("/")
def secure_data(
    # Depends() tells FastAPI:
    #
    # "Before running secure_data(), run verify_token()."
    #
    # So the flow is:
    #
    #     Request
    #        ↓
    #     verify_token()
    #        ↓
    #     token valid?
    #        ↓
    #     yes
    #        ↓
    #     secure_data()
    #
    # If verify_token() raises an HTTPException,
    # secure_data() is never executed.
    user=Depends(verify_token)
):

    # If we reach this point, the token was valid.
    return {
        "message": "secured data accessed",

        # "user" contains whatever verify_token()
        # returned.
        #
        # In our case, that's the decoded JWT payload.
        "user": user
    }

# The JWT flow to remember
#                     LOGIN
#                       │
#                       │ username + password
#                       ▼
#                  /login
#                       │
#                       ▼
#               create_token()
#                       │
#                       ▼
#                  JWT token
#                       │
#                       │ return to client
#                       ▼
#                    CLIENT
#                       │
#                       │ sends token
#                       ▼
#                 GET /
#                       │
#                       ▼
#              Depends(verify_token)
#                       │
#                       ▼
#                jwt.decode()
#                       │
#               ┌───────┴───────┐
#               │               │
#            invalid           valid
#               │               │
#               ▼               ▼
#           401 error       payload
#                               │
#                               ▼
#                          secure_data()
#                               │
#                               ▼
#                          response

# Three things to remember
# create_token()
#     ↓
# creates + signs JWT


# verify_token()
#     ↓
# decodes + verifies JWT


# Depends(verify_token)
#     ↓
# forces verify_token() to run
# before the protected endpoint


# And this part:

# user = Depends(verify_token)


# does not mean user is the username automatically.

# It means:

# "Run verify_token() and put whatever it returns into user."

# That's why we return payload from verify_token().