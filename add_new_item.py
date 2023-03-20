from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

@app.route('/add-new-item', methods=['POST'])
def add_new_item():
    # Get the user's login information from the request
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')
    name = request.form.get('name')

    _item = us.item(category)
    data = [x for x in _item if x["name"]== _item]
    # return jsonify(_user)
    #Get Data
    if (data):
        return jsonify({'message': 'Cannot create item.'}), 401
    else:
        us.add_item(name, price, instock, category)
        return jsonify({'message': 'Created successfully.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) #127.0.0.1