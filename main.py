from whatsapp import Whatsapp
from db import Database
from datetime import datetime

if __name__ == "__main__":
    db = Database()
    numbers = db.execQuery("SELECT DISTINCT cel FROM mensagens WHERE status = 0 AND fk_data = '" + datetime.today().strftime('%Y%m%d') + "'")

    wp = Whatsapp()
    wp.browser(numbers, db)

    db.close()