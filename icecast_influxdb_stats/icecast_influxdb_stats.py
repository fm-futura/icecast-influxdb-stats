#!/usr/bin/env python3

import argparse
import requests

import xml.etree.ElementTree as ET

from influxdb import InfluxDBClient


httptimeout = 2.0


def send_stats(host=None, port='8000', user='admin', password='hackme', mountpoint=None, influx_dsn=None,
               influx_database=None):

    url = "http://{}:{}/admin/listclients?mount={}".format(host, port, mountpoint)
    req = requests.get(url, auth=(user, password), timeout=httptimeout)

    if req.status_code == 401:
        raise Exception("Authentication Failed.")

    elif req.status_code != 200:
        raise Exception("Unknown Error.")

    try:
        parsed = ET.fromstring(req.text)
        listeners = int(parsed.find('source/Listeners').text)
    except:
        raise Exception("Error parsing xml.")

    client = InfluxDBClient.from_dsn(influx_dsn)
    if influx_database is not None:
        client.switch_database(influx_database)

    payload = [
        {
            'measurement': 'listeners',
            'fields': {
                'count': listeners
            }
        }
    ]

    client.write_points(payload)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--influx-dsn',
                        required=False,
                        default='influxdb://root:root@localhost:8086/',
                        help='The InfluxDB data source name. Defaults to %(default)s')

    parser.add_argument('--influx-database',
                        required=False,
                        default='live',
                        help='The InfluxDB database name. Defaults to %(default)s')

    parser.add_argument('--host',
                        required=True,
                        help='Icecast host. (%(default)s)',
                        default='127.0.0.1')

    parser.add_argument('--port',
                        required=True,
                        help='Icecast port. (%(default)s)',
                        type=int,
                        default=8000)

    parser.add_argument('--user',
                        required=True,
                        help='Icecast admin user. (%(default)s)',
                        default='admin')

    parser.add_argument('--password',
                        required=True,
                        help='Icecast admin password.')

    parser.add_argument('--mountpoint',
                        required=True,
                        help='Icecast mountpoint.')

    args = parser.parse_args()
    send_stats(**vars(args))


if __name__ == '__main__':
    main()
