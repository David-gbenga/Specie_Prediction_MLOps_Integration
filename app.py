from flask import Flask,request, jsonify
import joblib
import os
from pathlib import Path

#Flask is used to create the web application.
#request is used to access data sent by the client, such as JSON input in a POST request.
#jsonify is used to return data from the server in JSON format.
#joblib It is used to load the saved machine learning model from a .pkl file.
#The os module is used for interacting with the operating system, such as files and directories.
#Path is used to work with file paths in a cleaner and more modern way than plain strings.


app = Flask(__name__)
MODEL_PATH = Path("artifacts/model.pkl")


if not MODEL_PATH.exists():
    # convenience: train model if not exists
    import train as _train
    _train.main()
    
    
model = joblib.load(MODEL_PATH)


@app.route("/health", methods =["GET"])  

def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods =["POST"])

def predict():
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error":"send JSON with key 'features'"}), 400
    #features = data.get()
    features = data["features"]
    
    try:
        features = [float(x) for x in features]
        pred = model.predict([features])
        return jsonify({"prediction":int(pred[0])})
    
    except Exception as e:
        return jsonify({"error" : str(e)}),500
    
if __name__ == "__main__":
        app.run(host= "0.0.0.0", port = 5001)
        
    
        
    
    
    


  