# TODO

import sqlite3
import sys

def fun(house_name):
    db = sqlite3.connect('students.db')
    cursor = db.cursor()
    # 执行查询语句
    cursor.execute("select first,middle,last,birth from students where house = (?) order by last,first",[house_name])
    res = cursor.fetchall()
    if len(res) == 0:
        print("not in the house list, please input the right house name!")
        return 0
    # 逐行打印
    for row in res:
        if row[1] == 'NULL':
            print(row[0],row[2],', born',row[-1])
        else:
            print(row[0],row[1],row[2],', born',row[-1])
    db.commit()
    db.close()

if __name__ == '__main__':
    house_name = sys.argv[1]
    fun(house_name)
