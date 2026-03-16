from flask import Flask
from app import Board

app = Flask("checkers")


@app.route("/")
def main():
    board = Board()
    return repr(board)
