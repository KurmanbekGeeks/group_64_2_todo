import sqlite3
from db import queries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_tasks)
    print('БД подключена')
    conn.commit()
    conn.close()


def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_task, (task, ))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

