from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'


@app.route('/test_page')
def test_page_fn():
	return 'Hello there'
