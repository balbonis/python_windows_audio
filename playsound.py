from flask import Flask
app = Flask(__name__)

import winsound 
message = "Now playing audio using Windows system sound ...."
@app.route("/")
def home():
    winsound.PlaySound("sample.wav",winsound.SND_ASYNC)
    return message 
