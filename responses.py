import json
import os
import os.path as path

from prettytable import PrettyTable


if __name__ == '__main__':
    table = PrettyTable()
    table.field_names = ['Name', 'Email', 'Choice', 'Time']

    objs = []
    for filename in os.listdir('responses'):
        with open(path.join('responses', filename), 'r') as f:
            obj = json.load(f)
        objs.append(obj)

    objs = sorted(objs, key=lambda x: x['timestamp'])

    for obj in objs:
        table.add_row([obj['name'], obj['email'], obj.get('choice', '?'), obj['timestamp']])

    print(table)
