#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys


def main():
    """Main entry function"""

    try:
        db_config = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        cursor = db_config.cursor()

        query = "SELECT * FROM states WHERE name = '{}' \
            ORDER BY id ASC;".format(sys.argv[4])

        try:
            cursor.execute(query)
        except MySQLdb.Error as err:
            print("An error occurred: {}".format(err))
        else:
            results = cursor.fetchall()
            for row in results:
                print(row)

    except MySQLdb.Error as err:
        print("Error: Can't connect to Database ({})".format(err))

    finally:
        if cursor:
            cursor.close()
        if db_config:
            db_config.close()


if __name__ == "__main__":
    main()
