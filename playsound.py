from flask import Flask
app = Flask(__name__)

import winsound 
message = "Now Playing"
@app.route("/")
def home():
    winsound.PlaySound("sample.wav",winsound.SND_ASYNC)
    return message 