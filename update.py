def bycontact(s, w, x, y, z):
    import sqlite3
    try:
        direct = sqlite3.connect('directory.db')
        sql = "SELECT * from details WHERE contact='" + s + "';"
        curse = direct.cursor()
        curse.execute(sql)
        record = curse.fetchone()
        if record!=None:
            sql = "UPDATE details SET firstName='" + str(w) + "', lastName='" + str(x) + "', contact='" + str(
                y) + "', address='" + str(z) + "' WHERE contact='" + str(s) + "';"
            curse.execute(sql)
            direct.commit()
            return ('updated now')
        else:
            return ('Number does not exist')


    except:
        return ("Error in operation.")
        direct.rollback()
    direct.close()



