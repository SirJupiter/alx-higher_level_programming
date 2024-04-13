#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


def main():
    """Entry point function"""

    try:
        db_config = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        cursor = db_config.cursor()

        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"

        try:
            cursor.execute(query)
        except MySQLdb.Error as e:
            print("An error occurred: {}".format(e))
        else:
            result = cursor.fetchall()

            for row in result:
                print(row)

    except MySQLdb.Error as err:
        print("ERROR: Unable to connect to MySQL ({})".format(err))

    finally:
        if cursor:
            cursor.close()
        if db_config:
            db_config.close()


if __name__ == "__main__":
    main()
