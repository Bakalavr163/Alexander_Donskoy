import os
import sys
print('sys.argv = ', sys.argv)

def print_help():
    print("help -получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print("директория {} создана".format(dir_name))
    except FileExistsError:
        print("директория {} уже существует".format(dir_name))
def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping
}
try:
    dir_name = sys.argv[2]
except:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("wrong key")
        print("write help to get help")
