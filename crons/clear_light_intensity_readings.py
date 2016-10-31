#!/usr/bin/env python

import sqlite3

def remove_rows_from_light_intensity_table():
    try:
        with sqlite3.connect('../../light') as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM light_intensity")
            connection.commit()
    except EnvironmentError:
        print('Error with add_light_intensity, sql')

remove_rows_from_light_intensity_table()
