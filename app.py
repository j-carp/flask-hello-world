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
