# PyMySQL - um cliente MySQL feito em Python Puro
# Documentação: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import os

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="walisson22t69",
    database="base_de_dados",
    charset="utf8mb4"
)


with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ')'
        )
        # CUIDADO: Isso limpa a tabela
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Walisson', 19)
        result = cursor.execute(sql, data)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s) '
        )
        data2 = {
            "nome": "walisson",
            "idade": 59
        }
        result = cursor.execute(sql, data2)
        print(sql)
        print(data2)
        print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s) '
        )
        data3 = (
            {"nome": "Michael", "idade": 69},
            {"nome": "Fernanda", "idade": 82},
            {"nome": "Julia", "idade": 11},
        )
        result = cursor.executemany(sql, data3)
        print(sql)
        print(data3)
        print(result)
    connection.commit()
    
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ( "Siririca", 15),
            ("Clitores",  18),
        )
        result = cursor.executemany(sql, data4)
        print(sql)
        print(data4)
        print(result)
    connection.commit()

    # Lendo os valores com select
    with connection.cursor() as cursor:
        menor_id = input('Digite o menor id :')
        maior_id = input('Digite o maior id :')

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND  %s'
        )
        
        cursor.execute(sql, (menor_id, maior_id))
        data5 = cursor.fetchall()
        for row in data5:
            print(row)