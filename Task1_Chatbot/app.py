from flask import Flask,render_template,request
from chatbot import chatbot_response


app=Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")



@app.route("/chat",methods=["POST"])
def chat():

    msg=request.form["msg"]

    reply=chatbot_response(msg)

    return reply



app.run(debug=True)