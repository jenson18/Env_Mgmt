import sqlite3

db = sqlite3.connect('VAPP.db')
cr=db.cursor()
cr.execute("create table ENV(VAPP text, BSS_NON_CPQ text, CPQ_OSS_SIO text, ARM text,DB_SERVERS text,COMMENTS text)")
db.commit()
db.close()