from flask import Flask, request, json
from app import app

if __name__ == '__main__':
	app.secret_key = 'shradhataneja'
	app.run(debug=True)
    # app.config['SESSION_TYPE'] = 'filesystem'

