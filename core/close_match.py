import difflib
def find_closest_match(products, product_name):
    product_names = [product["product_name"] for product in products]
    closest_matches = difflib.get_close_matches(product_name, product_names, n=1, cutoff=0.0)
    return closest_matches[0] if closest_matches else None