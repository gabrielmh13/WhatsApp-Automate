import psycopg2 as pg
import json
import pathlib

class Database:
    def __init__(self):
        config = str(pathlib.Path(__file__).parent.resolve()) + '\config.json'
        with open(config, 'r') as config:
            cred = json.load(config)

        self.host = cred['host']
        self.port = cred['port']
        self.database = cred['database']
        self.user = cred['user']
        self.password = cred['password']

        self.conn = pg.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def execQuery(self, query):
        self.cur.execute(query)
        self.results = self.cur.fetchall()
        return list(self.results)
    
    def update(self, query):
        self.cur.execute(query)

    def close(self):
        self.conn.close()