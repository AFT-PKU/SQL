# TODO

import sqlite3
import pandas as pd
import sys

def build_db(file_name):
    if file_name != 'characters.csv':
        print("read error!")
        return 0
    data = pd.read_csv(file_name)
    df = pd.DataFrame(data)

    db = sqlite3.connect('students.db')
    cursor = db.cursor()
    for i in range(df.shape[0]):
        house_ = df['house'][i]
        birth_ = int(df['birth'][i])

        name = df['name'][i].split(" ")
        first_ = name[0]
        if len(name) == 2:
            middle_ = "NULL"
            last_ = name[1]
        elif len(name) == 3:
            middle_ = name[1]
            last_ = name[2]

        cursor.execute("INSERT INTO students (first,middle,last,house,birth) VALUES (?,?,?,?,?) ",[first_,middle_,last_,house_,birth_])
    db.commit()
    db.close()


if __name__ == '__main__':
    file_name = sys.argv[1]
    build_db(file_name)