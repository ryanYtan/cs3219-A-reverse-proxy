import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_name():
    names = ["Mr. Mittens", "McFluffes", "M.C Escher", "Mayonnaise"]
    return random.choice(names)

if __name__  == "__main__":
    # has to correspond to port being exposed in dockerfile
    app.run(host="0.0.0.0", port="5001")
