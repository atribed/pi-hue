"""
    Pi-Hue

    Quick Flask app that sets you up to interface with Philips Hue lighting.

"""

from flask import Flask, render_template
import sqlite3

# Not ideal, but since it's just being used across a home network not concerned at the moment.
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def load_home():
    with sqlite3.connect('../../light.db') as connection:
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM light_intensity ORDER BY reading_time LIMIT 10')
        rows = cursor.fetchall()
    return render_template('index.html', rows=rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
