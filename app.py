# Author: Jessica Carpenter
# April 2, 2024
# Render tutorial 3308

from flask import Flask
import psycopg2

app = Flask(__name__)

# Hello world page #########################################################################
@app.route('/')
def hello_world():
    return 'Hello, World! from Jessica in 3308'

# db test page #############################################################################
@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://jc_database_user:P0NCJOjJNYstCiEBy2O3Ox8uSPf6vDCg@dpg-co6b5eq0si5c73cd2kng-a/jc_database")
    conn.close()
    return "Database Connection Successful"

# create table page ##########################################################
@app.route('/db_create')
def creating():
        conn = psycopg2.connect("postgres://jc_database_user:P0NCJOjJNYstCiEBy2O3Ox8uSPf6vDCg@dpg-co6b5eq0si5c73cd2kng-a/jc_database")
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
            ''')
        conn.commit()
        conn.close()
        return "Basketball Table Successfully Created"

# insert into table page ####################################################################   
@app.route('/db_insert')
def inserting():
        conn = psycopg2.connect("postgres://jc_database_user:P0NCJOjJNYstCiEBy2O3Ox8uSPf6vDCg@dpg-co6b5eq0si5c73cd2kng-a/jc_database")
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            Values
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
        conn.commit()
        conn.close()
        return "Basketball Table Successfully Populated"

# query the data and return information ####################################################
@app.route('/db_select')
def selecting():
        conn = psycopg2.connect("postgres://jc_database_user:P0NCJOjJNYstCiEBy2O3Ox8uSPf6vDCg@dpg-co6b5eq0si5c73cd2kng-a/jc_database")
        cur = conn.cursor()
        cur.execute('''
            SELECT * FROM Basketball;
            ''')
        records = cur.fetchall()
        conn.close()
        response_string=""
        response_string+="<table>"
        for player in records:
            response_string+="<tr>"
            for info in player:
                response_string+="<td>{}</td>".format(info)
            response_string+="</tr>"
        response_string+="</table>"
        return response_string

# drop from table #########################################################################
@app.route('/db_drop')
def dropping():
        conn = psycopg2.connect("postgres://jc_database_user:P0NCJOjJNYstCiEBy2O3Ox8uSPf6vDCg@dpg-co6b5eq0si5c73cd2kng-a/jc_database")
        cur = conn.cursor()
        cur.execute('''
            DROP TABLE Basketball;
            ''')
        conn.commit()
        conn.close()
        return "Basketball Table Successfully Dropped"
        
  





