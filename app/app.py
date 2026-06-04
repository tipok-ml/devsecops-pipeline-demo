#!/usr/bin/env python3
import os
from flask import Flask, request
import sqlite3
app = Flask(__name__)

# "Случайно" закомментированный токен, который найдёт Gitleaks
# SECRET_API_TOKEN = "ghp_FAKETOKEN1234567890"

def get_db():
    conn = sqlite3.connect('users.db')
    return conn

@app.route('/')
def index():
    return '<form method="GET" action="/greet"><input name="user" placeholder="Введите имя"><button>Поприветствовать</button></form>'

@app.route('/greet')
def greet():
    user = request.args.get('user', 'Гость')
    # Уязвимость: SQL-инъекция из-за прямой подстановки в запрос
    query = f"SELECT * FROM users WHERE name = '{user}'"
    conn = get_db()
    cur = conn.execute(query)
    row = cur.fetchone()
    if row:
        return f"Привет, {row[1]}!"
    return f"Привет, {user}!"
