from flask import Flask, render_template, request, jsonify
import numpy as np
import diamonds_predictionmodel as dp
from dotenv import load_dotenv

app = Flask(__name__)



@app.route("/index", methods = ['GET','POST'])
def Home(): 
    if request.method == "POST":
        data = request.form
        carat = data['carat']
        depth = data['depth']
        table = data['table']
        x = data['x']
        y = data['y']
        z = data['z']
        
        numbers  = np.array([carat,depth,table,x,y,z])

        diamond_price = dp.diamond_prediction(numbers)
        print(diamond_price)

    return render_template("index.html", cijena = diamond_price)


if __name__=="__main__":
    app.run(debug=True)