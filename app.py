import os
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from dotenv import load_dotenv
# from flask_sqlalchemy import SQLAlchemy


CREATE_PLAYERS_TABLE = (
    "CREATE TABLE IF NOT EXISTS players (player_id SERIAL PRIMARY KEY, player_name VARCHAR(2")

load_dotenv()


app = Flask(__name__)
url = os.getenv('DATABASE_URL')
connection = psycopg2.connect(url)


@app.route('/')
def home():
    return "hello, world!"


def create_players_table():
    cursor = connection.cursor()

    create_table_query = (
        "CREATE TABLE IF NOT EXISTS players ("
        "player_id SERIAL PRIMARY KEY, "
        "player_name VARCHAR(255), "
        "height INTEGER, "
        "weight INTEGER, "
        "college VARCHAR(255), "
        "team VARCHAR(255), "
        "position VARCHAR(10), "
        "mpg FLOAT, "
        "rpg FLOAT, "
        "apg FLOAT, "
        "spg FLOAT, "
        "bpg FLOAT, "
        "tpg FLOAT, "
        "ppg FLOAT"
        ")"
    )

    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    create_players_table()
    app.run()
