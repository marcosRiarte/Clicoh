import json
from collections import namedtuple
from django.contrib.sites import requests
from iteration_utilities import duplicates


""" Devuelve el valor del dolar blue actual"""


def get_usd():
    response = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    dictionary = json.loads(response.text)
    dolar_blue = dictionary[1]
    return dolar_blue['casa']['venta']


"""Contraola que no se repitan los productos"""


def item_repeated(data):
    list_to_items = data['details']
    #Valido si hay items (lista Vacia)
    #creo lista de product_id
    product_id_list = []
    for item in list_to_items:
        product_id_list.append(item['product'])
    product_id_duplicates = list(duplicates(product_id_list))
    if len(product_id_duplicates) == 0:
        return False
    else:
        return True



"""Controla que la cantidad de todos los productos de la orden sea mayor a cero"""


def amount_non_zero(data):
    list_to_items = data['details']
    #Valido si hay items (lista Vacia)
    for item in list_to_items:
        if item['cuantity'] <= 0:
            return False
        else:
            return True


"""Obtiene el precio de los productos"""


def get_product_price(queryset, id_product):
    for i in queryset:
        id_set = i.id
        if id_set == id_product:
            return i.price
    return print('No existe el producto')


"""Calcula el monto total de la orden en pesos"""


def get_total(queryset, data):
    list_to_json = data['details']
    #Valido si hay items (lista Vacia)
    total = 0
    for item in list_to_json:
        id_product = item['product']
        cuantity = item['cuantity']
        price = get_product_price(queryset, id_product)
        total = total + price * cuantity
    return total


"""Calcula el monto total de la orden en dolares"""


def get_total_usd(total_price):
    dolar_price = get_usd()
    order_amount_total = total_price * dolar_price
    return order_amount_total


"""Devuelve la lista de items de la orden"""


def get_order_items_list(self, response):
    dictionary = json.loads(response.text)
    body_test = namedtuple("body", dictionary.keys())(*dictionary.values())
    list_to_json = body_test.items
    return list_to_json


"""Obtener el id de la orden"""


def get_order_id(self, response):
    dictionary = json.loads(response.text)
    body_test = namedtuple("body", dictionary.keys())(*dictionary.values())
    order_id = body_test.id
    return order_id


def get_order_date_time(self, response):
    dictionary = json.loads(response.text)
    body_test = namedtuple("body", dictionary.keys())(*dictionary.values())
    order_date_time = body_test.date_time
    return order_date_time



