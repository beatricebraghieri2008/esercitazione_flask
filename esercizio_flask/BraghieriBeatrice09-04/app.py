import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

df= pd.read_csv("profilo.csv").yo:dict(orient='records')

def trova_valore(utente_selezionato, valore):
    valori= df[utente_selezionato].values()
    lista= list(valori)
    return lista[valore]

def trova_chiave(valore):
    lista= list(vdf[0].keys()
    return lista[valore]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", 
                           nome = trova_valore(0,0), 
                           cognome = trova_valore(0,1), 
                           scuola = trova_valore(0,2), 
                           hobby = trova_valore(0,3), 
                           chiave3 = trova_chiave(2), 
                           chiave4 = trova_chiave(3))




@app.route('/modifica', methods=['POST'])
def modifica():
    return render_template("modifica.html")



if __name__ == '__main__':
    app.run(debug=True)
