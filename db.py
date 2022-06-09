import psycopg2 as pg

class Database:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

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