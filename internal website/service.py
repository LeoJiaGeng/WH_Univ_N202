from flask import Flask,render_template,request,session,redirect,url_for
 
app = Flask(__name__,template_folder='templates')
app.secret_key='any random string'    #这里我们直接给定一个密钥

user = {"cao":"123"}

# 给前端模板传参，同时接收超链接传入参数
@app.route("/index1/<a>", methods=["GET"])
def index(a):
    data = {
        'name':'张三',
        'age':18,
        'mylist':[1,2,3,4,5,6,7],
        'receivers':a
    }
    # 以键值对的形式传参给模板index2.html
    # 左边是形参：data）；
    # 右边是我们给这个变量传的值（实参：字典data）；
    return render_template('index2.html',data=data)

# 主界面index 
@app.route('/template', methods=["GET"])
def template():  # put application's code here
    # 渲染
    return render_template('index.html')

# 显示登录界面
@app.route('/login')
def login_gui():  # put application's code here
    # 渲染
    return render_template('login.html')

# 登录逻辑界面：确认用户名和密码，可以链接数据库，目前不使用
@app.route('/loginProcess',methods=['POST','GET'])
def login_process_page():
    if request.method == 'POST':
        nm=request.form['nm']     #获取姓名文本框的输入值
        pwd=request.form['pwd']   #获取密码框的输入值
        if nm=='cao' and pwd==user['cao']:
            session['username']=nm             #使用session存储方式，session默认为数组，给定key和value即可            
            return redirect(url_for('template'))  #重定向跳转到首页
        else:
            return 'the username or user_pwd does not match!'

@app.route('/logout')
def logout():
    # res.delete_cookie('username')
    session.pop('username')
    return redirect(url_for('template'))

@app.route('/software')
def software():

    return render_template('software.html') 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2020)