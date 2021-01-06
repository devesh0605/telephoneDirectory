def bycontact(s):
    import sqlite3
    try:
        direct = sqlite3.connect('directory.db')
        sql = "SELECT * from details WHERE contact='" + s + "';"
        curse = direct.cursor()
        curse.execute(sql)
        record = curse.fetchone()
        if record!=None:
            sql = "DELETE FROM details WHERE contact='" + str(s) + "';"
            curse.execute(sql)
            direct.commit()
            return ('Number deleted')
        else:
            return ('Number does not exist')


    except:
        return ("Error in operation.")
        direct.rollback()
    direct.close()


