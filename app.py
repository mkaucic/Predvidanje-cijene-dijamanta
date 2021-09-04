from operator import pos
from os import environ
from flask import Flask , render_template, request, redirect, url_for, jsonify
import urllib
import urllib.request as urlrequest
import json
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for('index'))

@app.route("/index", methods = ['GET','POST'])
def index(): 
    if request.method == "POST":
        data = request.form
        cut = data['cut']
        color = data['color']
        clarity = data['clarity']
        carat = data['carat']
        depth = data['depth']
        table = data['table']
        x = data['x']
        y = data['y']
        z = data['z']
       
        price = None
        
        data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["carat", "cut", "color", "clarity", "depth", "table", "price", "x", "y", "z"],
                    "Values": [ [ carat, cut, color, clarity, depth, table, "0", x, y, z ] ]
                },        },
            "GlobalParameters": {
}
    }

        body = str.encode(json.dumps(data))

       
        url = 'https://ussouthcentral.services.azureml.net/workspaces/5641075c2a6e47dcb6f77c73ab015a96/services/bd8b034095b24bd5b1ec84f7c4b5719b/execute?api-version=2.0&details=true'
        api_key = 'hZkFZBcDqOstKUFFf66uc0bQxZwGEvcXru8MFYelUn5XBRrN+DP3dub7VrdHxlXhNxBDhxXoGuYAlwzIdIOvEg==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urlrequest.Request(url, body, headers) 

        try:
            response = urlrequest.urlopen(req)

            result = json.loads(response.read())
            price = float(result['Results']['output1']['value']['Values'][0][10])
            price = "{:.2f}".format(price)
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            print(error.info())

            print(json.loads(error.read()))         

        return render_template("index.html", cijena=price)
        
    return render_template("index.html")
       

    


if __name__=="__main__":
    app.run(debug=True)