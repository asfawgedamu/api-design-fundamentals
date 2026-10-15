# =========================================
#One of the purposes of an API is to decouple the data from the application that uses it, thereby hiding the data implementation details. In this case, we are using a hardcoded list of menu items instead of fetching them from a database. This allows us to change the data source in the future without affecting the application that uses it.
# =========================================

MENU = [
    {
        "id": 1,
        "name": "Burger",
        "price": 250
    },
    {
        "id": 2,
        "name": "Pizza",
        "price": 450
    },
    {
        "id": 3,
        "name": "Pasta",
        "price": 350
    },
    {
        "id": 4,
        "name": "Salad",
        "price": 150
    },
    
      {
        "id": 5,
        "name": "Shiro",
        "price": 450
    },
    {
        "id": 6,
        "name": "Doro Wat",
        "price": 1500
    }
]

def get_all_menu_items():
    return MENU