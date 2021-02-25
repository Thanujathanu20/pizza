# Pizza Assignment Documentation

## Table of contents
* [General info](#general-info)
* [API endpoints](#Api-end-points)
* [Setup](#setup)

## General info
This project is a Django application which stores information about different types of Pizza. I created an API interface that lists the information about the different stored pizzas and can also edit & delete the pizzas information.

## API endpoints
### GET the pizzas
If the request given is:
```
GET /api/pizza_api
```
Then the response is:

```
[
    {
        "pizzaType": "Regular",
        "pizzaSize": "Large",
        "toppings": "Onions"
    },
    {
        "pizzaType": "Square",
        "pizzaSize": "Large",
        "toppings": "corn"
    },
    {
        "pizzaType": "Regular",
        "pizzaSize": "small",
        "toppings": "corn"
    },
    {
        "pizzaType": "Square",
        "pizzaSize": "small",
        "toppings": "cheese"
    }
]
```
### POST the pizza to the list
If the request given is:
```
POST /api/pizza_api

{
    "pizzaType": "Regular",
    "pizzaSize": "Medium",
    "toppings": "Tomato"
}
```
Then the response is:
```
{
    "id":8,
    "pizzaType":"Regular",
    "pizzaSize":"Medium",
    "toppings":"Tomato"
}
```
### UPDATE the pizza in the list
If the request given is:
```
PUT /api/pizza_api/:id
```
Example:
```
{
    "pizzaType": "Regular",
    "pizzaSize": "Large",
    "toppings": "Capsicum"
}
```
Then the response is:
```
{
    "id":8,
    "pizzaType":"Regular",
    "pizzaSize":"Large",
    "toppings":"Capsicum"
}
```
### DELETE the pizza in the list
If the request given is:
```
DELETE /api/pizza_api/:id
```
Example:
```
{
    "pizzaType": "Regular",
    "pizzaSize": "Large",
    "toppings": "Capsicum"
}
```
Then the response is:
```
"Deleted Successfully"
```
### GET the filtered pizzas based on type and size
If the request given is:
```
GET /api/pizza_api?type=Regular&size=Large
```
Then the response is:

```
[
    {
        "pizzaType": "Regular",
        "pizzaSize": "Large",
        "toppings": "Onions"
    }
]
```

## Setup
To run this project:
### Clone the project
Run this command 
```
git clone https://github.com/Thanujathanu20/pizza.git
```
### Install the requirements
```
pip install -r requirements.txt
```
### Run the server 
```
python manage.py runserver
```
