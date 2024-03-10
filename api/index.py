from scarper_logic import use_get_all_categories, use_get_category_total_pages, use_get_category_items, use_get_item_details
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'