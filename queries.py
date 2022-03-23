import psycopg2
import os

def insert_data_to_db(func):
    try:
        DATABASE_URL = 'postgres://xvgvrxzrfffhil:e1e56958e248c55623ff1dd7da953a9de00c0493eca529210377ccec4ad91eb9@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/d3aubcndgja659'
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        """conn = psycopg2.connect(dbname='postgres', user='postgres',
                                password='postgres', host='localhost')"""
        cursor = conn.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS banks'
                        '(id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, '
                        'day DATE NOT NULL DEFAULT CURRENT_DATE, '
                        'name_bank VARCHAR(10) NOT NULL, '
                        'country VARCHAR(3) NOT NULL, '
                        'usd_buy FLOAT, usd_sell FLOAT, '
                        'euro_buy FLOAT, euro_sell FLOAT, '
                        'lira_buy FLOAT, lira_sell FLOAT)')
    except:
        print("Ошибка при работе с PostgreSQL")

    data_list = [item[1] for item in func().items()]

    sql = f'INSERT INTO BANKS (day, name_bank, country, usd_buy, usd_sell, ' \
          'euro_buy, euro_sell, lira_buy, lira_sell) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'

    cursor.execute(sql, data_list)
    conn.commit()
    cursor.close()


def select_data_foreign_banks_db():
    query = f"SELECT name_bank, country, usd_buy, usd_sell, euro_buy, euro_sell " \
			f"FROM banks WHERE day = CURRENT_DATE AND country <> 'gel'"
    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        """conn = psycopg2.connect(dbname='postgres', user='postgres',
								password='postgres', host='localhost')"""
        cursor = conn.cursor()
        cursor.execute(query)
        sql_list = cursor.fetchall()
        conn.commit()
        cursor.close()
    except:
        print("Ошибка при работе с PostgreSQL")
        return 'Ошибка при работе с PostgreSQL'
    for item in sql_list:
        if item[1] == None or type(item[1]) == 'NoneType':
            sql_list.remove(item)

    answer_message = f'Курсы Валют в других странах: \n'
    for item in sql_list:
        answer_message += f'{item[0].capitalize().strip()} \nUSD {item[2]} || {item[3]} {item[1].upper()}\n' \
						  f'EUR {item[4]} || {item[4]} {item[1].upper()}\n'
    return answer_message


def select_data_from_db(currency):
    phrases_dict = {'usd_sell': 'продают доллары', 'usd_buy': 'покупают доллары', 'euro_sell': 'продают евро',
                    'euro_buy': 'покупают евро', 'lira_sell': 'продают лиры', 'lira_buy': 'покупают лиры'}

    query = f"SELECT name_bank, {currency} FROM banks WHERE day = CURRENT_DATE AND country = 'gel'"
    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        """conn = psycopg2.connect(dbname='postgres', user='postgres',
                                password='postgres', host='localhost')"""

        cursor = conn.cursor()
        cursor.execute(query)

        sql_list = cursor.fetchall()

        conn.commit()
        cursor.close()
    except:
        print("Ошибка при работе с PostgreSQL")
        return 'Ошибка при работе с PostgreSQL'

    for item in sql_list:
        if item[1] == None or type(item[1]) == 'NoneType':
            sql_list.remove(item)

    sql_list.sort(key=lambda x: (x[1], x[0]))

    answer_message = f'Банки {phrases_dict[currency]} по следующему курсу: \n'
    for item in sql_list:
        answer_message += f'{item[0].capitalize().strip()} : {item[1]} \n'
    return answer_message

def update_data_db(bank_dict):
    bank_dict = bank_dict()
    bank = [bank_dict['usd_buy'], bank_dict['usd_sell'], bank_dict['euro_buy'], bank_dict['euro_sell'],
            bank_dict['lira_buy'], bank_dict['lira_sell'], bank_dict['name_bank']]
    update = f'UPDATE banks SET ' \
             f'usd_buy = %s,' \
             f'usd_sell = %s,' \
             f'euro_buy = %s,' \
             f'euro_sell = %s,' \
             f'lira_buy = %s,' \
             f'lira_sell = %s' \
             f' WHERE day = CURRENT_DATE AND name_bank = %s;'

    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    """conn = psycopg2.connect(dbname='postgres', user='postgres',
                                password='postgres', host='localhost')"""
    cursor = conn.cursor()
    cursor.execute(update, bank)

    conn.commit()
    cursor.close()



