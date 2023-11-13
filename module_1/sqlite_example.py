'''
sqlite example for sprint 10, mod 1
'''
import sqlite3
import queries as q
import pandas as pd


# DB Connect function
def connect_to_db(db_name='rpg_db.sqlite3'):
    '''Connection function to for DB'''
    return sqlite3.connect(db_name)


def execute_q(conn, query):
    '''function to make cursor and execute query and pulling results'''
    curs = conn.cursor()
    curs.execute(query)
    return curs.fetchall()


# step 1 - Connect to the database
# triple check the spelling of your database filename
# connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - Make the "cursor"
# cursor = connection.cursor()

# step 3 - Write a query
# QUERY = 'SELECT character_id, name FROM charactercreator_character;'
# see queries.py file

# step 4 - Execute the query on the cursor and fetch results
# "pulling the results" from the cursor
# results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    conn = connect_to_db()
    print(execute_q(conn, q.SELECT_ALL))
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER)
    df = pd.DataFrame(results)
    df.columns = ['name', 'average_item_weight']
    print(df.head())
    df.to_csv('rpg_db.csv', index=False)
