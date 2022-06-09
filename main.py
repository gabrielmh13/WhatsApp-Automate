from whatsapp import Whatsapp
from db import Database
from datetime import datetime

if __name__ == "__main__":
    db = Database('127.0.0.1', 'sc_teste', 'postgres', '123456')
    numbers = db.execQuery("SELECT DISTINCT cel FROM mensagens WHERE status = 0 AND fk_data = '" + datetime.today().strftime('%Y%m%d') + "'")

    for number in numbers:
        msgs = db.execQuery("SELECT msg FROM mensagens WHERE cel = '" + number[0] + "' AND fk_data = '" + datetime.today().strftime('%Y%m%d') + "'")
        wp = Whatsapp()
        wp.Browser(number[0], msgs)
        db.update("UPDATE mensagens SET status = 1 WHERE cel = '" + number[0] + "' AND fk_data = '" + datetime.today().strftime('%Y%m%d') + "'")

    db.close()