import logging 
import sqlite3 
from contextlib import contextmanager 



@contextmanager 
def open_db(file_name: str):
    conn = sqlite3.connect(file_name)
    try:
        logging.info("creating connection")
        yield conn.cursor() 
        try: 
            conn.commit() 
            logging.info("commiting db ..")
        except: 
            logging.info("error with saving db")
    finally:
        conn.close()
        logging.info("closed db ")

def main():
    logging.basicConfig(level=logging.INFO)
    with open_db(file_name="application.db") as cursor:
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


if __name__ == '__main__':
    main() 
