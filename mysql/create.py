import mysql.connector

def connectToMySQL():
    cnx = mysql.connector.connect(password = 'pass', user='user')
    cursor = cnx.cursor()
    return cursor, cnx

def createDatabase(cursor, DB_NAME):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def makeTable(cursor):
    infile = open("states.txt", "r")
    line = infile.readline()
    line = line.strip()
    fields = line.split(",")
    sql = "CREATE TABLE states (" + fields[0] + " VARCHAR(20), " + fields[1] + " VARCHAR(20), " + fields[2] + " INT);"
    print(sql)
    cursor.execute(sql)
    infile.close()
    print("states table created")


def insertData(cursor):
    infile = open("states.txt", "r")
    header = infile.readline() 
    for line in infile:
        sql = ""
        line = line.strip()
        record = line.split(",")
        data = "'"
        data = "'" + record[0] + "', "
        data += "'" + record[1] + "', "
        data += "'" + record[2] + "'"
  
        sql = "INSERT INTO states VALUES (" + data + ");"
        cursor.execute(sql)
    infile.close()
    print("state data inserted into state table")


def main():
    DB_NAME = 'Info'
    cursor, connection = connectToMySQL()
    createDatabase(cursor, DB_NAME)  # comment this line after first successful run
    cursor.execute("USE {}".format(DB_NAME))
    makeTable(cursor)   # comment this line after first successful run
    insertData(cursor)  # comment this line after first successful run
    

    # don't modify below this line
    connection.commit()
    cursor.close()
    connection.close()

main()

