#!/usr/bin/env python3


import argparse
import configparser
import json
import requests


def main ():
    config = configparser.ConfigParser()
    config.read('/etc/tell-discord.ini')

    parser = argparse.ArgumentParser()
    parser.add_argument('channel')
    parser.add_argument('messages', nargs='+')
    args = parser.parse_args()

    headers = {'content-type': 'application/json'}

    payload = {
        'content': ' '.join(args.messages)
    }

    requests.post(config[args.channel]['url'], headers=headers, data=json.dumps(payload))


if __name__ == '__main__':
    main()
