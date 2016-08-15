"""
    Pi-Hue

    Quick Flask app that sets you up to interface with Philips Hue lighting.

"""

from flask import Flask, request, render_template, jsonify
import picamera

# Not ideal, but since it's just being used across a home network not concerned at the moment.
app = Flask(__name__, static_url_path='/static')

# Setting up camera so we can submit pictures to set a scene with Hue.
camera = picamera.PiCamera()

@app.route('/')
def load_home():
    return render_template('index.html')

@app.route('/picture', methods=['POST'])
def take_picture():
    images_path = 'static/images/image.jpg'
    camera.capture(images_path)
    #
    # Just a temp response for the time being.
    return jsonify(
        success=True,
        imagePath=images_path
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
