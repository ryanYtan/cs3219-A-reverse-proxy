import random
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_image():
    urls = [
        "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_960_720.jpg",
        "https://cdn.pixabay.com/photo/2014/04/13/20/49/cat-323262_960_720.jpg",
        "https://cdn.pixabay.com/photo/2017/11/14/13/06/kitty-2948404_960_720.jpg",
        "https://cdn.pixabay.com/photo/2020/08/14/13/57/cat-5488070_960_720.jpg",
        "https://cdn.pixabay.com/photo/2016/11/29/10/07/animal-1868911_960_720.jpg"
    ]

    return {
        "imgsrc": random.choice(urls),
        "imgcap": request.args.get("name")
    }

if __name__  == "__main__":
    # has to correspond to port being exposed in dockerfile
    app.run(host="0.0.0.0", port="5002")
