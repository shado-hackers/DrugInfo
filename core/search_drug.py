def search_product(products, product_name):
    product_name = product_name.lower().strip()
    for product in products:
        if product["product_name"].lower().strip() == product_name:
            return product
    return "Product not found."