from contextlib import closing
from typing import Callable
import psycopg
import logging
import os

def get_logger(level:logging):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=level)
    logger = logging.getLogger("uvicorn")
    logger.setLevel(level)
    return logger

# init logger
logger = get_logger(logging.INFO)

class Database:

    def __init__(self, env:str = 'dev'):

        # make sure password is in env
        password = os.getenv('SUPABASE_DB_PASS')
        assert password

        # assemble credentials
        self.env = env
        if env == 'dev':
            
            logger.info('Loading credentials for development database')

            self.credentials = {
                'user': 'postgres.qsdqlenrrnmbtmgkqwbp',
                'password': password,
                'host': 'aws-0-us-west-1.pooler.supabase.com',
                'port': 6543,
                'dbname': 'postgres'
            }

        elif env == 'prod':
            ...
        else:
            raise ValueError('Unknown environment selected when initializing database. Select `prod` or `dev`.')

        for k,v in self.credentials.items():
            v = f"{v[:3]}***" if k == 'password' else v
            logger.info(f"{k}: {v}")

        self.connected = False

    def connect(self):

        target = f"{self.credentials['host']}/{self.credentials['dbname']}"
        logging.info(f"Connecting to {target}")

        try:
            self.conn = psycopg.Connection.connect(**self.credentials)
        except Exception as e:
            logging.critical(f"Unable to connect:\n{e}")
        finally:
            self.connected = True

    def is_connected(self):
        return self.connected and self.conn and not self.conn.closed

    def close(self):
        if self.connected:
            try:
                self.conn.close()
            except:
                ...

    def execute(self, statement:str):
        
        logger.info(f"Query -> {statement}")
        if not self.is_connected():
            self.connect()

        try:
            with closing(self.conn.cursor()) as curs:
                curs.execute(statement)
                data = curs.fetchall()
    
                return [d for d in data] if data else None
                
        except Exception as e:
            ...

if __name__=="__main__":

  ...