import mysql.connector


def connectToMySQL():
    cnx = mysql.connector.connect(password = 'pass', user='user')
    cursor = cnx.cursor()
    return cursor, cnx

def main():
    connectToMySQL()
    cursor, connection = connectToMySQL()
    print("State, Capitol, Population")
    cursor.execute("USE Info;")
    cursor.execute("SELECT * FROM states;")
    result = cursor.fetchone()
    while result is not None:
        print(result[0],result[1],result[2], sep=",")
        result = cursor.fetchone()

        
main()
