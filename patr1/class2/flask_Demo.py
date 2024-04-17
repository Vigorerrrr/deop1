# -*- coding: utf-8 -*-
# @file: flask_Demo.py
# @time: 2024 
# @user: Nemo
from flask import Flask

# 创建一个 Flask 应用实例
app = Flask(__name__)


# 定义路由，当访问根路径时返回 "Hello, World!"

@app.route('/')
def hello():
    return 'Hello, World!'

# 如果直接运行这个文件，则启动 Flask 服务器


if __name__ == '__main__':
    app.run(debug=True)
