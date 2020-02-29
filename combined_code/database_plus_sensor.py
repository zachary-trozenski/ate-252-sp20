#Create database with 2 columns
# - Time Stamp
# - Infrared Reading (on or off, 1 or 0)
#Use rasberry pi sensors to insert data into database

import sqlite3
import datetime
import RPi.GPIO as GPIO
import time

def sensor_data():
    try:
        print("PIR MODULE TEST, CTRL + C TO CANCEL")
        time.sleep(2)
        print("READY")


        while True:
            if GPIO.input(PIR_PIN):
                sensor_signal = print("MOTION DETECTED", counter)
                counter += 1
            time.sleep(1)
            
    return sensor_signal

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

    PIR_PIN = 7
    GPIO.setup(PIR_PIN, GPIO.IN)

    counter = 0
    sensor_signal = sensor_data()
    insert_row('sensor_data.db', sensor_signal)
    print_table('sensor_data.db')

    except KeyboardInterrupt:
        print("Quit")
        GPIO.cleanup()
    
main()    
    
