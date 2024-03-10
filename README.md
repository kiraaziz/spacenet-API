# SpaceNet Scraper API
![Project Logo](https://github.com/kiraaziz/spacenet-API/blob/main/assets/screen.png)

Welcome to the SpaceNet Scraper API documentation. This API allows you to retrieve information about categories, items, and detailed product information from the SpaceNet website.

## Base URL

The base URL for the SpaceNet Scraper API is:

```plaintext
https://spacenet-api.vercel.app
```

## Endpoints

### 1. Retrieve All Categories

#### Endpoint

```plaintext
GET /all-category
```

#### Description

Retrieve a list of all available categories and their subcategories.

#### Response

The API returns a JSON array containing categories and their subcategories:

```json
[
  {
    "id": "4-informatique",
    "name": "Informatique",
    "children": [
      {
        "id": "18-ordinateur-portable",
        "name": "Ordinateur portable"
      },
      {
        "id": "74-pc-portable-tunisie",
        "name": "PC Portable"
      },
      // ... other categories and subcategories
    ]
  },
  // ... other top-level categories
]
```

### 2. Retrieve Total Items in a Category

#### Endpoint

```plaintext
GET /category/page/{id}
```

- `{id}`: The unique identifier of the category.

#### Description

Retrieve the total number of items (products) in a specific category.

#### Response

The API returns a JSON object containing the total number of items in the specified category:

```json
{
  "total": 1
}
```

### 3. Retrieve Items in a Category

#### Endpoint

```plaintext
GET /category/items/{id}?page={number}
```

- `{id}`: The unique identifier of the category.
- `{number}`: The page number for pagination.

#### Description

Retrieve items in a specific category with pagination support.

#### Response

The API returns a JSON object containing an array of items in the specified category:

```json
{
  "total": [
    {
      "cover": "https://spacenet.tn/21235-home_default/processeur-intel-7eme-generation-i3-7100.jpg",
      "id": "13197-processeur-intel-7eme-generation-i3-7100",
      "manufacturer": {
        "image": "https://spacenet.tn/img/m/3522.jpg",
        "name": "intel"
      },
      "name": "PROCESSEUR Intel Core I3-7100 3.9GHz Socket LGA 1151 version Tray sans ventilateur",
      "price": 239,
      "ref": "CPU-I3-7100"
    },
    // ... other items
  ]
}
```

### 4. Retrieve Item Details

#### Endpoint

```plaintext
GET /item/{id}
```

- `{id}`: The unique identifier of the item.

#### Description

Retrieve detailed information about a specific item, including description, images, manufacturer details, price, references, and stock availability.

#### Response

The API returns a JSON object containing the item details:

```json
{
  "description": "<div class=\"product-des\" ... </p></div>",
  "images": [
    "https://spacenet.tn/161487-home_default/haut-parleur-bluetooth-portable-marvo-hy-07-noir.jpg",
    // ... other images
  ],
  "manufacturer": {
    "image": "https://spacenet.tn/img/m/6118.jpg",
    "name": "Marvo"
  },
  "price": "89",
  "ref": "HY-07",
  "sheet": {
    "Connectivité": "Bluetooth",
    "Couleur": "Noir",
    "Gamer": "Non",
    "Garantie": "1 An",
    "Puissance": "3 W"
  },
  "stock": [
    {
      "address": "56, Rue de L'industrie Charguia I   cp 2035",
      "location": "https://www.google.com/maps/place/Spacenet+Charguia/...",
      "name": "Magasin Charguia",
      "state": "Disponible"
    },
    // ... other stock locations
  ],
  "title": "Haut Parleur Bluetooth Portable Marvo HY-07 - Noir"
}
```

## Examples in Node.js

### Example 1: Retrieve All Categories

```javascript
const axios = require('axios');

async function getAllCategories() {
  try {
    const response = await axios.get('https://spacenet-api.vercel.app/all-category');
    console.log(response.data);
  } catch (error) {
    console.error('Error retrieving categories:', error.message);
  }
}

getAllCategories();
```

### Example 2: Retrieve Total Items in a Category

```javascript
const axios = require('axios');

async function getTotalItemsInCategory(categoryId) {
  try {
    const response = await axios.get(`https://spacenet-api.vercel.app/category/page/${categoryId}`);
    console.log(response.data);
  } catch (error) {
    console.error('Error retrieving total items:', error.message);
  }
}

getTotalItemsInCategory('203-pc-gamer-tunisie');
```

### Example 3: Retrieve Items in a Category

```javascript
const axios = require('axios');

async function getItemsInCategory(categoryId, page) {
  try {
    const response = await axios.get(`https://spacenet-api.vercel.app/category/items/${categoryId}?page=${page}`);
    console.log(response.data);
  } catch (error) {
    console.error('Error retrieving items:', error.message);
  }
}

getItemsInCategory('203-pc-gamer-tunisie', 1);
```

### Example 4: Retrieve Item Details

```javascript
const axios = require('axios');

async function getItemDetails(itemId) {
  try {
    const response = await axios.get(`https://spacenet-api.vercel.app/item/${itemId}`);
    console.log(response.data);
  } catch (error) {
    console.error('Error retrieving item details:', error.message);
  }
}

getItemDetails('13197-processeur-intel-7eme-generation-i3-7100');
```

Feel free to use these examples as a reference for integrating SpaceNet Scraper into your Node.js application.

Feel free to use the SpaceNet Scraper API to retrieve information about categories and the total number of items in specific categories. If you encounter any issues or have suggestions, please open an [issue](https://github.com/kiraaziz/spacenet-API/issues) on the GitHub repository. Happy coding!
