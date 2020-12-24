from flask import Flask, redirect, request, render_template
app = Flask(__name__)
app.secret_key='Our secret key is our secret key. None of your secret key'

@app.route('/',methods=['GET'])
def initial():
	print('Server running')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)