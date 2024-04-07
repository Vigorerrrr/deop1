from flask import Flask
import json

app = Flask(__name__)

# 定义路由，返回 HTML 数据连接


@app.route('/get_html_link')
def get_html_link():
    html_link = 'http://192.168.1.14:8899/309/index.html'  # 替换成实际的 HTML 数据连接
    response = {'html_link': html_link}
    return json.dumps(response)

# 定义路由，返回要展示的 HTML 数据


@app.route('/display_html')
def display_html():
    html_data = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML 数据展示</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is some HTML data displayed by a Flask app.</p>
        </body>
        </html>
    """
    return html_data


if __name__ == '__main__':
    app.run(debug=True)

