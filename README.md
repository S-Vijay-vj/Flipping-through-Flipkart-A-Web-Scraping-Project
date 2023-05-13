
# Flipping through Flipkart

This project involved scraping laptops' name, price, rating, and MRP from multiple pages of the popular Indian e-commerce website, Flipkart using Python and Beautiful Soup library and storing it in a CSV file. The scraped data is then exposed as a RESTful API using FastAPI. Users can send HTTP requests to the API to retrieve the scraped data in JSON format.


## Tools used
- Python 
- Beautiful Soup library for web scraping
- Requests library for HTTP requests
- Pandas library for data manipulation and analysis
- FastAPI library for creating RESTful API
- Uvicorn library for running FastAPI application
---


## Installation

Install request and Beautifulsoup library

```bash
  pip install requests
  pip install beautifulsoup4
  pip install fastapi
  pip install uvicorn[standard]
```
---
## About request library

The Requests library is a Python library that allows you to send HTTP requests using Python. It provides a simple API for interacting with HTTP operations. The methods implemented in the Requests library execute HTTP operations against a specific web server specified by its URL.

## About BeautifulSoup library

Beautiful Soup is a Python library for getting data out of HTML, XML, and other markup languages. It allows developers to parse HTML and XML documents and extract data from them. Beautiful Soup is designed to handle poorly formatted HTML and XML documents, which can be difficult to parse using other tools. It is a powerful Python library that makes web scraping and data extraction easy.

## About FastAPI library

FastAPI is a web framework for building APIs with Python. It is known for its simplicity, high performance, and support for modern web standards. FastAPI is based on the ASGI server and supports both synchronous and asynchronous programming models.

## About uvicorn library

Uvicorn is used to run the FastAPI application that provides a RESTful API to serve the scraped data from the Flipkart website. Uvicorn is chosen because it is a high-performance, lightweight ASGI server that is capable of handling many connections simultaneously with minimal overhead.

---
# Project Flow

## <b>Web scraping</b>

 1) Importing libraries

    The necessary libraries such as Pandas, requests and BeautifulSoup were imported.

    ```` bash
    import pandas as pd
    import csv
    from bs4 import BeautifulSoup 
    import requests
    ````

2) The required data is scraped using `request` and `BeautifulSoup` libraries.
3) With the scraped data, a data frame is created using `Pandas`.
    ````bash
    df=pd.DataFrame({'product':product,'price':price,'MRP':mrp,'ratings':rating})
    ````

4) Finally, the created dataframe is converted into [CSV](flipkart_laptop_scraping.csv) file using pandas inbuilt function.
    ````bash
    df.to_csv('flipkart_laptop_scraping.csv',index=False)
    ````

Here is the [Jupyter Notebook](flipkart_laptops_scraping.ipynb) for reference.

---

## Building API 

1) Importing libraries.

    The necessary libraries such as FastAPI and csv were imported.

    ```` bash
    from fastapi import FastAPI
    import csv
    ````
2)  Creating a fastapi instance
    ```bash
    app = FastAPI()
    ```
3) Defining root path.
    ```bash
    async def welcome():
      return {'welcome':'all'}   
    ```
4) Defining path parameter

    ``` bash
    @app.get("/data")
    async def read_data():
      with open(
          "D:\\python\\webscraping\\Flipkart_web_scraping\\flipkart_laptop_scraping.csv",
          newline="",
          encoding="utf-8",
      ) as csvfile:
          data = list(csv.DictReader(csvfile))
          return data
      ```

Here is the [python file](api.py) for reference.

---