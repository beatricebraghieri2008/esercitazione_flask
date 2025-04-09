import pandas as pd
from flask import Flask, render_template, request, redirect, url_for #importiamo la classe flask
app = Flask(__name__) #inizializza app flask




df= pd.read_csv("profilo.csv")
user= df. iloc[0].to_dict()

@app.route('/')
def home():
    return render_template("index.html", df=user)


@app.route('/modifica_profilo', methods=['GET'. 'POST'])
def modifica_profilo():
    return render_template("modifica.html")


if __name__ == '__main__':
    app.run(debug=True)
