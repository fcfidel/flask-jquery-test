from flask import Flask, render_template, redirect, url_for,jsonify, request

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD = True
)


@app.route('/')
def home():
	return "Home Page !!!!!!!"

@app.route('/test')
def testPage():
	que = "algo something lol lmfao"
	return render_template('home.html',x=que)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/add')
def index():
    return render_template('add.html')



@app.route('/_say_something')
def say_something():
	a = request.args.get('a',type=str)
	return jsonify(result=a)

@app.route('/algo')
def lol():
	return render_template('algo.html')


if __name__ == '__main__':
	app.run()