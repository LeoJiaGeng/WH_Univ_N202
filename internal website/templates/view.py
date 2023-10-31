from flask import Flask,render_template,request,session,redirect,url_for
 
app = Flask(__name__,template_folder='templates')

# 主界面index 
@app.route('/template', methods=["GET"])
def template():  # put application's code here
    # 渲染
    return render_template('demo.html')

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

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2020)