from bs4 import BeautifulSoup 
import requests
from fastapi import FastAPI

# Creating a fastapi instance
app = FastAPI()


@app.get("/")
async def welcome():
    return "Welcome to Flipping to flipkart"

@app.get('/get/{data}')
async def get_data(data):

    product_dict = []

    # url of the product
    url = f"https://www.flipkart.com/search?q={data.replace(' ','%20')}"

    # Requesting the webpage
    request = requests.get(url).text

    # Creating soup object
    soup = BeautifulSoup(request, "lxml")

    # getting the total page number for particular product search
    page_no = soup.find("div", class_="_2MImiq").span.text
    start_index = page_no.find("of") + 3
    page_no = int(page_no[start_index:].replace(",", ""))


    for j in range(1, page_no + 1):
        # url of each page
        url = f"https://www.flipkart.com/search?q={data.replace(' ','%20')}&page=" + str(j)

        # Requesting the webpage
        request = requests.get(url).text

        # Creating soup object
        soup = BeautifulSoup(request, "lxml")

        # Looping through each line
        for i in soup.find_all("div", class_="_13oc-S"):
            # using conditional statement to check the presence of required data and fill `None` in absence of the data
            # scraping Product name
            if i.find("div", class_="_4rR01T"):
                name = i.find("div", class_="_4rR01T")
                product = name.text
            else:
                product = None

            # scraping Price
            if i.find("div", class_="_30jeq3 _1_WHN1"):
                rate = i.find("div", class_="_30jeq3 _1_WHN1")
                price = rate.text
            else:
                price = None

            # scraping MRP
            if i.find("div", class_="_3I9_wc _27UcVY"):
                max_price = i.find("div", class_="_3I9_wc _27UcVY")
                mrp = max_price.text
            else:
                mrp = None

            # scraping Rating
            if i.find("div", class_="_3LWZlK"):
                ratings = i.find("div", class_="_3LWZlK")
                rating = ratings.text
            else:
                rating = None

            product_dict.append(
                {"product": product, "price": price, "MRP": mrp, "ratings": rating}
            )

    return product_dict