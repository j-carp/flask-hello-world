from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! from Jessica in 3308'


@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://jc_database_user:P0NCJOjJNYstCiEBy2O3Ox8uSPf6vDCg@dpg-co6b5eq0si5c73cd2kng-a/jc_database")
    conn.close()
    return "Database Connection Successful"

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
        
        
        
        
        