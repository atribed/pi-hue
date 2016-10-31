#!/usr/bin/env python

import sqlite3

def remove_rows_from_light_intensity_table():
    """
    Removes light intensity information from the light_intensity table.
    :return:
    """
    try:
        connection = sqlite3.connect('../../light')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM light_intensity")
    except EnvironmentError:
        print('Error with add_light_intensity, sql')
    finally:
        connection.commit()

remove_rows_from_light_intensity_table()
