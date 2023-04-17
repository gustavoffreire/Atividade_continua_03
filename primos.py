from flask import Flask, jsonify

app = Flask(__name__)

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

@app.route('/')
def numeros_primos():
    primos = []
    num = 2
    while len(primos) < 100:
        if primo(num):
            primos.append(num)
        num += 1
    
    return f"{primos}<br><br>Gustavo Emynem Izidre Ribeiro (RA: 2200826) | Gustavo Farias Freire (RA: 2201292)"

if __name__ == '__main__':
    app.run()
