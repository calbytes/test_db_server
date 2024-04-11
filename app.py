from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/quote', methods = ['GET', 'POST'])
def get_quote():
    if(request.method == 'GET'):
        quote = get_random_quote()
        keys = ['quote', 'author', 'title']
        quote_dict = dict(zip(keys, quote))
        return jsonify(quote_dict)

def get_random_quote():
	quote = 'fake_db random quote'
	title = 'fake_db title'
	author = 'fake_db author'
	return quote, author, title

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
   
