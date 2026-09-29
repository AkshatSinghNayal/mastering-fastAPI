from fastapi import FastAPI, HTTPException, UploadFile, File
import shutil
from fastapi.staticfiles import StaticFiles
import os

# Create the FastAPI application object
app = FastAPI()


# Name of the directory where uploaded files will be stored
DIR_REQ = "uploads"


# Check if the "uploads" directory already exists
if not os.path.exists("uploads"):

    # If it doesn't exist, create it
    os.makedirs("uploads")


# Mount the local "uploads" directory to the "/files" URL
#
# This means:
#
#     uploads/photo.jpg
#
# can be accessed through:
#
#     http://127.0.0.1:8000/files/photo.jpg
#
# StaticFiles is responsible for serving the existing files.
#
# mount() connects the URL path "/files"
# with the local directory "uploads".
app.mount(
    "/files",
    StaticFiles(directory="uploads"),
    name="files"
)


# Endpoint for uploading a file
#
# POST /post
#
# UploadFile represents the uploaded file.
# File(...) tells FastAPI that this parameter
# should come from a multipart/form-data file upload.
#
# The ... means the file is required.
@app.post("/post")
def create_post(file: UploadFile = File(...)):

    # Check if a filename was provided
    if not file.filename:

        # raise is used to stop the function and return an HTTP error
        raise HTTPException(
            status_code=404,
            detail="file not exits"
        )


    # Get only the filename from the uploaded file
    #
    # Example:
    #
    #     file.filename = "photo.jpg"
    #
    # filename = "photo.jpg"
    #
    # basename() is useful to remove any directory/path
    # information that might be included in the filename.
    filename = os.path.basename(file.filename)


    # Create the complete path where the file will be saved
    #
    # Example:
    #
    #     DIR_REQ = "uploads"
    #     filename = "photo.jpg"
    #
    # Result:
    #
    #     file_path = "uploads/photo.jpg"
    file_path = os.path.join(DIR_REQ, filename)


    try:

        # Open/create the destination file
        #
        # "wb" means:
        #
        #     w = write
        #     b = binary
        #
        # Binary mode is important because files can be
        # images, PDFs, videos, etc.
        #
        # "buffer" is the destination file object.
        with open(file_path, "wb") as buffer:

            # file.file is the uploaded file's underlying
            # file-like object.
            #
            # shutil.copyfileobj() copies the contents from:
            #
            #     file.file  --->  buffer
            #
            # So the uploaded file gets copied into:
            #
            #     uploads/photo.jpg
            shutil.copyfileobj(file.file, buffer)

    finally:

        # The "with open(...)" automatically closes "buffer".
        # So this line is actually unnecessary.
        #
        # You can remove the finally block completely.
        buffer.close()


    # Return information about the uploaded file
    return {

        # Message returned to the client
        "msg": "uploaded done with respect",

        # Name of the uploaded file
        #
        # Example:
        #     "photo.jpg"
        "file_name": filename,

        # Actual path on the server's filesystem
        #
        # Example:
        #     "uploads/photo.jpg"
        "filepath": file_path,

        # URL through which the file can be accessed
        #
        # Because we mounted:
        #
        #     "/files" -> "uploads"
        #
        # this URL:
        #
        #     /files/photo.jpg
        #
        # points to:
        #
        #     uploads/photo.jpg
        "fileurl": f"http://127.0.0.1:8000/files/{filename}"
    }


# Endpoint for checking whether a file exists
#
# Example:
#
#     GET /file/photo.jpg
#
@app.get("/file/{filename}")
def get_file(filename: str):

    # Get only the filename
    #
    # Example:
    #
    #     filename = "photo.jpg"
    filename = os.path.basename(filename)


    # Create the path to the file
    #
    # Example:
    #
    #     uploads/photo.jpg
    file_path = os.path.join(DIR_REQ, filename)


    # Check if the file actually exists
    if not os.path.exists(file_path):

        # If it doesn't exist, return a 404 error
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )


    # Return the URL where the file can be accessed
    #
    # This endpoint does NOT send the actual file.
    #
    # It only gives the client a URL.
    #
    # StaticFiles will handle that URL and return the actual file.
    return {
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }


# Simple home endpoint
#
# GET /
#
@app.get("/")
def home():

    # Return a simple JSON response
    return {
        "message": "File upload API"
    }

# The core flow in your code
# POST /post
#     ↓
# UploadFile
#     ↓
# file.file
#     ↓
# shutil.copyfileobj()
#     ↓
# uploads/photo.jpg
#     ↓
# StaticFiles
#     ↓
# /files/photo.jpg
#     ↓
# actual file returned


# One correction I made is important: use raise HTTPException(...), not return HTTPException(...).