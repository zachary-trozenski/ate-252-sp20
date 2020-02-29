#Create database with 2 columns
# - Time Stamp
# - Infrared Reading (on or off, 1 or 0)
#Use rasberry pi sensors to insert data into database

import sqlite3
import datetime

def create_table(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS sense_data (time text, ir_stat integer)")
    conn.commit()
    conn.close()

#Insert a row of data - function
def insert_row(db, ir_value):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    sql = str("INSERT INTO sense_data VALUES (datetime('now'), %d)" % ir_value)
    print('About to execute ', sql)
    c.execute(sql)
    conn.commit()
    conn.close()

def print_table(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM sense_data")
    print(c.fetchall())

def main():
    create_table('sensor_data.db')
    insert_row('sensor_data.db', 1)
    print_table('sensor_data.db')
    
main()    
    