#!/usr/bin/env python

import sqlite3
import requests
import ConfigParser
import json

# This should be combined with record_light_reading_cron.py

def get_configs():
    """
    Gets configs from config file.
    :return:
    """
    config = ConfigParser.ConfigParser()
    config.read('/etc/pi-hue/pi-hue.ini')
    return config

def get_active_light_groups():
    """
    Gets active group light IDs.
    TODO: better error handling...
    :return:  list
    """
    try:
        connection = sqlite3.connect('../../light')
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute("SELECT group_id FROM light_groups WHERE is_active=1")
    except:
        print('Error getting active lights, sql')
    finally:
        active_lights = cursor.fetchall()
        connection.close()
        return active_lights

def get_last_light_reading():
    """
    Gets active group light IDs.
    TODO: better error handling...
    :return:  list
    """
    try:
        connection = sqlite3.connect('../../light')
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute("SELECT light_reading FROM light_intensity ORDER BY date(reading_time) DESC Limit 1")
    except:
        print('Error getting last light reading, sql')
    finally:
        light_reading = cursor.fetchone()
        connection.close()
        return light_reading

def update_hue():
    """
    API call to hue.
    :return:  void
    """
    active_lights = get_active_light_groups()
    config = get_configs()

    # TODO: lookup for light reading to ct value
    # light_reading = get_last_light_reading()

    # look at hue api, gotta be a better way
    for active_light in active_lights:
        url = '{bridge_address}/api/{username}/groups/{group_id}/action'.\
            format(bridge_address=config.get('api', 'ip_address'), username=config.get('api', 'username'), group_id=active_light[0])
        data = {"ct": 500}
        try:
            r = requests.put(url, json.dumps(data))
            print r.json();
        except:
            print('Error with API call to hue, update_hue')
