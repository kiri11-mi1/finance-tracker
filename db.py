import os
import sqlite3

# Подключаю базу
db = sqlite3.connect('finance.db')
cursor = db.cursor()

def insert(table, column_values):
    '''Добавление в таблицу'''
    pass


def get_all(table, columns):
    '''Получение данных с таблицы'''
    pass


def delete(table, row_id):
    '''Удаление строки из таблицы'''
    pass


def get_cursor():
    pass


def init_db():
    '''Инициализация базы'''
    if db_exist():
        return
    with open('createdb.sql') as rf:
        sql = rf.read()
    cursor.executescript(sql)
    db.commit()


def db_exist():
    '''Прверка на существование базы данных'''
    cursor.execute("SELECT name FROM sqlite_master "
                    "WHERE type='table' AND name='expense'")
    table = cursor.fetchall()
    if table:
        return True
    return False

init_db()