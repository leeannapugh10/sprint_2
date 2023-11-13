'''
sqlite example for sprint 10, mod 1
'''
# Step 0 - import sqlite3
import sqlite3
import queries as q

# step 1 - Connect to the database
# triple check the spelling of your database filename
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - Make the "cursor"
cursor = connection.cursor()

# step 3 - Write a query
# QUERY = 'SELECT character_id, name FROM charactercreator_character;'
# see queries.py file

# step 4 - Execute the query on the cursor and fetch results
# "pulling the results" from the cursor
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])
