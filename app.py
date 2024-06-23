from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

DATABASE = "webtags.db"


def create_connection(db_filename):
    try:
        connection = sqlite3.connect(db_filename)
        return connection
    except Error as e:
        print(e)
        return None


@app.route('/')
def render_home_page():  # put application's code here
    return render_template('base.html')


@app.route('/display\<table_type>')
def render_display_page(table_type):  # put application's code here

    query = ("SELECT player_name, team_abbreviation, age, player_height,"
             " player_weight, college, country, points, assists, rebounds, season FROM ?")
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, (table_type, ))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('display.html', data=data_list)


if __name__ == '__main__':
    app.run()