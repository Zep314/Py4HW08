"""
Init-файл для пакета с моими модулями
"""
from my_file_utils2.my_dirs import get_dirs
from my_file_utils2.files_routine import save_to_json
from my_file_utils2.files_routine import save_to_pickle
from my_file_utils2.files_routine import save_to_csv

# Эти функции будем "экспортировать" для внешней работы
__all__ = ['get_dirs', 'save_to_json', 'save_to_csv', 'save_to_pickle']
