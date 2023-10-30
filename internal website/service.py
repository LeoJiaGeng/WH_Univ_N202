from flask import Flask,render_template
 
app = Flask(__name__,template_folder='templates')
 
# 给前端模板传参
@app.route("/")
def index():
    data = {
        'name':'张三',
        'age':18,
        'mylist':[1,2,3,4,5,6,7]
    }
    # 以键值对的形式传参给模板index2.html
    # 左边是形参：data）；
    # 右边是我们给这个变量传的值（实参：字典data）；
    return render_template('index2.html',data=data)
 
@app.route('/template')
def template():  # put application's code here
    # 渲染
    return render_template('demo.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2020)