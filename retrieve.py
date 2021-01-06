def byfirstname(x):
    strfname = ''
    strlname = ''
    strcont = ''
    stradd = ''
    import sqlite3
    try:
        direct = sqlite3.connect('directory.db')
        sql = "SELECT * from details WHERE firstName='" + x + "';"
        curse = direct.cursor()
        curse.execute(sql)
        result = curse.fetchall()
        for record in result:
            strfname = strfname + str(record[0]) + '\n'
            strlname = strlname + str(record[1]) + '\n'
            strcont = strcont + str(record[2]) + '\n'
            stradd = stradd + str(record[3]) + '\n'

        if strcont != '':
            f = [strfname, strlname, strcont, stradd]
            return f
        else:
            return 0
    except:
        print("Error in operation.")
        direct.rollback()
    direct.close()


def bylastname(x):
    strfname = ''
    strlname = ''
    strcont = ''
    stradd = ''


    import sqlite3
    try:
        direct = sqlite3.connect('directory.db')
        sql = "SELECT * from details WHERE lastName='" + x + "';"
        curse = direct.cursor()
        curse.execute(sql)
        result = curse.fetchall()
        for record in result:
            strfname = strfname + str(record[0]) + '\n'
            strlname = strlname + str(record[1]) + '\n'
            strcont = strcont + str(record[2]) + '\n'
            stradd = stradd + str(record[3]) + '\n'

        if strcont != '':
            f = [strfname, strlname, strcont, stradd]
            return f
        else:
            return 0


    except:
        print("Error in operation.")
        direct.rollback()
    direct.close()


def bycontact(x):
    strfname = ''
    strlname = ''
    strcont = ''
    stradd = ''

    import sqlite3
    try:
        direct = sqlite3.connect('directory.db')
        sql = "SELECT * from details WHERE contact='" + x + "';"
        curse = direct.cursor()
        curse.execute(sql)
        result = curse.fetchall()
        for record in result:
            strfname = strfname + str(record[0]) + '\n'
            strlname = strlname + str(record[1]) + '\n'
            strcont = strcont + str(record[2]) + '\n'
            stradd = stradd + str(record[3]) + '\n'

        if strcont!='':
            f = [strfname, strlname, strcont, stradd]
            return f
        else:
            return 0



    except:
        print("Error in operation.")
        direct.rollback()
    direct.close()



