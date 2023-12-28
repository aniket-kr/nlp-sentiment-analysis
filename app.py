from flask import Flask, request
from flask.templating import render_template

from model import predict

app = Flask(__name__)


@app.get('/')
def index():
  return render_template('index.html', has_output=False)


@app.post('/')
def make_prediction():
  query = str(request.form['query'])
  rating = predict(query) * 10

  return render_template('index.html',
                         has_output=True,
                         rating=rating,
                         query=query)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)