from database import *
from os import urandom
from flask import Flask, render_template, url_for , request ,session, escape, request, redirect

app = Flask(__name__)

app.secret_key = urandom(24)




@app.route('/')
def Home_page():
    return render_template('home.html' ,  username=session.get('username'))

@app.route('/F.A.Q')
def FAQ_page():
    return render_template('F.A.Q.html' ,  username=session.get('username'))

@app.route('/Register', methods=['GET', 'POST'])
def Register():
	if request.method== 'GET':
		return render_template('Register.html')
	else:	
		fname = request.form['txb_fname']
		lanme = request.form['txb_lname']
		username = request.form['txb_username']
		password = request.form['txb_pass']
		cheack_password = request.form['txb_cpass']
		cheack_user=query_by_name(username)
		if password ==cheack_password:	
			if cheack_user==None:		
				Login(fname , lanme , username , password)
				session['username']=username
				return redirect(url_for('Home_page' ))
			else:
				return render_template('Register.html' , taken='this user name is taken')
		else:
			return render_template('Register.html' , dont_match=  'The confirm password confirmation does bot match ')

@app.route('/Login', methods=['GET' , 'POST'])
def LogIn_page():
	if request.method== 'GET':
		return render_template('Login.html')
	else:	
		username = request.form['txb_uname']
		password = request.form['txb_pass']
		u=query_by_name(username)
		if u is not None and u.uname==username and u.password==password:
			session['username']=username
			return redirect(url_for('get_session' ))
		else:

			return render_template('Login.html' , wrong='wrong password or username')

@app.route('/session' , methods=['GET' , 'POST'])
def get_session():
	if session.get('username')==None:
		return redirect(url_for('LogIn_page'))
	if request.method== 'GET':
		return render_template('Session.html' , username=session.get('username') )
	else:	
		Element = request.form['Elements']
		Different_element =request.form['txb_different_ex']
		Date = request.form['txb_Date']
		Time = request.form['']
		u=session.get('username')
		add_session( Different_element, Element ,  session.get('username') ,Date, Time)
		posts = query_session_by_user( session.get('username'))
		return redirect(url_for('get_session'))	

@app.route('/upperbudy')
def upperbudy_ex():
    return render_template('upperbudy.html' ,  username=session.get('username'))

@app.route('/LowerBody')
def LowerBody_ex():
    return render_template('LowerBody.html' ,  username=session.get('username'))

@app.route('/CoreBody')
def CoreBody_ex():
    return render_template('CoreBody.html' ,  username=session.get('username'))

@app.route('/Pushupsvar')
def Pushupsvar_ex():
    return render_template('Pushupsvar.html' ,  username=session.get('username'))
		

@app.route('/sign_out')
def sign_out():
	if session.get('username')==None:
		return redirect(url_for('Home_page' ))
	else:	
	    session.pop('username')
	    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)