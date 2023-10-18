"""
Вспомогательные функции для сериализации
"""

import json
import pickle
import csv


def save_to_json(filename, data):  # Запись в JSON
    if filename and data:
        with open(filename, 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=4)


def save_to_pickle(filename, data):  # Запись в PICKIE
    if filename and data:
        with open(filename, 'wb') as f:  # pickie не переводит числа в строку, поэтому пишем в двоичный файл
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)


def save_to_csv(filename, data):  # Запись в CSV
    def get_dict_obj(local_data):  # Разворачиваем структуру словаря в плоскую таблицу
        nonlocal files
        for key, item in local_data.items():
            if key in ['files', 'directories']:
                for fkey, fitem in item.items():
                    files.append({'name': fkey, 'is_dir': key == 'directories',
                                  'parent': fitem['parent'], 'size': fitem['size']})
                    if key == 'directories':
                        get_dict_obj(fitem)

    if filename and data:
        files_header = ['name', 'is_dir', 'parent', 'size']
        files = [{'name': "root", 'is_dir': True, 'parent': data['parent'], 'size': data['size']}]
        get_dict_obj(data)

        with open(filename, 'w', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=files_header)
            writer.writeheader()
            writer.writerows(files)
