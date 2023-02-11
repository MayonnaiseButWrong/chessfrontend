from flask import Flask

app =Flask(__name__)

@app.route('/ChessGame')
def get_chess_game():
    return {'data':'I am data and i am cool'}