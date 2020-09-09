import random
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_image():
    urls = ["test1", "test2", "test3", "test4"]

    return {
        "imgsrc": random.choice(urls),
        "imgcap": request.args.get("name")
    }

if __name__  == "__main__":
    # has to correspond to port being exposed in dockerfile
    app.run(host="0.0.0.0", port="5002")
