import csv

def load_products_from_csv(file_path):
    products = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products