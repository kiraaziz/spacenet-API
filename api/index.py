from scarper_logic import use_get_all_categories, use_get_category_total_pages, use_get_category_items, use_get_item_details
from flask import Flask

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