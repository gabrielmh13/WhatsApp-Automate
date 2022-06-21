from whatsapp import Whatsapp
from db import Database
from datetime import datetime
import sys
import json
import pathlib

if __name__ == "__main__":
    config = str(pathlib.Path(__file__).parent.resolve()) + '\config.json'
    with open(config, 'r') as config:
        cred = json.load(config)
        
    verify_numbers = []

    db = Database()
    numbers = db.execQuery("SELECT DISTINCT mobile_phone FROM ocean_cfg.msg_whatsapp_log WHERE send_ok = 0 AND date_send = '" + datetime.today().strftime('%Y%m%d') + "'")

    wp = Whatsapp()
    wp.browser(numbers, db, verify_numbers, cred['company'])

    db.close()
    
    sys.exit()