# Importing the libraries
from fastapi import FastAPI
import csv

# Creating a fastapi instance
app = FastAPI()

# Create root path
@app.get('/')
async def welcome():
    return {'welcome':'all'}
# path operation decorator
@app.get("/data")
# path operation function
async def read_data():
    # UTF-8 is commonly used for text files, web pages, and APIs that handle multilingual text data.
    with open(
        "D:\\python\\webscraping\\Flipkart_web_scraping\\flipkart_laptop_scraping.csv",
        newline="",
        encoding="utf-8",
    ) as csvfile:
        data = list(csv.DictReader(csvfile))
        return data
    # This opens the csv file and read the contents return the data as list of Dictionaries
