# Погружение в Python (семинары)
## Урок 8. Сериализация

### Задание 1

Напишите функцию, которая получает на вход директорию и рекурсивно обходит её 
и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle. 
- Для дочерних объектов указывайте родительскую директорию. 
- Для каждого объекта укажите файл это или директория. 
- Для файлов сохраните его размер в байтах, а для директорий размер файлов 
в ней с учётом всех вложенных файлов и директорий.

### Задание 2

Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.


### Решение
**Задание 1**

Решение находится в файле *my_file_utils2/my_dirs.py*

**Задание 2**

Пакет реализован в папке *my_file_utils2*

Примеры использования функций находятся в файле *main.py*

#### Результат работы:

Файл *dir_members.json*:

    {
    "parent": "C:\\Work\\python\\dz4\\Py4HW08",
    "is_dir": true,
    "size": 7342,
    "files": {
        "files_routine.py": {
            "parent": "C:\\Work\\python\\dz4\\Py4HW08",
            "is_dir": false,
            "size": 1675
        },
        "my_dirs.py": {
            "parent": "C:\\Work\\python\\dz4\\Py4HW08",
            "is_dir": false,
            "size": 1767
        },
        "__init__.py": {
            "parent": "C:\\Work\\python\\dz4\\Py4HW08",
            "is_dir": false,
            "size": 464
        }
    },
    "directories": {
        "__pycache__": {
            "parent": "C:\\Work\\python\\dz4\\Py4HW08\\my_file_utils2",
            "is_dir": true,
            "size": 3436,
            "files": {
                "files_routine.cpython-310.pyc": {
                    "parent": "C:\\Work\\python\\dz4\\Py4HW08\\my_file_utils2",
                    "is_dir": false,
                    "size": 1557
                },
                "my_dirs.cpython-310.pyc": {
                    "parent": "C:\\Work\\python\\dz4\\Py4HW08\\my_file_utils2",
                    "is_dir": false,
                    "size": 1415
                },
                "__init__.cpython-310.pyc": {
                    "parent": "C:\\Work\\python\\dz4\\Py4HW08\\my_file_utils2",
                    "is_dir": false,
                    "size": 464
                }
            },
            "directories": {}
        }
    }
    }


Файл *dir_members.csv*:

    name,is_dir,parent,size
    root,True,C:\Work\python\dz4\Py4HW08,7342
    files_routine.py,False,C:\Work\python\dz4\Py4HW08,1675
    my_dirs.py,False,C:\Work\python\dz4\Py4HW08,1767
    __init__.py,False,C:\Work\python\dz4\Py4HW08,464
    __pycache__,True,C:\Work\python\dz4\Py4HW08\my_file_utils2,3436
    files_routine.cpython-310.pyc,False,C:\Work\python\dz4\Py4HW08\my_file_utils2,1557
    my_dirs.cpython-310.pyc,False,C:\Work\python\dz4\Py4HW08\my_file_utils2,1415
    __init__.cpython-310.pyc,False,C:\Work\python\dz4\Py4HW08\my_file_utils2,464


Файл *dir_members.pickle* - находится в двоичном формате. Его можно посмотреть, скачав его.
