"""
# -*- coding: utf-8 -*-
@Filename:pro_test.py
@SoftWare: PyCharm
# @user: Nemo

"""
import requests

from do_mysql_handler import do_mysql_saas3_super
from flask import Flask, request, render_template, jsonify, Response

app = Flask(__name__)



@app.route('/',methods=['get'])
def index():
    return render_template('html.html')


@app.route('/geturl',methods=['get'])
def geturl():
    sql1 = "SELECT report_url FROM `diff_coverage_report` WHERE job_record_uuid=308;"
    url_data = do_mysql_saas3_super(sql1)[0][0]

    return jsonify({'code': "1", "url": url_data, "msg":"成功"})


@app.route('/getdata',methods=['get'])
def getdata():
    url = "http://192.168.1.14:8899/308/index.html"
    response = requests.get(url)
    html_content = response.text
    return Response(html_content, content_type='text/html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)












