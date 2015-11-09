#db_check

import sqlite3


# Connect to database
conn = sqlite3.connect('file_verify.db')

def createTable():
	conn.execute("CREATE TABLE if not exists FILE_INFO \
	(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
		ACTION_DATE TEXT, \
		ACTION_TAKEN TEXT \
		);")
		
def newEntry(action_date, action_taken):
	# Create values part of sql command
	val_str = "'{}', '{}'".format(action_date, action_taken)
	
	sql_str = "INSERT INTO FILE_INFO (ACTION_DATE, ACTION_TAKEN) VALUES ({});".format(val_str)
	
	print sql_str
	
	conn.execute(sql_str)
	conn.commit()
	return conn.total_changes
	
def viewLastCheck(action_date):

        # Create sql string
        sql_str = "SELECT ACTION_DATE FROM FILE_INFO WHERE ACTION_TAKEN = 'Check' ORDER BY ID DESC LIMIT 1"
        cursor = conn.execute(sql_str)
	
	# Get data from cursor in array
        row = cursor.fetchall()

        for a in row:
                for i in a:
                        action_date.append(i)

        return action_date

def viewLastMove(move_date):

        # Create sql string
        sql_str = "SELECT ACTION_DATE FROM FILE_INFO WHERE ACTION_TAKEN = 'Move' ORDER BY ID DESC LIMIT 1"
        cursor = conn.execute(sql_str)
	
	# Get data from cursor in array
        row = cursor.fetchall()

        for a in row:
                for i in a:
                        move_date.append(i)

        return move_date

        
'''	
def updateCharacter(chage_id, anem, gender, age, occupation):
	# Create values part of sql command
	val_str = "NAME='{}', GENDER='{}', AGE='{}', OCCUPATION='{}'.format(name, gender, age, occupation)"
	
	sql_str = "UPDATE SIMPSON_INFO set {} where ID= {};".format(val_str, change_id)
	
	print sql_str
	
	conn.execute(sql_str)
	conn.commit()
	return conn.total_changes

def deleteCharacter(change_id):
	# Create sql string
	sql_str = "DELETE from SIMPSON_INFO where ID={}".format(change_id)
	conn.execute(sql_str)
	conn.commit()
	return conn.total_changes
'''
	
createTable()
