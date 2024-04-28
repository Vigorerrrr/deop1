"""
# -*- coding: utf-8 -*-
@Filename:do_mysql_handler.py
@SoftWare: PyCharm
# @user: Nemo

"""

import pymysql


def do_mysql_saas3_super(sql_data):
    db_config = {
        'host': '192.168.1.14',
        'port': 3306,
        'user': 'root',
        'pwd': '123456',
        'db': 'super-jacoco',
        'charset': 'utf8'
    }

    db = pymysql.connect(host=db_config['host'],
                         port=db_config['port'],
                         user=db_config['user'],
                         password=db_config['pwd'],
                         database=db_config['db'],
                         charset=db_config['charset'])
    cursor = db.cursor()
    # sql = "SELECT * FROM cl_loan_order WHERE order_no='2023052413295040810548'"
    cursor.execute(sql_data)
    db.commit()
    result = []
    for i in cursor.fetchall():
        result.append(i)

    db.close()
    return result


if __name__ == '__main__':

    sql1 = "SELECT report_url FROM `diff_coverage_report` WHERE job_record_uuid=308;"
    order_no = do_mysql_saas3_super(sql1)[0][0]
    print(order_no)

