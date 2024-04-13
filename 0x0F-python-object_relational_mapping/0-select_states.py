"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def main():
    args_list = sys.argv

    try:
        db_config = MySQLdb.connect(
            host='localhost',
            user=args_list[1],
            passwd=args_list[2],
            db=args_list[3]
        )

        cursor = db_config.cursor()
        query = "SELECT * FROM states ORDER BY id ASC;"
        try:
            cursor.execute(query)
        except Exception as e:
            print("Error executing query: {}".format(e))
        else:
            result = cursor.fetchall()
            for row in result:
                print(row)

    except MySQLdb.Error as err:
        print("MySQL Error {:d}: {:s}".format(err.args[0], err.args[1]))

    finally:
        # Closing connection and cursor
        cursor.close()
        db_config.close()


if __name__ == "__main__":
    main()
