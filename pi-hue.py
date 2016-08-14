"""
    Pi-Hue

    Quick Flask app that sets you up to interface with Philips Hue lighting.

"""

from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def load_home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
