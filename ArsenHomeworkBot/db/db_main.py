import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print("База данных подключена!")

    cursor.execute(queries.CREATE_DATABASE_PRODUCTS)
    cursor.execute(queries.CREATE_TABLE_PRODUCTS_DETAIL)
    db.commit()


# async def sql_insert_products(name_products, size, price, product_id, photo):
#     cursor.execute(queries.INSERT_PRODUCTS, (
#         name_products,
#         size,
#         price,
#         product_id,
#         photo
#     ))
#     db.commit()

async def sql_insert_products(name_products, size, price, product_id, photo):
    with sqlite3.connect('db/store.sqlite3') as db:
        cursor = db.cursor()
        cursor.execute(queries.INSERT_PRODUCTS, (
            name_products, size, price, product_id, photo
        ))
        db.commit()


async def sql_insert_products_detail(product_id, category, info_product):
    with sqlite3.connect('db/store.sqlite3') as db:
        cursor = db.cursor()
        cursor.execute(queries.INSERT_PRODUCTS_DETAIL, (
            product_id,
            category,
            info_product
        ))
        db.commit()