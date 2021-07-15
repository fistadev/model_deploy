from flask import Flask, render_template
import pickle
# import client

app = Flask(__name__)

# client = client()


# Get model and predict

# loaded_model = prepro.load_model()
# pred = loaded_model.predict(x_test)


@app.route("/")
def index():

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
