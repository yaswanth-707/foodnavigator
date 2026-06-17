from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/')
def home():

    search_query = request.args.get('search', '').lower()
    food_mapping = {
    "idly": "tiffin",
    "idli": "tiffin",
    "dosa": "tiffin",
    "vada": "tiffin",
    "poori": "tiffin",
    "upma": "tiffin",
        
    "chicken": "lunch",
    "biryani" :"lunch",
    "meals": "lunch",
    "rice": "lunch",

    "tea": "beverages",
    "coffee": "beverages",
    "juice": "beverages",

    "cake": "bakery",
    "puff": "bakery"
}
    if search_query in food_mapping:
     search_query = food_mapping[search_query]

    conn = get_db_connection()

    query = "SELECT * FROM food_centers WHERE 1=1"

    params = []

    if search_query:

        query += """
        AND (
            name LIKE ?
            OR area LIKE ?
            OR food_type LIKE ?
        )
        """

        params.extend([
            f'%{search_query}%',
            f'%{search_query}%',
            f'%{search_query}%'
        ])

    foods = conn.execute(query, params).fetchall()

    conn.close()

    return render_template(
        'index.html',
        foods=foods,
        search_query=search_query
    )
if __name__ == '__main__':
    app.run(debug=True)