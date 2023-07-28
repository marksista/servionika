# -*- coding: utf-8 -*-

import argparse
import json
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def load_data():
    try:
        if os.path.exists(storage_path):
            with open(storage_path, 'r') as f:
                return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print("Ошибка при загрузке и считывании данных")
    return {}



def add_data(key, value):
    data = load_data()
    data.setdefault(key, []).append(value)
    try:
        with open(storage_path, 'w') as f:
            json.dump(data, f, ensure_ascii=False)
            print('Key-Value has been saved:', key, '-', value)
    except IOError as e:
        print("Ошибка при сохранении данных")

def get_data(key):
    data = load_data()
    return data.get(key, None)

def main():
    try:
        parser = argparse.ArgumentParser(description="Хранилище типа \"Ключ-Значение\"")
        parser.add_argument('--key', help='Ключ')
        parser.add_argument('--val', help='Значение')
        args = parser.parse_args()

        if not args.key and not args.val:
            parser.print_help()
        elif args.key and args.val:
            add_data(args.key, args.val)
        elif args.key:
            values = get_data(args.key)
            if values:
                print(','.join(values))
            else:
                print(None)
    except Exception as e:
        print("Ошибка!")
        print (e)

if __name__ == '__main__':
    main()
