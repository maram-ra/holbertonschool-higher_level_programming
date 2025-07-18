from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json') as file:
        return json.load(file)

def read_csv():
    products = []
    with open('products.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = []
    error = None

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        error = 'Wrong source'
        return render_template('product_display.html', error=error)

    if product_id:
        try:
            product_id = int(product_id)
            data = [item for item in data if item['id'] == product_id]
            if not data:
                error = 'Product not found'
        except ValueError:
            error = 'Invalid ID format'
            data = []

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
