import requests
from bs4 import BeautifulSoup
import re
from flask import Flask

url = 'https://spacenet.tn'

def transform_value(input_value):
    cleaned_value = re.sub(r'[^\d]+', '', input_value.replace('\xa0', ''))
    numeric_value = int(cleaned_value)
    return numeric_value

def use_get_all_categories():
    result = []
    response = requests.get(url)

    if response.status_code == 200:

        content = BeautifulSoup(response.text, 'html.parser')
        links = content.select(".nav>li")

        for link in links:

            category =  link.select("a")
            children = []

            for child in link.select(".dropdown-menu>ul>li>a"):
                children.append({
                    "name":' '.join(child.text.split()),
                    "id": child.get("href").replace("/", "")       
                })

            result.append({
                "name":' '.join(category[0].text.split()),
                "id": category[0].get("href").replace("/", ""),
                "children": children
            })

    
    return result
    
def use_get_category_total_pages(id):
    result = 1
    response = requests.get(url+"/"+str(id))

    if response.status_code == 200:

        content = BeautifulSoup(response.text, 'html.parser')
        numbers = content.select(".page-list>li>a")

        if(numbers != []):
            result = int(numbers[-2].text)
        
    else:
        result = 0
    
    return result


# orders = [position.asc, date_add.desc, name.asc, name.desc, price.desc, price.asc, quantity.desc, random.desc]
def use_get_category_items(id, page=1, order="random.desc"):

    result = []

    subUrl = url +"/"+str(id)+"?order=product."+order
    if(page != 1):
        subUrl = subUrl + "&page=" + str(page)

    response = requests.get(subUrl)
    content = BeautifulSoup(response.text, 'html.parser')

    items = content.select(".item>div")

    for item in items:
        result.append({
            "id": item.select(".right-product>h2>a")[0].get("href").split("/")[-1].replace(".html", ""),
            "name": item.select(".right-product>h2>a")[0].text.strip(),
            "price": transform_value(item.select(".right-product>div>span")[1].text.strip())/1000,
            "ref": item.select(".right-product>.product-reference>span")[0].text.strip(),
            "cover": item.select(".left-product>a>span>img")[0].get("src"),
            "manufacturer": {
                "name": item.select(".right-product>.product-manufacturer>a")[0].get("href").split("-")[-1],
                "image": item.select(".right-product>.product-manufacturer>a>img")[0].get("src"),
            },
        })

    return result


def use_get_item_details(id):
    
    response = requests.get(url+"/"+str(id)+".html")

    if response.status_code == 200:

        content = BeautifulSoup(response.text, 'html.parser')

        return {
            "title": content.select(".product_right>h1")[0].text.strip(),
            "price": content.select(".current-price>span")[0].get("content"),
            "ref": content.select(".product-reference>span")[0].text.strip(),
            "images": [val.get("src") for val in content.select(".product-images>div>img")],
            "description": str(content.select(".product-des")[0]),
            "manufacturer": {
                "name": content.select(".manufacturer-logo")[0].get("alt"),
                "image": content.select(".manufacturer-logo")[0].get("src"),
            },
            "stock": [{
                "name": val.select("div>span")[0].text.strip(),
                "address":  val.select("div>p")[0].text.strip() if val.select("div>p") != [] else "",
                "location": val.select("div>span>a")[0].get("href") if val.select("div>span>a") else "",
                "state": val.select("div>span")[1].text.strip() if val.select("div>p") != [] else "",
            } for val in content.select(".magasin-table>.table-bloc")],
            "sheet": {
                val.text.strip(): content.select(".data-sheet>dd")[index].text.strip()
                for index, val in enumerate(content.select(".data-sheet>dt"))
            }
        }

    return {}


app = Flask(__name__)

@app.route('/all-category')
def list():
    return use_get_all_categories()

@app.route('/category/page/<string:id>')
def page(id):
    return {"total" : use_get_category_total_pages(id)}

@app.route('/category/items/<string:id>')
def items(id):
    return {"total" : use_get_category_items(id)}

@app.route('/item/<string:id>')
def item(id):
    return use_get_item_details(id)