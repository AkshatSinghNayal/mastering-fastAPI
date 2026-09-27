from fastapi import FastAPI,Request
import time



app = FastAPI()


@app.middleware("http")
async def get_logs( request : Request, call_next ):
    starttime = time.time()

    response = await call_next(request)

    processTime = time.time() - starttime

    print(f"Path : {request.url.path} | time : {processTime}")

    return response



# @app.middleware("http")
# async def my_middleware( request : Request , call_next):
#     print("Request Recieved")

#     response = await call_next(request)

#     print("Response sent")

#     return response