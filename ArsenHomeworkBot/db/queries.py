CREATE_DATABASE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_products VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    product_id VARCHAR(255),
    photo TEXT
    )
"""


INSERT_PRODUCTS = """
    INSERT INTO products (name_products, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""


CREATE_TABLE_PRODUCTS_DETAIL = """
    CREATE TABLE IF NOT EXISTS products_detail
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product_id VARCHAR(255),
    category VARCHAR(255),
    info_product VARCHAR(255)
    )
"""

INSERT_PRODUCTS_DETAIL = """
    INSERT INTO products_detail (product_id, category, info_product)
    VALUES (?, ?, ?)
"""

CREATE_TABLE_PRODUCTS_COLLECTION = """
    CREATE TABLE IF NOT EXISTS products_collection
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id VARCHAR(255),
    collection VARCHAR(255)
    )
"""

INSERT_PRODUCTS_COLLECTION = """
INSERT INTO products_collection (product_id, collection)
VALUES (?, ?)
"""