import os
import sqlite3

# Подключаю базу
db = sqlite3.connect('finance.db')
cursor = db.cursor()


def insert(table, column_values):
    '''Добавление в таблицу'''
    columns = ', '.join( column_values.keys() )
    values = [ tuple(column_values.values()) ]
    placeholders = ', '.join( "?" * len(column_values.keys()) )
    return placeholders
    cursor.executemany(
        f"INSERT INTO {table}"
        f"({columns})"
        f"VALUES ({placeholders})",
        values)
    db.commit()



def fetchall(table, columns):
    '''Получение данных с таблицы''' 
    columns_joined = ', '.join(columns)
    cursor.execute(f'SELECT {columns_joined} FROM {table}')
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result



def delete(table, row_id):
    '''Удаление строки из таблицы'''
    row_id = int(row_id)
    cursor.execute(f"delete from {table} where id={row_id}")
    db.commit()


def get_cursor():
    return cursor


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