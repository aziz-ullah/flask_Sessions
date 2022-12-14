from flask import Flask,redirect,render_template,request,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user', usr = user))
    else:
        return render_template('login.html')
    
@app.route('/<usr>')
def user(usr):
    return render_template('welcome.html', usr=usr)






if __name__ == '__main__':
    app.run(debug=True)

