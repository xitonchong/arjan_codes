import sqlite3
import logging



class SQLite():
    def __init__(self, file_name: str):
        self.file_name = file_name 
        self.connection = sqlite3.connect(file_name)

    def __enter__(self):
        logging.info("calling __enter__ ")
        return self.connection.cursor() 

    def __exit__(self, error: Exception, value: object, traceback: object):
        logging.info("calling __exit__")
        self.connection.commit()
        self.connection.close()




def main():
    logging.basicConfig(level=logging.INFO) 
    with SQLite(file_name="application.db") as cur: 
        cur.execute("SELECT * FROM blogs")
        logging.info(cur.fetchall())


if __name__ == '__main__':
    main()