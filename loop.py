from flask import Flask, render_template
app = Flask(__name__)

@app.route('/store/<string:name>')
def Store(name):
	items = [{'name': 'Ice cream', 'price': 50},
			 {'name': 'Cookie', 'price': 35},
			 {'name': 'Chocolate', 'price': 40},
			 {'name': 'Milk', 'price': 32.5}]
	return render_template('store.html', name=name, items=items)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
