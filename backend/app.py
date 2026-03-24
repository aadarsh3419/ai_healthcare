from flask import Flask,request,jsonify
import mysql.connector
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Aadarsh#@3419",
    port = 3306,
    database = "healtcare"
)

cursor = db.cursor()
@app.route("/")
def home():
    return "backend running"

@app.route("/add",methods = ["POST"])
def add_data():
    data = request.json
    try:
        weight = float(data["weight"])
        bp = int(data["bp"])
        sugar = int(data["sugar"])
        sleep = float(data["sleep"])
        steps = int(data["steps"])
    except:
        return jsonify({"error":"invalid input"}),400
    if weight<=0 or sleep<=0 or steps<=0 or sugar<=0 or bp<=0 :
        return jsonify({"error":"invalid values"}),400
    

    

    query = """
insert into health_data(weight,bp,sugar,sleep,steps)
values (%s,%s,%s,%s,%s)"""

    cursor.execute(query,(weight,bp,sugar,sleep,steps))
    db.commit()

    return jsonify({"message":"data added sucessfully"})

if __name__=='__main__':
    app.run(debug=True)