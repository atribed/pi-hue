#!/usr/bin/env python

import picamera
import picamera.array
import numpy as np
import sqlite3
import os

def add_light_intensity(light_intensity=None):
    """
    Adds a light intensity reading to the database.
    :param light_intensity: int
    :return:
    """
    try:
        connection = sqlite3.connect('../../light')
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute("INSERT INTO light_intensity('light_reading') VALUES(?)", (light_intensity,))
    except:
        connection.rollback()
        print('Error with add_light_intensity, sql')
    else:
        connection.commit()
    finally:
        connection.close()


def get_light_reading():
    """
    Quick and cheap way to gauge light intensity from an image.
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
