import os


def get_dirs(path):
    """
    Функция получает на вход начальный каталог, и возвращает в виде словаря внутреннюю
    структуру этого каталога
    - Указывается родительская директория.
    - Указывается файл это или директория.
    - Для файлов указывается его размер в байтах, а для директорий размер файлов
      в ней с учётом всех вложенных файлов и директорий.
    :param path:  Начальный каталог
    :return: Словарь со структурой каталога
    """
    files_container = {}  # Тут храним словарь файлов
    dirs_container = {}  # Тут храним словарь каталогов
    dir_size = 0

    for dr in os.listdir(path):  # обходим каталог по его содержимого
        obj_path = os.path.join(path, dr)
        if not os.path.isdir(obj_path):  # Проверка на каталог
            files_container[dr] = {"parent": os.sep.join(path.split(os.sep)[:-1]),
                                   "is_dir": False, "size": os.stat(obj_path).st_size}
            dir_size += os.stat(obj_path).st_size
        else:
            dirs_container[dr] = get_dirs(path + os.sep + dr)  # Спускаемся в дочерний каталог
            dir_size += dirs_container[dr]["size"]

    return {"parent": os.sep.join(path.split(os.sep)[:-1]), "is_dir": True, "size": dir_size, "files": files_container,
            "directories": dirs_container}
