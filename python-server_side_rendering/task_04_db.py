from flask import Flask, render_template, request
import json, csv, sqlite3

app = Flask(__name__)

def read_json():
    with open('products.json') as f:
        return json.load(f)

def read_csv():
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        return list(reader)

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = [{"id": r[0], "name": r[1], "category": r[2], "price": r[3]} for r in rows]
        return products
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = []

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    if isinstance(data, dict) and "error" in data:
        return render_template('product_display.html', error=data["error"])

    if product_id:
        data = [item for item in data if str(item.get("id")) == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
