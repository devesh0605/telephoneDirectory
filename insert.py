


def insertinfo(a, b, c, d):
    import sqlite3
    try:
        direct = sqlite3.connect('directory.db')
        curse = direct.cursor()
        curse.execute("INSERT INTO details (firstName, lastName, contact, address) VALUES(?,?,?,?);",
                      (a, b, c, d))
        direct.commit()
        return ("One record added successfully.")
    except:
        return ("Entry alredy exist")
        direct.rollback()
    direct.close()

