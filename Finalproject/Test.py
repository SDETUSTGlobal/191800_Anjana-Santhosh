from flask import Flask, render_template, request
from flask_mysqldb import MySQL

dbd = Flask(__name__)

dbd.config['MYSQL_HOST'] = 'localhost'
dbd.config['MYSQL_USER'] = 'root'
dbd.config['MYSQL_PASSWORD'] = 'root'
dbd.config['MYSQL_DB'] = 'fproject'

mysql = MySQL(dbd)


@dbd.route('/', methods=['GET', 'POST'])
def nav():
    if request.method == "POST":
        info = request.form
        l = info['a']
        m = info['b']
        n = info['c']
        o = info['d']
        p = info['e']

        connect = mysql.connection.cursor()
        connect.execute("INSERT INTO details(Fullname, UID , Company, Email, password1) VALUES (%s, %s, %s, %s, %s)",
                        (l, m, n, o, p))
        mysql.connection.commit()
        connect.close()
        return render_template('login.html', w=l, x=m, y=n, z=o, za=p)
    return render_template('index.html')


@dbd.route('/login')
def page():
    return render_template('login.html')



if __name__ == '__main__':
    dbd.run()
