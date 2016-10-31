#!/usr/bin/env python

import picamera
import picamera.array
import numpy as np
import sqlite3
import os

def add_light_intensity(light_intensity=None):
    try:
        with sqlite3.connect('../../light') as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO light_intensity('light_reading') VALUES(?)", (light_intensity,))
            connection.commit()
    except EnvironmentError:
        print('Error with add_light_intensity, sql')


def get_light_reading():
    """
    Quick hacky-ish way to gauge light intensity.
    :return:  void
    """
    images_path = os.path.abspath('./image.jpg')
    with picamera.PiCamera() as camera:
        camera.capture(images_path)
        camera.resolution = (100, 75)
        with picamera.array.PiRGBArray(camera) as stream:
            camera.exposure_mode = 'auto'
            camera.awb_mode = 'auto'
            camera.capture(stream, format='rgb')
            pixAverage = int(np.average(stream.array[..., 1]))
            return pixAverage

add_light_intensity(get_light_reading())
