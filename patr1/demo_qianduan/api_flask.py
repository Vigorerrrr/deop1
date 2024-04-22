# -*- coding: utf-8 -*-
# @file: api_flask.py
# @time: 2024 
# @user: Nemo
# 伪代码示例，使用Python和Flask框架
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/get-html-url', methods=['GET'])
def get_html_url():
    # 这里应该是你的逻辑来获取或生成HTML地址
    html_url = 'http://192.168.1.14:8899/309/index.html'
    return jsonify({'htmlUrl': html_url})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
