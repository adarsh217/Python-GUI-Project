
# Executable Python based GUI Application

* This is a Python GUI app which has been created using Python and MongoDB as database.
* It provides the user the facility to visualize graphs as well as classify between "good" and "bad" products

#
#


# Prerequisites:
* Python3
* PySide2
* MongoDB (cloud based)
#
#

# Usage:
#### Clone the repository:
```
$ git clone https://github.com/adarsh217/Python-GUI-Project.git
```
Or Alternatively you can choose to download it as a zip file.
#
#### Install Dependencies :
Extract the zip file in case you downloaded it as zip
#
#### Run the app by simply executing :
```
Python-GUI-Project/dist/main/app.exe
```
#
#
#### Setting up the MongoDB database
A static dataset of images of bottles was taken from online sources.
A databse collection was setup on MongoDB Atlas cloud server with the format
* SKU id
* Unit id
* Status

The databse was fetched by the python code from the cloud server (as can been seen in the main.py file)
After establishing the connection, we use the database as required.
#
#
