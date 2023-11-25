# from flask import Flask,redirect,url_for,request,render_template

# app=Flask(__name__)

# @app.route('/Ak')
# def func1():
#     return render_template('redirecth.html')

# @app.route('/redirect_check', methods = ["POST"] )  
# def validate():  
#     if request.method == 'POST' and request.form['username'] == 'Akansha' and request.form['password'] == '1705': 

#         return redirect(url_for("success"))  
#     else:
#        return redirect(url_for("invalid"))  

# @app.route('/success')
# def success():
#      return "Logged in Successfully!"

# @app.route('/invalid')
# def invalid():
#      return "Invalid credentials - login failed!"

# if __name__=='__main__':
#      app.run(debug=True)

from flask import Flask, redirect, url_for, request, render_template, jsonify

app = Flask(__name__)

@app.route('/Ak')
def func1():
    return render_template('redirecth.html')

@app.route('/redirect_check', methods=["POST"])
def validate():
    if request.method == 'POST' and request.form['username'] == 'Akansha' and request.form['password'] == '1705':
        return jsonify({"message": "Logged in Successfully!"})
    else:
        return jsonify({"message": "Invalid credentials - login failed!"})

@app.route('/success')
def success():
    return "Logged in Successfully!"

@app.route('/invalid')
def invalid():
    return "Invalid credentials - login failed!"

if __name__ == '__main__':
    app.run(debug=True)
