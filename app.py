from flask import Flask, render_template

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




if __name__ == '__main__':
	app.run()