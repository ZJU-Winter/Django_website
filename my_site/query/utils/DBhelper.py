import pymysql


class dbhelper(object):
    def __init__(self):
        self.database_name = 'my_database'
        self.db = pymysql.connect(host="localhost", port=3306, user="root",
                                  password="dongdong", database=self.database_name)
        self.cursor = self.db.cursor()

    def update(self, sql):
        try:
            self.cursor.execute(sql, [])
            self.db.commit()
        except Exception as error:
            print(sql)
            print('修改失败')
            print(error)
            self.db.rollback()
            return False
        return True

    def query(self, sql, param=[]):
        try:
            self.cursor.execute(sql, param)
            return self.cursor.fetchall()
        except Exception as error:
            print(sql)
            print('查询失败')
            print(error)
            return None

    def close(self):
        self.cursor.close()
        self.db.close()
